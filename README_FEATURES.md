# 🚀 Network Routing Optimization - Yeni Özellikler

## 📋 İçindekiler
1. [Ana Ekran](#ana-ekran)
2. [Karşılaştırma Ekranı](#karşılaştırma-ekranı)
3. [Raporlar Ekranı](#raporlar-ekranı)
4. [Kullanım Kılavuzu](#kullanım-kılavuzu)

---

## 🏠 Ana Ekran

Ana ekran, tek bir algoritma ile hızlı yol bulma işlemleri için tasarlanmıştır.

### Özellikler:
- ✅ 250 düğümlü ağ topolojisi görselleştirme
- ✅ 4 farklı meta-sezgisel algoritma (GA, Q-Learning, PSO, SA)
- ✅ QoS ağırlık ayarlama (Gecikme, Güvenilirlik, Maliyet)
- ✅ Kaynak-hedef düğüm seçimi
- ✅ Canlı log konsolu
- ✅ Dark/Light tema desteği
- ✅ CSV dosya yükleme

### Nasıl Kullanılır:
1. **Algoritma Seçimi**: Açılır menüden algoritma seçin
2. **Kaynak/Hedef**: Düğüm numaralarını girin (0-249)
3. **QoS Ağırlıkları**: Slider'ları ayarlayın
4. **Hesapla**: "Yol Bul" butonuna tıklayın
5. **Sonuçları İncele**: Yol üzerinde renkli çizgi ve log konsolu

---

## 🔄 Karşılaştırma Ekranı

Birden fazla algoritmayı **aynı parametrelerle** karşılaştırarak performans analizi yapın.

### Özellikler:
- 🎯 **Performans Hedefleri**: 3 farklı önayar (Hız, Güvenilir, Dengeli)
- 🔬 **Algoritma Seçimi**: En az 2 algoritma seçebilirsiniz
- 📍 **Rota Parametreleri**: Kaynak, hedef ve talep ayarı
- 📊 **Gerçek Zamanlı Sonuçlar**: Her algoritma için ayrı kart
- ⏱️ **Hesaplama Süresi**: Her algoritmanın çalışma süresi
- 🎨 **Modern UI**: Kart tabanlı, renkli metrik gösterimi

### Kullanım Adımları:
1. **Hedef Belirle**: "Hız", "Güvenilir" veya "Dengeli" butonuna tıklayın
   - Veya manuel olarak slider'ları ayarlayın
2. **Algoritmaları Seç**: Karşılaştırmak istediğiniz algoritmaları işaretleyin (min 2)
3. **Rota Gir**: Kaynak, hedef ve talep değerlerini girin
4. **Analiz Et**: "▶ Analizi Başlat" butonuna tıklayın
5. **Sonuçları Karşılaştır**: Sağ panelde metrik kartlarını inceleyin

### Metrikler:
- **Gecikme (ms)**: Toplam yol gecikmesi (düşük = iyi)
- **Güvenilirlik (%)**: Yol güvenilirlik oranı (yüksek = iyi)
- **Maliyet**: Kaynak kullanım maliyeti (düşük = iyi)
- **Hesaplama Süresi**: Algoritmanın çalışma süresi

---

## 📈 Raporlar Ekranı

Karşılaştırma sonuçlarını detaylı grafik ve tablolarla analiz edin.

### 3 Ana Tab:
#### 1️⃣ Genel Özet
- **En Hızlı Algoritma**: En düşük gecikme
- **En Güvenilir Algoritma**: En yüksek güvenilirlik
- **En Verimli Algoritma**: En düşük maliyet
- **En Dengeli Algoritma**: Normalize skorlara göre en iyi

📋 **Detaylı Performans Tablosu**: Tüm metrikleri normalize skorlar ile karşılaştırma

#### 2️⃣ Algoritma Karşılaştırması
📊 **Bar Grafikleri**: 3 yan yana grafik
- Gecikme karşılaştırması
- Güvenilirlik karşılaştırması
- Maliyet karşılaştırması

#### 3️⃣ Performans Analizi
🕸️ **Radar (Spider) Grafiği**: Tüm algoritmaların 3 metrikte performans gösterimi
- Her algoritma farklı renk
- Dolu alanlar güçlü yönleri gösterir

### Dışa Aktarma:
- **📊 CSV Dışa Aktar**: Tüm sonuçları Excel'de açabilirsiniz
- **📄 PDF İndir**: (Yakında eklenecek)
- **🔄 Raporları Yenile**: Yeni karşılaştırma sonralarını grafiğe ekler

---

## 📚 Kullanım Kılavuzu

### Adım 1: Program Başlatma
```bash
python main.py
```

### Adım 2: İlk Karşılaştırma
1. Menü bar'da **🔄 Karşılaştırma**'ya tıklayın
2. "Dengeli" butonuna tıklayın (tüm metrikler eşit ağırlık)
3. Kaynak: 0, Hedef: 249, Talep: 100 bırakın
4. 4 algoritma da seçili olsun
5. **▶ Analizi Başlat** butonuna tıklayın
6. Log konsolundan algoritmaların çalışmasını izleyin
7. Sağ panelde sonuç kartlarını inceleyin

### Adım 3: Raporları İncele
1. Menü bar'da **📈 Raporlar**'a tıklayın
2. **Genel Özet** tab'ında en iyi algoritmaları görün
3. **Algoritma Karşılaştırması** tab'ında bar grafiklerini inceleyin
4. **Performans Analizi** tab'ında radar grafiğine bakın
5. **📊 CSV Dışa Aktar** ile sonuçları kaydedin

### Farklı Senaryolar:
#### Senaryo 1: Hız Odaklı
- "Hız" butonuna tıklayın (Gecikme %80)
- GA ve PSO algoritmalarını seçin
- Hangi algoritma daha hızlı bulur?

#### Senaryo 2: Güvenilirlik Odaklı
- "Güvenilir" butonuna tıklayın (Güvenilirlik %80)
- Q-Learning ve SA'yı seçin
- Hangi algoritma daha güvenilir yol bulur?

#### Senaryo 3: Farklı Node'lar
- Kaynak: 50, Hedef: 200 gibi farklı değerler deneyin
- Tüm algoritmaları karşılaştırın
- Hangi algoritma bu senaryoda daha iyi?

---

## 🎨 UI Özellikleri

### Modern Tasarım:
- ✨ **Kart Tabanlı Layout**: Her özellik ayrı kartta
- 🎨 **Gradient Butonlar**: Önemli aksiyonlarda gradient efektler
- 📊 **Renkli Metrikler**: Her metrik farklı renk borderlı kart
- 🌙 **Dark Theme**: Göz yorulmayan koyu tema
- 🔲 **Responsive**: Pencere boyutuna göre uyum

### İkonlar:
- 🏠 Ana Ekran
- 🔄 Karşılaştırma
- 📈 Raporlar
- 🧬 Genetik Algoritma
- 🤖 Q-Learning
- 🐝 PSO
- 🔥 Benzetimli Tavlama
- ⚡ En Hızlı
- 🛡️ En Güvenilir
- 💰 En Verimli
- ⚖️ En Dengeli

---

## 🔧 Teknik Detaylar

### Algoritmalar:
1. **Genetik Algoritma (GA)**: Evrimsel süreçler, mutasyon ve crossover
2. **Q-Learning (RL)**: Takviyeli öğrenme, ajan tabanlı keşif
3. **PSO (Meta-Heuristic)**: Parçacık sürü optimizasyonu
4. **Benzetimli Tavlama (SA)**: Simulated annealing, soğutma parametreleri

### Metrik Hesaplama:
- **Normalize Skor**: Her metrik 0-1 arasına normalize edilir
- **Dengeli Skor**: 3 metriğin normalize ortalaması
- **Ağırlıklı Toplam**: Kullanıcının belirlediği QoS ağırlıkları

### Performans:
- **250 Düğüm, ~1200 Kenar**: Orta ölçekli ağ
- **GA**: ~2-5 saniye
- **Q-Learning**: ~3-7 saniye (öğrenme fazı dahil)
- **PSO**: ~1-3 saniye
- **SA**: ~2-5 saniye (optimize edilmiş)

---

## 📦 Gereksinimler

```txt
PyQt5>=5.15.0
matplotlib>=3.7.0
networkx>=3.0
numpy>=1.24.0
```

---

## 🚨 Bilinen Sınırlamalar

1. **Radar Grafik**: Matplotlib'in polar subplot özelliği kullanıldığında bazı type hint uyarıları çıkabilir (çalışmayı etkilemez)
2. **PDF Dışa Aktarma**: Henüz implementeasyon edilmedi, CSV alternatifi mevcut
3. **Büyük Ağlar**: 500+ düğüm ağlarda görselleştirme yavaşlayabilir

---

## 🎯 Gelecek Özellikler

- [ ] PDF rapor dışa aktarma
- [ ] Histogram grafikleri (hesaplama süresi)
- [ ] Karşılaştırma geçmişi (önceki analizler)
- [ ] Algoritma parametrelerini özelleştirme
- [ ] Batch analiz (birden fazla kaynak-hedef çifti)
- [ ] 3D ağ görselleştirmesi

---

## 📞 Destek

Herhangi bir sorun veya öneriniz varsa lütfen iletişime geçin.

---

**Version**: 2.0.0  
**Last Updated**: 2024  
**License**: MIT
