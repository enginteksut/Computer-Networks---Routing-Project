import networkx as nx
import random
import math

class TopologyManager:
    def __init__(self):
        self.G = None
        self.pos = None
        self.num_nodes = 250

    def create_network(self):
        """Ağı ve ÇATIŞAN verileri oluşturur (Trade-off Logic)"""
        # 1. Topoloji
        # Seed None yaptık ki her seferinde farklı ağ gelsin
        self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=0.04, seed=None) 
        
       
        # Bağlantı garantisi
        if not nx.is_connected(self.G):
            components = list(nx.connected_components(self.G))
            for i in range(len(components)-1):
                #kopuk parçaları birbiribe bağlama,
                u = list(components[i])[0]
                v = list(components[i+1])[0]
                self.G.add_edge(u,v)
       
        self.pos = nx.spring_layout(self.G, seed=42)

        # 2. Düğüm Özellikleri
        for node in self.G.nodes():
            self.G.nodes[node]['proc_delay'] = random.uniform(0.5, 2.0)
            self.G.nodes[node]['reliability'] = random.uniform(0.95, 0.999)

        # 3. Bağlantı Özellikleri (TRADE-OFF MEKANİZMASI)
        link_types = ["fiber", "microwave", "satellite"]
        
        for u, v in self.G.edges():
            l_type = random.choice(link_types)
            
            if l_type == "fiber":
                # FİBER: Çok Hızlı, Geniş Bant, Düşük Güvenilirlik (Riskli)
                delay = random.uniform(1, 5)       
                bw = random.uniform(800, 1000)      
                rel = random.uniform(0.90, 0.95)    
                
            elif l_type == "microwave":
                # MİKRODALGA: Orta değerler
                delay = random.uniform(5, 10)
                bw = random.uniform(300, 600)
                rel = random.uniform(0.95, 0.98)
                
            else: # satellite
                # UYDU: Çok Yavaş, Dar Bant ama Çok Sağlam
                delay = random.uniform(20, 50)      
                bw = random.uniform(10, 100)        
                rel = random.uniform(0.99, 0.9999)  
            
            # Değerleri Ata
            self.G.edges[u, v]['link_delay'] = delay
            self.G.edges[u, v]['bandwidth'] = bw
            self.G.edges[u, v]['reliability'] = rel
            self.G.edges[u, v]['type'] = l_type

        return self.G, self.pos

   
    def calculate_path(self, source, target, w_delay, w_rel, w_res, algorithm="Dijkstra"):
        """
        Seçilen algoritmaya göre rotayı hesaplar.
        """
        if self.G is None: return None

        # DEĞİŞKEN TANIMLARI EN BAŞA ALINDI 
        # Ağırlıkları normalize ediyoruz
        total_w = w_delay + w_rel + w_res
        if total_w == 0: total_w = 1
        
        wd = w_delay / total_w
        wr = w_rel / total_w
        wres = w_res / total_w
      

        # Grafikteki ağırlıkları güncelle
        for u, v in self.G.edges():
            data = self.G.edges[u, v]
            
            cost_delay = data['link_delay']
            
            # Güvenilirlik logaritması (Hata almamak için kontrol)
            if data['reliability'] > 0:
                cost_reliability = -math.log(data['reliability'])
            else:
                cost_reliability = 100 # Çok yüksek maliyet ata
            
            # Kaynak maliyeti (Sıfıra bölünme koruması)
            if data['bandwidth'] > 0:
                cost_resource = 1000.0 / data['bandwidth']
            else:
                cost_resource = 1000.0 # Varsayılan yüksek maliyet

            # Weighted Sum Method (Artık wd, wr, wres tanımlı olduğu için çalışır)
            total_cost = (wd * cost_delay) + (wr * cost_reliability * 100) + (wres * cost_resource)
            
            # Dinamik ağırlığı kenara kaydet
            self.G.edges[u, v]['dynamic_weight'] = total_cost

        # --- ALGORİTMA SEÇİM MANTIĞI ---
        try:
            path = []
            
            # Algoritma ismine göre seçim (Arayüzden gelen string ile eşleşmeli)
            if "Genetik" in algorithm:
                # İLERİDE BURAYA GA KODU GELECEK
                # Şimdilik çökmemesi için Dijkstra kullanıyoruz
                path = nx.shortest_path(self.G, source=source, target=target, weight='dynamic_weight')

            elif "Q-Learning" in algorithm:
                # İLERİDE BURAYA RL KODU GELECEK
                path = nx.shortest_path(self.G, source=source, target=target, weight='dynamic_weight')
            
            else:
                # Varsayılan: Dijkstra
                path = nx.shortest_path(self.G, source=source, target=target, weight='dynamic_weight')
            
            # --- METRİK HESAPLAMA ---
            metrics = {
                "total_delay": 0,
                "reliability_log": 0,
                "resource_cost": 0,
                "path": path,
                "final_reliability": 0 # Varsayılan değer
            }

            if not path: return None

            # Kenar metriklerini topla
            for i in range(len(path)-1):
                u, v = path[i], path[i+1]
                d = self.G.edges[u, v]
                metrics["total_delay"] += d['link_delay']
                metrics["reliability_log"] += -math.log(d['reliability'])
                metrics["resource_cost"] += (1000.0 / d['bandwidth'])
            
            # Düğüm gecikmelerini ekle (Kaynak ve Hedef hariç ara düğümler)
            for node in path[1:-1]:
                metrics["total_delay"] += self.G.nodes[node]['proc_delay']

            # Log güvenilirliğini yüzdeye çevir
            metrics["final_reliability"] = math.exp(-metrics["reliability_log"]) * 100
            
            return metrics

        except nx.NetworkXNoPath:
            return None
        except Exception as e:
            print(f"Hata oluştu: {e}") # Konsola hatayı yazdırır, çökmez
            return None
    
    def build_from_csv(self, node_file, edge_file):
        try:
            self.G = nx.Graph() # yönsüz graph
            
            # 1. Düğüm dosyasını oku
            with open (node_file, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                # Başlığı atlama 
                header = lines[0].strip().split(';')
                
                for line in lines[1:]:
                    if not line.strip(): continue
                    parts = line.strip().split(';')
                    
                    # CSV formatı : node_ıd; s_ms; r_node
                    node_id = int(parts[0])
                    proc_delay = float(parts[1].replace(',' , '.')) # Virgülü noktaya çevir
                    reliability = float(parts[2].replace(',', '.'))  
                    
            # Kenar dosyasını oku
            with open(edge_file, 'r', encoding='utf-8-sig') as f:
                
                lines = f.readlines()
                # Başlığı atla
                header = lines[0].strip().split(';')
                
                for line in lines[1:]:
                    if not line.strip(): continue
                    parts = line.strip().split(';')
                    
                    # CSV Formatı: src; dst; capacity_mbps; delay_ms; r_link
                    u = int(parts[0])
                    v = int(parts[1])
                    bw = float(parts[2].replace(',', '.')) # Bazen tam sayı olabilir ama float güvenlidir
                    delay = float(parts[3].replace(',', '.'))
                    rel = float(parts[4].replace(',', '.'))
                    
                    # Grafiğe ekle
                    self.G.add_edge(u,v,bandwidth=bw, 
                                    link_delay=delay, 
                                    reliability=rel,
                                    type='custom') # Tipi custom olsun
            
            
            # Yerleşim ve Güncelleme 
            # Bağlantı garantisi kontrolü
            if not nx.is_connected(self.G):
                # Kopuksa en büyük parçayı al veya bağla
                pass
            
            self.pos = nx.spring_layout(self.G, seed=42)
            self.num_nodes = len(self.G.nodes())
            
            return self.G, self.pos, True
        except Exception as e:
            print(f"CSV okuma hatası: {e}")
            return None, None, False       
                       