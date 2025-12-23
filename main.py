import sys
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QPushButton, QLabel, QComboBox, QSlider, 
                             QGroupBox, QFormLayout, QFrame, QGraphicsDropShadowEffect, 
                             QSizePolicy, QStyle, QLineEdit, QFileDialog)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QIntValidator

# --- HARİCİ MODÜL ENTEGRASYONU ---
from topology import TopologyManager 

# =============================================================================
# 1. CSS STİL ŞABLONLARI
# =============================================================================

COMMON_CSS = """
QWidget { font-family: 'Segoe UI', sans-serif; }

/* Panel Kartları (Sol Menü) */
QFrame#PanelCard { 
    border-radius: 10px; 
    border-left: 4px solid; 
}
QLabel#PanelTitle { font-size: 13px; font-weight: bold; margin-bottom: 2px; text-transform: uppercase; letter-spacing: 0.5px; }

/* Dashboard Metrik Kartları (Alt Kısım - BÜYÜTÜLDÜ) */
QFrame#MetricCard { border-radius: 12px; }
QLabel#MetricTitle { font-size: 11px; font-weight: bold; letter-spacing: 1px; opacity: 0.8; }
QLabel#MetricValue { font-size: 28px; font-weight: bold; } /* Font büyüdü */

/* Grafik Çerçevesi */
QFrame#GraphContainer { 
    border-radius: 12px; 
    border: 2px solid; 
}

/* Grafik Başlığı (Sağ Üst Header - Sol ile Eşitlendi) */
QLabel#GraphHeader {
    border-radius: 6px; 
    padding: 12px; 
    font-size: 16px; 
    font-weight: bold;
    margin-bottom: 5px;
}
"""

# --- KARANLIK MOD ---
DARK_THEME = COMMON_CSS + """
QMainWindow, QWidget { background-color: #1e1e2e; color: #cdd6f4; }

/* Kartlar */
QFrame#PanelCard { background-color: #262636; border: 1px solid #313244; border-left-color: #89b4fa; }
QLabel#PanelTitle { color: #89b4fa; }

/* Headerlar (Hem Sol Hem Sağ) */
QLabel#HeaderLabel, QLabel#GraphHeader { 
    background-color: #313244; color: #ffffff; 
    border: 1px solid #45475a;
}
/* Sağ Header Rota Hesaplandığında Renklensin diye özel ID */
QLabel#GraphHeader[active="true"] { color: #fab387; border-color: #fab387; }

/* Form Elemanları */
QComboBox { background-color: #1e1e2e; border: 1px solid #45475a; border-radius: 5px; padding: 5px; color: #cdd6f4; }
QComboBox::drop-down { border: none; width: 20px; }
QComboBox::down-arrow { image: none; border-left: 2px solid #45475a; } 
QComboBox QAbstractItemView { background-color: #1e1e2e; color: #cdd6f4; selection-background-color: #45475a; }

QSlider::groove:horizontal { background: #313244; height: 6px; border-radius: 3px; }
QSlider::handle:horizontal { background: #89b4fa; width: 14px; height: 14px; margin: -4px 0; border-radius: 7px; }

/* Grafik Alanı */
QFrame#GraphContainer { background-color: #232330; border-color: #313244; } 

/* Metrik Kartları */
QFrame#MetricCard { background-color: #262636; border: 1px solid #313244; }
QLabel#MetricTitle { color: #a6adc8; }
QLabel#MetricValue { color: #ffffff; }

/* Butonlar */
QPushButton { border-radius: 6px; font-weight: bold; font-size: 13px; }
QPushButton#CalcBtn { background-color: #a6e3a1; color: #1e1e2e; border: none; }
QPushButton#CalcBtn:hover { background-color: #94e2d5; }
QPushButton#ResetBtn { background-color: #fab387; color: #1e1e2e; border: none; }
QPushButton#ResetBtn:hover { background-color: #f9e2af; }
QPushButton#ThemeBtn { background-color: #313244; color: #cdd6f4; border: 1px solid #45475a; font-size: 14px; }
"""

# --- AYDINLIK MOD ---
LIGHT_THEME = COMMON_CSS + """
QMainWindow, QWidget { background-color: #f3f4f6; color: #374151; }

/* Kartlar */
QFrame#PanelCard { background-color: #ffffff; border: 1px solid #e5e7eb; border-left-color: #3b82f6; }
QLabel#PanelTitle { color: #3b82f6; }

/* Headerlar */
QLabel#HeaderLabel, QLabel#GraphHeader { 
    background-color: #ffffff; color: #111827; 
    border: 1px solid #d1d5db;
}
QLabel#GraphHeader[active="true"] { color: #ef4444; border-color: #ef4444; }

/* Form Elemanları */
QComboBox { background-color: #ffffff; border: 1px solid #d1d5db; border-radius: 5px; padding: 5px; color: #1f2937; }
QComboBox QAbstractItemView { background-color: white; color: black; selection-background-color: #bfdbfe; }

QSlider::groove:horizontal { background: #e5e7eb; height: 6px; border-radius: 3px; }
QSlider::handle:horizontal { background: #3b82f6; width: 14px; height: 14px; margin: -4px 0; border-radius: 7px; }

/* Grafik Alanı */
QFrame#GraphContainer { background-color: #ffffff; border-color: #e5e7eb; }

/* Metrik Kartları */
QFrame#MetricCard { background-color: #ffffff; border: 1px solid #e5e7eb; }
QLabel#MetricTitle { color: #6b7280; }
QLabel#MetricValue { color: #111827; }

/* Butonlar */
QPushButton { border-radius: 6px; font-weight: bold; font-size: 13px; }
QPushButton#CalcBtn { background-color: #10b981; color: white; border: none; }
QPushButton#CalcBtn:hover { background-color: #059669; }
QPushButton#ResetBtn { background-color: #f59e0b; color: white; border: none; }
QPushButton#ResetBtn:hover { background-color: #d97706; }
QPushButton#ThemeBtn { background-color: #ffffff; color: #374151; border: 1px solid #d1d5db; font-size: 14px; }
"""

# =============================================================================
# 2. GRAFİK TUVALİ (NETWORK CANVAS)
# =============================================================================
class NetworkCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        
        # --- DÜZELTME: GRAFİK KENAR BOŞLUKLARINI SIFIRLA ---
        # Bu işlem grafiğin çerçeveye tam oturmasını sağlar
        self.fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        
        super(NetworkCanvas, self).__init__(self.fig)
        self.setParent(parent)
        self.ax.axis('off') 
        self.set_theme_colors('dark')

    def set_theme_colors(self, mode):
        if mode == 'dark':
            self.bg_color = '#232330' 
            self.node_color = '#cba6f7' 
            self.edge_color = '#45475a' 
            self.glow_color = '#89b4fa' 
            self.text_color = '#ffffff' # Etiket rengi
        else:
            self.bg_color = '#ffffff' 
            self.node_color = '#3b82f6' 
            self.edge_color = '#9ca3af'
            self.glow_color = '#f97316' 
            self.text_color = '#000000'
            
        self.fig.patch.set_facecolor(self.bg_color)
        self.ax.set_facecolor(self.bg_color)
        
    def draw_network(self, G, pos, path_list=None):
        self.ax.clear()
        if not G: return

        if not path_list:
            # --- NORMAL DURUM ---
            nx.draw_networkx_nodes(G, pos, ax=self.ax, node_size=35, node_color=self.node_color, alpha=0.8)
            nx.draw_networkx_edges(G, pos, ax=self.ax, width=0.5, alpha=0.3, edge_color=self.edge_color)
        else:
            # --- ROTA MODU ---
            # Arka planı silikleştir
            nx.draw_networkx_nodes(G, pos, ax=self.ax, node_size=30, node_color='gray', alpha=0.05)
            nx.draw_networkx_edges(G, pos, ax=self.ax, width=0.5, alpha=0.02, edge_color='gray')
            
            # Rota Çizgileri
            path_edges = list(zip(path_list, path_list[1:]))
            
            # Glow Efekti (Dengeli)
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, ax=self.ax, width=6, alpha=0.15, edge_color=self.glow_color)
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, ax=self.ax, width=2, alpha=1.0, edge_color='white') # Çekirdek Beyaz
            
            # Ara Noktalar
            nx.draw_networkx_nodes(G, pos, nodelist=path_list[1:-1], ax=self.ax, node_size=180, node_color='white', edgecolors=self.glow_color, linewidths=2)
            
            # Başlangıç/Bitiş Noktaları (Daha Büyük)
            nx.draw_networkx_nodes(G, pos, nodelist=[path_list[0]], ax=self.ax, node_size=250, node_color='#00ff00', alpha=1.0, edgecolors='white', linewidths=2) 
            nx.draw_networkx_nodes(G, pos, nodelist=[path_list[-1]], ax=self.ax, node_size=250, node_color='#ff0000', alpha=1.0, edgecolors='white', linewidths=2)

            # --- YENİ ÖZELLİK: DÜĞÜM NUMARALARI ---
            # Sadece rota üzerindeki noktaların numaralarını yazalım
            labels = {node: str(node) for node in path_list}
            nx.draw_networkx_labels(G, pos, labels=labels, ax=self.ax, font_size=8, font_color='black', font_weight='bold')

        self.draw()

# =============================================================================
# 3. ANA PENCERE (MAIN WINDOW)
# =============================================================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QoS-Intelligence: Akıllı Rotalama Simülatörü")
        self.setGeometry(100, 100, 1450, 950)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DriveNetIcon))
        
        self.is_dark_mode = True
        self.current_path = None 
        
        # Header Animasyonu için
        self.hue = 0 
        self.timer_anim = QTimer()
        self.timer_anim.timeout.connect(self.animate_border)
        self.timer_anim.start(50) 
        
        self.manager = TopologyManager()
        self.G, self.pos = self.manager.create_network()

        self.init_ui()
        self.apply_theme()
        
    def load_graph_from_file(self):
        """Hocanın CSV dosyalarını sırayla yükler ve arayüzü günceller."""
        
        # 1. NODE Dosyası Seçimi
        fname_node, _ = QFileDialog.getOpenFileName(self, '1. Adım: NodeData (Düğüm) Dosyası', '.', "CSV Files (*.csv);;All Files (*)")
        if not fname_node: return

        # 2. EDGE Dosyası Seçimi
        fname_edge, _ = QFileDialog.getOpenFileName(self, '2. Adım: EdgeData (Kenar) Dosyası', '.', "CSV Files (*.csv);;All Files (*)")
        if not fname_edge: return

        # 3. Yükleme İşlemi
        G, pos, success = self.manager.build_from_csv(fname_node, fname_edge)
        
        if success:
            self.G = G
            self.pos = pos
            self.current_path = None
            
            # Comboboxları yeni düğüm sayısına göre güncelle
            self.populate_combos()
            
            # Header Bilgisini Güncelle
            node_count = len(self.G.nodes())
            edge_count = len(self.G.edges())
            self.lbl_graph_header.setText(f"VERİ YÜKLENDİ: {node_count} DÜĞÜM / {edge_count} KENAR")
            
            # Grafiği Çiz
            self.canvas.draw_network(self.G, self.pos)
            
            # Kartları Sıfırla
            self.card_delay.findChild(QLabel, "MetricValue").setText("-")
            self.card_rel.findChild(QLabel, "MetricValue").setText("-")
            self.card_res.findChild(QLabel, "MetricValue").setText("-")
        else:
            self.lbl_graph_header.setText("HATA: DOSYA OKUNAMADI!")    

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(25) # Paneller arası boşluk
        central_widget.setLayout(main_layout)
       

        # --- SOL PANEL (KONTROLLER) ---
        left_panel = QWidget()
        left_panel.setFixedWidth(350)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(20) # Kartlar arası boşluk
        left_panel.setLayout(left_layout)
        
        # 1. Header (Kontrol Paneli)
        self.header = QLabel("KONTROL PANELİ")
        self.header.setObjectName("HeaderLabel")
        self.header.setAlignment(Qt.AlignCenter)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 5)
        self.header.setGraphicsEffect(shadow)
        left_layout.addWidget(self.header)
        
        # ... (self.header kodları bittikten sonra, card_route öncesine) ...
        left_layout.addWidget(self.header)

        # --- YENİ EKLENEN: DOSYA YÜKLEME KARTI ---
        card_file = self.create_input_card("📁 Veri Kaynağı")
        layout_file = QVBoxLayout()
        layout_file.setContentsMargins(0, 5, 0, 5)
        
        self.btn_load_files = QPushButton("📂 CSV Dosyalarını Yükle")
        self.btn_load_files.setFixedHeight(40)
        self.btn_load_files.setCursor(Qt.PointingHandCursor)
        # Mevcut tasarıma uygun Mavi buton stili
        self.btn_load_files.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6; 
                color: white; 
                border: none; 
                border-radius: 6px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover { background-color: #2563eb; }
        """)
        self.btn_load_files.clicked.connect(self.load_graph_from_file)
        
        layout_file.addWidget(self.btn_load_files)
        
        # Bilgi Notu
        lbl_info = QLabel("Sırasıyla Node ve Edge dosyalarını seçiniz.")
        lbl_info.setStyleSheet("color: gray; font-size: 10px; font-style: italic;")
        lbl_info.setAlignment(Qt.AlignCenter)
        layout_file.addWidget(lbl_info)

        card_file.layout().addLayout(layout_file)
        left_layout.addWidget(card_file)
        # ---------------------------------------------

        # 2. Rota Seçimi KARTI (Buradan kodun devam ediyor...)
        card_route = self.create_input_card("📍 Rota ve Hedef Seçimi")
        

        # 2. Rota Seçimi KARTI (İç boşluk azaltıldı)
        card_route = self.create_input_card("📍 Rota ve Hedef Seçimi")
        layout_route = QFormLayout()
        layout_route.setSpacing(8) # Inputlar arası boşluk azaltıldı
        layout_route.setContentsMargins(0,0,0,0) # Ekstra kenar boşlukları alındı
        
        # --- YENİLİK: Editable (Yazılabilir) Combobox ve Validator ---
        self.combo_source = QComboBox()
        self.combo_source.setEditable(True) # Yazılabilir
        self.combo_source.setValidator(QIntValidator(0, 249)) # Sadece 0-249 arası sayı
        
        self.combo_target = QComboBox()
        self.combo_target.setEditable(True)
        self.combo_target.setValidator(QIntValidator(0, 249))
        
        self.populate_combos()
        layout_route.addRow("Kaynak (S):", self.combo_source)
        layout_route.addRow("Hedef (D):", self.combo_target)
        card_route.layout().addLayout(layout_route)
        left_layout.addWidget(card_route)

        # 3. QoS Ağırlıkları (İç boşluk azaltıldı)
        card_qos = self.create_input_card("⚖️ QoS Ağırlık Dağılımı")
        layout_qos = QVBoxLayout()
        layout_qos.setSpacing(8) 
        layout_qos.setContentsMargins(0,0,0,0)
        
        self.lbl_delay = QLabel("Gecikme (Hız): %33")
        self.slider_delay = QSlider(Qt.Horizontal)
        self.slider_delay.setRange(0, 100)
        self.slider_delay.setValue(33)
        self.slider_delay.valueChanged.connect(self.update_ui_labels)
        
        self.lbl_rel = QLabel("Güvenilirlik (Sağlamlık): %33")
        self.slider_rel = QSlider(Qt.Horizontal)
        self.slider_rel.setRange(0, 100)
        self.slider_rel.setValue(33)
        self.slider_rel.valueChanged.connect(self.update_ui_labels)

        self.lbl_res = QLabel("Kaynak (Maliyet): %34")
        self.slider_res = QSlider(Qt.Horizontal)
        self.slider_res.setRange(0, 100)
        self.slider_res.setValue(34)
        self.slider_res.valueChanged.connect(self.update_ui_labels)

        layout_qos.addWidget(self.lbl_delay)
        layout_qos.addWidget(self.slider_delay)
        layout_qos.addWidget(self.lbl_rel)
        layout_qos.addWidget(self.slider_rel)
        layout_qos.addWidget(self.lbl_res)
        layout_qos.addWidget(self.slider_res)
        card_qos.layout().addLayout(layout_qos)
        left_layout.addWidget(card_qos)

        # 4. Butonlar (Daha Büyük)
        self.btn_calc = QPushButton("▶ ROTA HESAPLA")
        self.btn_calc.setObjectName("CalcBtn")
        self.btn_calc.setFixedHeight(50)
        self.btn_calc.setCursor(Qt.PointingHandCursor)
        self.btn_calc.clicked.connect(self.on_calculate_click)
        left_layout.addWidget(self.btn_calc)

        self.btn_reset = QPushButton("↺ SİSTEMİ SIFIRLA")
        self.btn_reset.setObjectName("ResetBtn")
        self.btn_reset.setFixedHeight(45)
        self.btn_reset.setCursor(Qt.PointingHandCursor)
        self.btn_reset.clicked.connect(self.reset_application)
        left_layout.addWidget(self.btn_reset)
        
        # 5. Mod Butonu (BÜYÜTÜLDÜ)
        self.btn_theme = QPushButton("Mod: Karanlık 🌙")
        self.btn_theme.setObjectName("ThemeBtn")
        self.btn_theme.setFixedHeight(45) # Yükseklik artırıldı
        self.btn_theme.setCursor(Qt.PointingHandCursor)
        self.btn_theme.clicked.connect(self.toggle_theme)
        left_layout.addWidget(self.btn_theme)
        
        # Sol alttaki boşluğu doldurması için stretch
        left_layout.addStretch()

        lbl_sign = QLabel("Interface Designed by Yusuf MEYDAN")
        lbl_sign.setAlignment(Qt.AlignCenter)
        lbl_sign.setStyleSheet("color: gray; font-size: 10px;")
        left_layout.addWidget(lbl_sign)
        
        main_layout.addWidget(left_panel)

        # --- SAĞ PANEL ---
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setSpacing(15) # Dikey boşluk
        right_panel.setLayout(right_layout)

        # Grafik Başlığı (HEADER İLE EŞİTLENDİ)
        self.lbl_graph_header = QLabel("AĞ TOPOLOJİSİ - BEKLEMEDE")
        self.lbl_graph_header.setObjectName("GraphHeader")
        self.lbl_graph_header.setAlignment(Qt.AlignCenter)
        # Buna da aynı gölgeyi verelim
        shadow_g = QGraphicsDropShadowEffect()
        shadow_g.setBlurRadius(20)
        shadow_g.setOffset(0, 5)
        self.lbl_graph_header.setGraphicsEffect(shadow_g)
        right_layout.addWidget(self.lbl_graph_header)

        # Grafik Çerçevesi
        graph_container = QFrame()
        graph_container.setObjectName("GraphContainer")
        graph_layout = QVBoxLayout()
        # --- DÜZELTME: GRAFİK ÇERÇEVESİ İÇ BOŞLUĞU SIFIRLANDI ---
        graph_layout.setContentsMargins(0, 0, 0, 0)
        graph_layout.setSpacing(0)
        graph_container.setLayout(graph_layout)
        
        self.canvas = NetworkCanvas(self, width=5, height=4, dpi=100)
        graph_layout.addWidget(self.canvas)
        
        right_layout.addWidget(graph_container, stretch=5) # Strech artırıldı

        # Dashboard Alanı (BÜYÜTÜLDÜ)
        dashboard_widget = QWidget()
        dashboard_widget.setFixedHeight(120) # Yükseklik 100 -> 120
        self.dash_layout = QHBoxLayout()
        self.dash_layout.setContentsMargins(0, 0, 0, 0)
        self.dash_layout.setSpacing(20)
        dashboard_widget.setLayout(self.dash_layout)
        
        self.card_delay = self.create_metric_card("⏱️ GECİKME", "-", "#ff6b6b")
        self.card_rel = self.create_metric_card("🛡️ GÜVENİLİRLİK", "-", "#1dd1a1")
        self.card_res = self.create_metric_card("💰 MALİYET", "-", "#feca57")
        
        self.dash_layout.addWidget(self.card_delay)
        self.dash_layout.addWidget(self.card_rel)
        self.dash_layout.addWidget(self.card_res)
        
        right_layout.addWidget(dashboard_widget, stretch=1)

        main_layout.addWidget(right_panel)
        
        self.canvas.draw_network(self.G, self.pos, path_list=self.current_path)

    # --- YARDIMCI FONKSİYONLAR ---
    def animate_border(self):
        self.hue = (self.hue + 5) % 360
        color = QColor.fromHsl(self.hue, 200, 150)
        rgb = color.name()
        
        # Sadece border-color'ı değiştir
        base_style = self.header.styleSheet() # Mevcut stili alamayız, tekrar tanımlamalıyız.
        
        # Temaya göre baz stil
        bg = "#313244" if self.is_dark_mode else "#ffffff"
        fg = "#ffffff" if self.is_dark_mode else "#111827"
        
        new_style = f"""
            QLabel#HeaderLabel {{
                background-color: {bg}; color: {fg};
                border-radius: 6px; padding: 12px; font-size: 16px; font-weight: bold; 
                border: 3px solid {rgb};
            }}
        """
        self.header.setStyleSheet(new_style)

    def create_input_card(self, title):
        card = QFrame()
        card.setObjectName("PanelCard")
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 12, 10, 12) # Daha sıkı boşluklar
        lbl_title = QLabel(title)
        lbl_title.setObjectName("PanelTitle")
        layout.addWidget(lbl_title)
        card.setLayout(layout)
        return card

    def create_metric_card(self, title, value, accent_color):
        card = QFrame()
        card.setObjectName("MetricCard")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 3)
        shadow.setColor(QColor(0, 0, 0, 40))
        card.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        lbl_title = QLabel(title)
        lbl_title.setObjectName("MetricTitle")
        lbl_title.setAlignment(Qt.AlignCenter)
        
        lbl_value = QLabel(value)
        lbl_value.setObjectName("MetricValue")
        lbl_value.setAlignment(Qt.AlignCenter)
        
        line = QFrame()
        line.setFixedWidth(50)
        line.setFixedHeight(4)
        line.setStyleSheet(f"background-color: {accent_color}; border: none; border-radius: 2px;")
        
        layout.addWidget(lbl_title)
        layout.addWidget(lbl_value)
        layout.addWidget(line, 0, Qt.AlignCenter)
        card.setLayout(layout)
        return card

    def highlight_cards(self):
        if self.is_dark_mode:
            flash_style = "QFrame#MetricCard { background-color: #45475a; border: 2px solid #b4befe; }"
        else:
            flash_style = "QFrame#MetricCard { background-color: #d1d5db; border: 2px solid #6b7280; }"
        self.card_delay.setStyleSheet(flash_style)
        self.card_rel.setStyleSheet(flash_style)
        self.card_res.setStyleSheet(flash_style)
        QTimer.singleShot(250, lambda: self.apply_theme_to_cards())

    def apply_theme_to_cards(self):
        self.card_delay.setStyleSheet("")
        self.card_rel.setStyleSheet("")
        self.card_res.setStyleSheet("")

    def populate_combos(self):
        nodes = [str(i) for i in range(250)]
        self.combo_source.clear()
        self.combo_target.clear()
        self.combo_source.addItems(nodes)
        self.combo_target.addItems(nodes)
        self.combo_target.setCurrentIndex(249)

    def update_ui_labels(self):
        self.lbl_delay.setText(f"Gecikme (Hız): %{self.slider_delay.value()}")
        self.lbl_rel.setText(f"Güvenilirlik (Sağlamlık): %{self.slider_rel.value()}")
        self.lbl_res.setText(f"Kaynak (Maliyet): %{self.slider_res.value()}")

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
        
    def apply_theme(self):
        if self.is_dark_mode:
            self.setStyleSheet(DARK_THEME)
            self.canvas.set_theme_colors('dark')
            self.btn_theme.setText("Mod: Karanlık 🌙")
        else:
            self.setStyleSheet(LIGHT_THEME)
            self.canvas.set_theme_colors('light')
            self.btn_theme.setText("Mod: Aydınlık ☀️")
        
        # Sağ Header'ın stilini güncelle (aktiflik durumunu koru)
        is_active = "true" if self.current_path else "false"
        self.lbl_graph_header.setProperty("active", is_active)
        self.lbl_graph_header.style().unpolish(self.lbl_graph_header)
        self.lbl_graph_header.style().polish(self.lbl_graph_header)
        
        self.canvas.draw_network(self.G, self.pos, path_list=self.current_path)

    def reset_application(self):
        self.slider_delay.setValue(33)
        self.slider_rel.setValue(33)
        self.slider_res.setValue(34)
        self.current_path = None 
        self.card_delay.findChild(QLabel, "MetricValue").setText("-")
        self.card_rel.findChild(QLabel, "MetricValue").setText("-")
        self.card_res.findChild(QLabel, "MetricValue").setText("-")
        
        self.lbl_graph_header.setText("AĞ TOPOLOJİSİ - SIFIRLANDI")
        self.lbl_graph_header.setProperty("active", "false")
        self.lbl_graph_header.style().unpolish(self.lbl_graph_header)
        self.lbl_graph_header.style().polish(self.lbl_graph_header)
        
        self.G, self.pos = self.manager.create_network()
        self.canvas.draw_network(self.G, self.pos)

    def on_calculate_click(self):
        try:
            s = int(self.combo_source.currentText())
            t = int(self.combo_target.currentText())
        except ValueError:
             self.lbl_graph_header.setText("HATA: GEÇERSİZ GİRİŞ!")
             return

        w_d = self.slider_delay.value() / 100.0
        w_r = self.slider_rel.value() / 100.0
        w_res = self.slider_res.value() / 100.0

        result = self.manager.calculate_path(s, t, w_d, w_r, w_res)

        if result:
            self.current_path = result["path"]
            self.card_delay.findChild(QLabel, "MetricValue").setText(f"{result['total_delay']:.2f} ms")
            self.card_rel.findChild(QLabel, "MetricValue").setText(f"%{result['final_reliability']:.4f}")
            self.card_res.findChild(QLabel, "MetricValue").setText(f"{result['resource_cost']:.2f}")
            self.highlight_cards()
            
            self.lbl_graph_header.setText(f"ROTA HESAPLANDI: DÜĞÜM {s} ➝ DÜĞÜM {t}")
            self.lbl_graph_header.setProperty("active", "true")
            self.lbl_graph_header.style().unpolish(self.lbl_graph_header)
            self.lbl_graph_header.style().polish(self.lbl_graph_header)
            
            self.canvas.draw_network(self.G, self.pos, path_list=self.current_path)
        else:
            self.lbl_graph_header.setText("HATA: UYGUN YOL BULUNAMADI!")
            self.canvas.draw()
            
            
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())