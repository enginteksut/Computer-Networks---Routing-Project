# 📡 Multi-QoS Network Routing Optimization System

> **Proje:** Bilgisayar Ağları Dönem Projesi  
> **Üniversite:** Bartın Üniversitesi  
> **Ders:**  Bilgisayar Ağları

---

## 📋 Proje Özeti

Bu proje, **çoklu QoS (Quality of Service) kısıtlı ağ rotalama optimizasyonu** problemini ele almaktadır. Kullanıcı dostu PyQt5 arayüzü ile 4 farklı optimizasyon algoritmasını karşılaştırmalı olarak test edebilirsiniz.

### 🎯 Temel Özellikler

- **Trade-off Mekanizması**: Fiber (hızlı-riskli), Microwave (dengeli), Satellite (yavaş-güvenli) link tipleri
- **3 QoS Kriteri**: Gecikme (Delay), Güvenilirlik (Reliability), Kaynak Kullanımı (Resource)
- **4 Algoritma Desteği**: 
  - Q-Learning (Pekiştirmeli Öğrenme)
  - PSO (Parçacık Sürü Optimizasyonu)
  - Genetik Algoritma (Evrimsel Hesaplama)
  - Benzetimli Tavlama (Simulated Annealing)
- **Karşılaştırma Modu**: Aynı ağ üzerinde farklı algoritmaları yan yana test etme
- **Görselleştirme**: Gerçek zamanlı ağ grafiği ve rota çizimi
- **Raporlama**: PDF ve TXT formatında detaylı metrik raporları

---

## 🖥️ Ekran Görüntüleri

### Ana Ekran (Tek Algoritma Modu)
![Ana Ekran](screenshots/Ana_Ekran.png)

### Karşılaştırma Ekranı (Multi-Algoritma)
![Karşılaştırma Ekranı](screenshots/Karsilastirma.png)

### Raporlar Ekranı
![Raporlar Ekranı](screenshots/Rapor1.png)

![Raporlar Ekranı](screenshots/Rapo2.png)

### Konsol Ekranı
![Konsol Ekranı](screenshots/Konsol.png)

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

- **Python 3.8+** (Önerilen: Python 3.10)
- **İşletim Sistemi**: Windows 10/11, Linux, macOS

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/enginteksut/Computer-Networks---Routing-Project.git
cd network-qos-routing
```

### 2. Sanal Ortam Oluşturun (Önerilen)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Gereksinimleri Yükleyin

```bash
pip install -r requirements.txt
```

**requirements.txt** içeriği:
```
PyQt5==5.15.9
networkx==3.1
matplotlib==3.7.2
numpy==1.24.3
pandas==2.0.3
```

### 4. Uygulamayı Başlatın

```bash
python main.py
```

---

## 🎮 Kullanım Kılavuzu

### Ana Ekran (Tek Algoritma Modu)

1. **Ağ Oluşturma:**
   - Düğüm sayısını ayarlayın (varsayılan 250)
   - "Ağ Oluştur" butonuna tıklayın
   - Alternatif: "CSV'den Yükle" ile özel ağ yükleyin

2. **Kaynak-Hedef Seçimi:**
   - Grafikte düğümlere tıklayarak kaynak ve hedef seçin
   - Veya manuel olarak ID'leri girin

3. **Algoritma Parametreleri:**
   - "Diğer Özellikler ⚙️" butonuyla algoritma parametrelerini düzenleyin
   - Q-Learning: alpha, gamma, epsilon, episodes
   - PSO: swarm_size, iterations, w, c1, c2
   - GA: population, generations, crossover_rate, mutation_rate
   - SA: initial_temp, cooling_rate, iterations

4. **QoS Ağırlıkları:**
   - Kaydırıcılarla gecikme, güvenilirlik ve kaynak ağırlıklarını ayarlayın
   - Toplamın 1.0 olması otomatik normalize edilir

5. **Hesaplama:**
   - "Hesapla ve Çiz" butonuyla rotayı bulun
   - Sonuçlar sağ panelde görüntülenir

### Karşılaştırma Ekranı

1. Karşılaştırmak istediğiniz algoritmaları seçin (checkbox)
2. Her algoritma için ⚙️ butonuyla parametreleri düzenleyin
3. "Tümünü Hesapla" ile tüm algoritmaları çalıştırın
4. Sonuçları tablo formatında görün ve karşılaştırın

### Raporlar Ekranı

- **PDF Raporu**: Detaylı metrikler, grafik ve açıklamalar
- **TXT Raporu**: Ham veri formatında raporlar
- Son 10 hesaplama geçmişini görüntüleme

---

## 📊 Algoritma Parametreleri

### Q-Learning
| Parametre | Varsayılan | Açıklama |
|-----------|------------|----------|
| alpha     | 0.1        | Öğrenme hızı (0-1) |
| gamma     | 0.9        | İndirim faktörü (0-1) |
| epsilon   | 0.9        | Keşif oranı (0-1) |
| episodes  | 500        | Eğitim episode sayısı |

### PSO
| Parametre     | Varsayılan | Açıklama |
|---------------|------------|----------|
| swarm_size    | 30         | Parçacık sayısı |
| iterations    | 100        | İterasyon sayısı |
| w (inertia)   | 0.7        | Atalet ağırlığı |
| c1 (cognitive)| 1.5        | Bilişsel katsayı |
| c2 (social)   | 2.0        | Sosyal katsayı |

### Genetik Algoritma
| Parametre        | Varsayılan | Açıklama |
|------------------|------------|----------|
| population       | 50         | Popülasyon boyutu |
| generations      | 200        | Jenerasyon sayısı |
| crossover_rate   | 0.8        | Çaprazlama olasılığı |
| mutation_rate    | 0.08       | Mutasyon olasılığı |

### Benzetimli Tavlama
| Parametre      | Varsayılan | Açıklama |
|----------------|------------|----------|
| initial_temp   | 10000      | Başlangıç sıcaklığı |
| cooling_rate   | 0.995      | Soğutma oranı |
| iterations     | 1000       | İterasyon sayısı |

---

## 🌐 Ağ Yapısı ve Trade-off Mekanizması

### Link Tipleri

Ağ, üç farklı link tipiyle **trade-off** özelliğine sahiptir:

| Link Tipi | Bant Genişliği | Gecikme | Güvenilirlik | Kullanım Senaryosu |
|-----------|----------------|---------|--------------|---------------------|
| **Fiber** | 800-1000 Mbps  | 1-5 ms  | 0.90-0.95    | Yüksek hız gerekli, risk kabul edilir |
| **Microwave** | 300-600 Mbps | 5-10 ms | 0.95-0.98    | Dengeli performans |
| **Satellite** | 10-100 Mbps | 20-50 ms | 0.99-0.9999  | Kritik güvenilirlik gerekli |

### QoS Metrikleri

1. **Gecikme (Delay)**: Link gecikmeleri + ara düğüm işlem süreleri
2. **Güvenilirlik (Reliability)**: Çarpımsal metrik (tüm bileşenlerin güvenilirliği)
3. **Kaynak Kullanımı (Resource)**: Bant genişliği ile ters orantılı maliyet

---

## 📁 Proje Yapısı

```
project/
├── main.py                      # Ana uygulama (PyQt5 arayüzü)
├── topology.py                  # Ağ topolojisi ve algoritma entegrasyonu
├── requirements.txt             # Python bağımlılıkları
├── README.md                    # Bu dosya
├── Algorithms/
│   ├── __init__.py
│   ├── qlearning_algorithm.py   # Q-Learning implementasyonu
│   ├── pso.py                   # PSO implementasyonu
│   ├── ga.py                    # Genetik Algoritma implementasyonu
│   ├── sa_algorithm.py          # Benzetimli Tavlama implementasyonu
│   ├── metrics.py               # Metrik hesaplama fonksiyonları
│   ├── network_generator.py     # Ağ oluşturma yardımcıları
│   ├── NodeData.csv             # Örnek düğüm verileri
│   ├── EdgeData.csv             # Örnek kenar verileri
│   └── DemandData.csv           # Örnek talep verileri
├── screenshots/                 # Ekran görüntüleri
│   ├── main_screen.png
│   ├── comparison_screen.png
│   └── reports_screen.png
└── reports/                     # Oluşturulan raporlar (otomatik oluşturulur)
    ├── *.pdf
    └── *.txt
```

---

## 🔬 Algoritma Performans Karşılaştırması

| Algoritma | Hız | Çözüm Kalitesi | Bellek Kullanımı | En İyi Senaryo |
|-----------|-----|----------------|------------------|----------------|
| **Q-Learning** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Dinamik ağlar, öğrenme gerekli |
| **PSO** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Global optimum aranıyor |
| **Genetik** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Karmaşık kısıtlar |
| **SA** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Lokal minimumdan kaçış |

---

## 🛠️ Teknik Detaylar

### Kullanılan Kütüphaneler

- **PyQt5**: GUI framework
- **NetworkX**: Graf algoritmaları ve veri yapıları
- **Matplotlib**: Ağ görselleştirme
- **NumPy**: Sayısal hesaplamalar (PSO, GA)
- **Pandas**: CSV veri işleme

### Optimizasyon Yöntemi

**Weighted Sum Method** ile çoklu QoS kısıtları tek fitness fonksiyonuna dönüştürülür:

```
fitness = w_delay * Delay + w_reliability * ReliabilityCost + w_resource * ResourceCost
```

Güvenilirlik maliyeti logaritmik ölçekte hesaplanır:
```
ReliabilityCost = -ln(reliability)
```

---

## 🐛 Bilinen Sorunlar ve Çözümler

### Problem: "No module named 'PyQt5'"
**Çözüm:**
```bash
pip install PyQt5==5.15.9
```

### Problem: Ağ bağlantısız (disconnected) hatası
**Çözüm:** Düğüm sayısını artırın veya bağlantı olasılığını yükseltin (create_network içinde `p=0.04` → `p=0.06`)

### Problem: Genetik Algoritma "Başlangıç popülasyonu oluşturulamadı"
**Çözüm:** Bant genişliği talebini azaltın veya daha büyük ağ oluşturun

---

## 📚 Kaynaklar ve Referanslar

1. **NetworkX Documentation**: https://networkx.org/documentation/stable/
2. **PyQt5 Tutorial**: https://www.riverbankcomputing.com/static/Docs/PyQt5/
3. **Q-Learning**: Sutton & Barto - Reinforcement Learning: An Introduction
4. **PSO**: Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization
5. **Genetik Algoritmalar**: Goldberg, D. E. (1989). Genetic Algorithms
6. **Benzetimli Tavlama**: Kirkpatrick, S., et al. (1983). Optimization by simulated annealing

---

## 🔐 Seed Bilgisi ve Tekrarlanabilirlik

Ağ topolojisi her çalıştırmada **farklı** üretilir (`seed=None` kullanılmaktadır). Deterministik testler için:

```python
# topology.py içinde
self.G = nx.erdos_renyi_graph(n=self.num_nodes, p=0.04, seed=42)  # Sabit seed
```

**Mevcut Seed Durumu**: `seed=None` (rastgele ağ üretimi)  
**Görselleştirme Seed**: `seed=42` (spring_layout için sabit konumlar)

---

## 👥 Ekip ve Katkıda Bulunanlar

- **Proje Lideri**: [İsim Soyisim]
- **Algoritma Geliştirme**: [İsim Soyisim]
- **UI/UX Tasarım**: [İsim Soyisim]
- **Test ve Dokümantasyon**: [İsim Soyisim]

---

## 📝 Lisans

Bu proje akademik amaçlı geliştirilmiştir. [Üniversite Adı] Bilgisayar Ağları Dersi kapsamında kullanılmak üzere hazırlanmıştır.

---

## 📧 İletişim

Sorularınız için:
- **E-posta**: [email@example.com]
- **GitHub Issues**: [Repository Issues Link]

---

## 🎓 Teşekkürler

- [Hoca Adı] - Ders Sorumlusu
- [Üniversite Adı] Bilgisayar Mühendisliği Bölümü
- NetworkX ve PyQt5 açık kaynak topluluğu

---

**Son Güncelleme**: 31 Aralık 2025  
**Versiyon**: 1.0.0
