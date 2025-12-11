# 🚀 QoS-Intelligence: Akıllı Rotalama ve Simülasyon Platformu

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green?style=for-the-badge&logo=qt)
![NetworkX](https://img.shields.io/badge/Network-NetworkX-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-yellow?style=for-the-badge)

Bu proje, **2025-2026 Güz Dönemi Bilgisayar Ağları (BSM307)** dersi kapsamında; Veri Merkezi (Datacenter) ağlarında **QoS (Hizmet Kalitesi)** odaklı rotalama problemlerini çözmek ve görselleştirmek için **Grup 6** tarafından geliştirilmiştir.

Proje, karmaşık ağ topolojilerinde en optimum yolu bulmak için klasik algoritmaların yanı sıra **Meta-Sezgisel** ve **Pekiştirmeli Öğrenme** yaklaşımlarını hibrit bir yapıda kullanmayı hedefler.

## 🎯 Proje Amacı ve Kapsam

250 düğümlü karmaşık bir ağ üzerinde, aşağıdaki çelişen hedeflerin optimize edilmesi amaçlanmıştır:
* ⏱️ **En Az Gecikme (Minimum Delay)**
* 🛡️ **En Yüksek Güvenilirlik (Maximum Reliability)**
* 💰 **En Az Kaynak Maliyeti (Minimum Resource Cost)**

## 📸 Arayüz ve Simülasyon (GUI)

Proje, algoritmaların performansını anlık olarak izlemek için **PyQt5** tabanlı, modern bir arayüze sahiptir.

### 🌙 Deep Ocean (Karanlık) & ☀️ Corporate (Aydınlık) Modları

<table>
  <tr>
    <td align="center"><b>Karanlık Mod - Genel Görünüm</b></td>
    <td align="center"><b>Aydınlık Mod - Genel Görünüm</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/arayuzkoyu1.png" width="400" alt="Karanlık Mod 1"></td>
    <td><img src="screenshots/arayuzacik1.png" width="400" alt="Aydınlık Mod 1"></td>
  </tr>
  <tr>
    <td align="center"><b>Karanlık Mod - Rota Hesaplama</b></td>
    <td align="center"><b>Aydınlık Mod - Rota Hesaplama</b></td>
  </tr>
  <tr>
    <td><img src="screenshots/arayuzkoyu2.png" width="400" alt="Karanlık Mod 2"></td>
    <td><img src="screenshots/arayuzacik2.png" width="400" alt="Aydınlık Mod 2"></td>
  </tr>
</table>

### ✨ Arayüz Özellikleri
* **Dinamik Dashboard:** Rota metriklerini (Gecikme, Maliyet) anlık gösteren kart yapısı.
* **Neon Görselleştirme:** Aktif rotayı parlama (glow) efektiyle vurgulayan Matplotlib motoru.
* **Akıllı Kontroller:** Kaynak/Hedef seçimi ve QoS ağırlıklarının slider ile yönetimi.

## ⚙️ Teknik Altyapı ve Algoritmalar

Proje mimarisi modüler bir yapıda tasarlanmış olup, aşağıdaki algoritmalar entegre edilmektedir:

1.  **Benzetimli Tavlama (Simulated Annealing - SA):** Soğutma takvimi ve komşuluk fonksiyonları ile yerel minimumdan kaçış stratejileri.
2.  **Genetik Algoritma (GA):** Kromozom tabanlı rota temsili, çaprazlama (crossover) ve mutasyon operatörleri.
3.  **Q-Learning (RL):** Ajan tabanlı öğrenme, Bellman denklemi ile Q-Tablosu güncellemesi ve Epsilon-Greedy yaklaşımı.
4.  **Parçacık Sürüsü Optimizasyonu (PSO):** Sürü zekası ile hız ve konum güncelleme vektörleri.

## 🛠️ Kurulum

Projeyi yerel ortamınızda çalıştırmak için:

```bash
# 1. Depoyu klonlayın
git clone [https://github.com/enginteksut/Computer-Networks---Routing-Project.git](https://github.com/enginteksut/Computer-Networks---Routing-Project.git)

# 2. Proje dizinine gidin
cd Computer-Networks---Routing-Project

# 3. Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 4. Uygulamayı başlatın
python main.py