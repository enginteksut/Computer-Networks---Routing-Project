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

    def calculate_path(self, source, target, w_delay, w_rel, w_res):
        """En kısa yolu hesaplar ve sonuç sözlüğü döner"""
        if self.G is None:
            return None

        # Ağırlıkları güncelle
        for u, v in self.G.edges():
            data = self.G.edges[u, v]
            
            cost_delay = data['link_delay']
            cost_reliability = -math.log(data['reliability'])
            cost_resource = 1000.0 / data['bandwidth']

            # Dinamik Ağırlık Hesabı
            total_weight = (w_delay * cost_delay) + \
                           (w_rel * cost_reliability * 100) + \
                           (w_res * cost_resource)
            
            self.G.edges[u, v]['dynamic_weight'] = total_weight

        # Hesapla (Dijkstra)
        try:
            path = nx.shortest_path(self.G, source=source, target=target, weight='dynamic_weight')
            
            # Sonuç Metriklerini Topla
            metrics = {
                "total_delay": 0,
                "reliability_log": 0,
                "resource_cost": 0,
                "path": path
            }

            for i in range(len(path)-1):
                u, v = path[i], path[i+1]
                d = self.G.edges[u, v]
                metrics["total_delay"] += d['link_delay']
                metrics["reliability_log"] += -math.log(d['reliability'])
                metrics["resource_cost"] += (1000.0 / d['bandwidth'])
            
            # Düğüm gecikmeleri
            for node in path[1:-1]:
                metrics["total_delay"] += self.G.nodes[node]['proc_delay']

            # Log güvenilirliğini yüzdeye çevir
            metrics["final_reliability"] = math.exp(-metrics["reliability_log"]) * 100
            
            return metrics

        except nx.NetworkXNoPath:
            return None