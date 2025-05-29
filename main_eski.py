import sys
import time
import sqlite3
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from taksit_goruntuleme_sayfasi import *
from User_Interface_max import *
from kayit_ekrani import *
from Fiyat_Belirleme import *
from Ders_Guncelle import *
from taksit_ekleme_sayfasi import *
from Guncelleme import *
from indirim_ekrani import *
from odeme_ekrani import *
from db_to_xlsx import *
from HesapM import *
from splash import *
from sifre_giris import Ui_Form
from arama_gor_ekrani import *
from datetime import datetime
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPalette, QColor
from dotenv import load_dotenv
from cagri_dinleyici import FirebaseListener
from CagriDetayPenceresi import *


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
pencere3 = kayitPage()
pencere4 = FiyatPage()
pencere5 = DersPage()
pencere6 = GuncellePage()
pencere7 = IndirimPage()
pencere8 = OdemePage()
pencere9 = TaksitPage()
pencere10 = TaksitgPage()
pencere11 = AramaPage()
pencere12 = CagriPenceresi()
Hesap = Example()
ui = Ui_MainWindow()
ui.setupUi(pencere)

splash = MovieSplashScreen("assets/mba3.png")
splash.show()

QtCore.QTimer.singleShot(3500, splash.close)
time.sleep(3)

pencere.showMaximized()

ui.sutun_btn

palette = QPalette()
palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
ui.statusbar.setPalette(palette)
date_today = QDate.currentDate()

# Veritabanı İşlemleri
baglanti = sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

islem.execute("""CREATE TABLE IF NOT EXISTS kisiler (
    ad TEXT, tarih TEXT, gsm TEXT, bolum TEXT, eknot TEXT, 
    unvan TEXT, ders TEXT, id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT)""")
baglanti.commit()

pixmap = QPixmap('assets/mba4.png')
ui.logo.setPixmap(pixmap)
ui.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
for row in islem.fetchall():
    ui.lnesecders.addItem(row[0])
ui.lnesecders.setCurrentIndex(-1)

def change_cell_color(table_widget, row, column, color):
    item = table_widget.item(row, column)
    if item is not None:
        item.setBackground(color)

def change_cell_text_color(table_widget, row, column, color):
    item = table_widget.item(row, column)
    if item is not None:
        item.setForeground(color)

def odeme_gunu_gelenler():
    bugun = datetime.now().strftime('%Y-%m-%d')
    baglanti = sqlite3.connect("database.db")
    islem = baglanti.cursor()
    islem.execute("""
        SELECT musteri_id FROM taksit_odeme_tarih
        WHERE son_odeme = ?
    """, (bugun,))
    sonuclar = [row[0] for row in islem.fetchall()]
    baglanti.close()
    return sonuclar

def odeme_gunu_gecenler():
    bugun = datetime.now().strftime('%Y-%m-%d')
    baglanti = sqlite3.connect("database.db")
    islem = baglanti.cursor()
    islem.execute("""
        SELECT musteri_id FROM taksit_odeme_tarih
        WHERE son_odeme < ?
    """, (bugun,))
    sonuclar = [row[0] for row in islem.fetchall()]
    baglanti.close()
    return sonuclar

def boya():
    gelenler = odeme_gunu_gelenler()
    gecenler = odeme_gunu_gecenler()
    for row in range(ui.tbllistele.rowCount()):
        for col in range(ui.tbllistele.columnCount()):
            item = ui.tbllistele.item(row, col)
            if item is not None:
                if item.text() == "Görüşme":
                    change_cell_color(ui.tbllistele, row, col, QColor(255, 165, 0))
                    change_cell_text_color(ui.tbllistele, row, col, QColor(255, 255, 255))
                elif item.text() == "Kayıt":
                    change_cell_color(ui.tbllistele, row, col, QColor(0, 255, 0))
                    change_cell_text_color(ui.tbllistele, row, col, QColor(0, 0, 0))
                elif item.text() in [str(g) for g in gelenler]:
                    change_cell_color(ui.tbllistele, row, col, QColor(255, 0, 0))
                    change_cell_text_color(ui.tbllistele, row, col, QColor(255, 255, 255))
                elif item.text() in [str(g) for g in gecenler]:
                    change_cell_color(ui.tbllistele, row, col, QColor(139, 0, 0))
                    change_cell_text_color(ui.tbllistele, row, col, QColor(255, 255, 255))

def kayit_listele():
    ui.tbllistele.clearContents()
    ui.tbllistele.setRowCount(0)
    ui.tbllistele.setColumnCount(8)
    ui.tbllistele.setHorizontalHeaderLabels(("Ad", "Tarih", "GSM", "Durum", "Ek Not", "Meslek", "Ders", "ID"))

    sorgu = "SELECT * FROM kisiler ORDER BY id DESC"
    islem.execute(sorgu)
    veriler = islem.fetchall()

    ui.tbllistele.setRowCount(len(veriler))
    for indexSatir, kayitNumarasi in enumerate(veriler):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tbllistele.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    ui.lnearaad.clear()
    ui.lnesecdurum.setCurrentIndex(-1)
    ui.lnesecders.setCurrentIndex(-1)
    ui.lnearagsm.clear()
    ui.lnearaid.clear()
    ui.lnearanot.clear()
    ui.lnearatarih.clear()
    ui.lnearameslek.clear()
    boya()
                
kayit_listele()
boya()
            
def kategoriye_gore_listele():
    arama_kriterleri = []
    sorgu_koşulları = []
    parametreler = []

    if ui.lnearaad.text():
        arama_kriterleri.append(("ad", ui.lnearaad.text()))
    if ui.lnearatarih.text():
        arama_kriterleri.append(("tarih", ui.lnearatarih.text()))
    if ui.lnearagsm.text():
        arama_kriterleri.append(("gsm", ui.lnearagsm.text()))
    if ui.lnesecdurum.currentIndex() != -1 and ui.lnesecdurum.currentText() != "Hepsi":
        arama_kriterleri.append(("bolum", ui.lnesecdurum.currentText()))
    if ui.lnearanot.text():
        arama_kriterleri.append(("eknot", ui.lnearanot.text()))
    if ui.lnearameslek.text():
        arama_kriterleri.append(("unvan", ui.lnearameslek.text()))
    if ui.lnesecders.currentIndex() != -1 and ui.lnesecders.currentText() != "Hepsi":
        arama_kriterleri.append(("ders", ui.lnesecders.currentText()))
    if ui.lnearaid.text():
        arama_kriterleri.append(("ad", ui.lnearaid.text()))

    # Eğer arama kriterleri varsa
    if arama_kriterleri:
        sorgu = "SELECT * FROM kisiler WHERE "
        
        # Kriterlere göre WHERE koşulunu oluşturuyoruz
        for kriter, deger in arama_kriterleri:
            sorgu_koşulları.append(f"{kriter} LIKE ?")
            parametreler.append(f"%{deger}%")
        
        # Koşulları birleştiriyoruz
        sorgu += " AND ".join(sorgu_koşulları)
        sorgu += " ORDER BY id DESC"

        # Veritabanına sorguyu gönderiyoruz
        try:
            islem.execute(sorgu, parametreler)
            veriler = islem.fetchall()

            # Tabloyu temizliyoruz ve verileri ekliyoruz
            ui.tbllistele.clearContents()
            ui.tbllistele.setRowCount(len(veriler))
            for indexSatir, kayitNumarasi in enumerate(veriler):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    ui.tbllistele.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
        except sqlite3.OperationalError as e:
            print(f"Hata: {e}")
        boya()
    else:
        ui.tbllistele.clear()
        kayit_listele()

# Arama kutularına tıklandığında arama yapılmasını sağlıyoruz
ui.lnearaad.returnPressed.connect(kategoriye_gore_listele)
ui.lnesecdurum.currentTextChanged.connect(kategoriye_gore_listele)
ui.lnesecders.currentTextChanged.connect(kategoriye_gore_listele)
ui.lnearagsm.returnPressed.connect(kategoriye_gore_listele)
ui.lnearaid.returnPressed.connect(kategoriye_gore_listele)
ui.lnearanot.returnPressed.connect(kategoriye_gore_listele)
ui.lnearatarih.returnPressed.connect(kategoriye_gore_listele)
ui.lnearameslek.returnPressed.connect(kategoriye_gore_listele)

from PyQt6.QtWidgets import QMessageBox, QPushButton

def kayit_sil():
    msg = QMessageBox(pencere)
    msg.setIcon(QMessageBox.Icon.Question)
    msg.setWindowTitle("Silme Onayı")
    msg.setText("Bu kayıt silinsin mi?")

    evet_buton = msg.addButton("Evet", QMessageBox.ButtonRole.YesRole)
    hayir_buton = msg.addButton("Hayır", QMessageBox.ButtonRole.NoRole)

    msg.exec()

    if msg.clickedButton() == evet_buton:
        try:
            secilen_kayit = ui.tbllistele.selectedItems()
            if not secilen_kayit:
                ui.statusbar.showMessage("Herhangi bir kayıt seçmediniz.", 4000)
                return
            
            silinecek_kayit = secilen_kayit[7].text()

            sorgu1 = "DELETE FROM kisiler WHERE id = ?"
            sorgu2 = "DELETE FROM detay WHERE ID = ?"

            islem.execute(sorgu1, (silinecek_kayit,))
            islem.execute(sorgu2, (silinecek_kayit,))
            baglanti.commit()

            ui.statusbar.showMessage("Kayıt başarıyla silindi.", 5000)
            kayit_listele()

        except Exception as eror:
            ui.statusbar.showMessage("Kayıt silinirken bir hata oluştu.", 4000)
            print(eror)
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi.", 2000)

aktif_pencereler = []

def yeni_cagri_geldi(cagri_verisi):
    pencere = CagriPenceresi()
    pencere.veriyi_goster(cagri_verisi)
    pencere.setFixedSize(512, 145)
    pencere.show()

    aktif_pencereler.append(pencere)



def ex_kayit():
    try:
        excel()
        QMessageBox.information(pencere,"Dosya Kayıt Oldu","Kaydetiğiniz dosyayı Masaüstünde 'Excel' klasörü içerisinde bulabilirsiniz.")
    except:
        ui.statusbar.showMessage("Excel dosyası kayıt edilirken bir hata oluştu.",2000)
def dkayitac():
    pencere3.setFixedSize(801, 517)
    pencere3.show()
    
def fguncelle():
    pencere4.setFixedSize(399, 299)
    pencere4.show()

def dersekle():
    pencere5.setFixedSize(779, 360)
    pencere5.show()
    
   
def idbul():
    try:
        secilen = ui.tbllistele.selectedItems()
        giden = secilen[7].text()
        return giden
    except Exception as eror:
        ui.statusbar.showMessage("Bir Kayıt Seçmediniz. {}".format(eror))
            
    
    
def kayitcek(sutun, tablo):
    idf = idbul()
    sorgu = "select {} from {} where id = ?".format(sutun, tablo)
    islem.execute(sorgu, (idf,))
    cikti = islem.fetchone()
    if cikti:
        return cikti[0]  
    else:
        return "Yok"
    
def hmac():
    Hesap.show()
    
def guncelle():
    yid = idbul()
    
    if yid == None:
        ui.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
    else:
        pencere6.idbul(yid)
        pencere6.setFixedSize(785, 517)
        pencere6.show()
        

def odeme():
    # Bağlantıyı aç
    baglanti = sqlite3.connect('database.db')
    islem = baglanti.cursor()
    yid = idbul()
    try:
        islem.execute("insert into tutucu (id) values({})".format(yid))
    except Exception as eror:
        ui.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
    baglanti.commit()
    baglanti.close()
    if yid == None:
        pass
    else:
        pencere8.setFixedSize(201, 331)
        pencere8.show()
        
def taksit():
    # Bağlantıyı aç
    baglanti = sqlite3.connect('database.db')
    islem = baglanti.cursor()
    yid = idbul()
    try:
        islem.execute("insert into tutucu (id) values({})".format(yid))
    except Exception as eror:
        ui.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
    baglanti.commit()
    baglanti.close()
    if yid == None:
        pass
    else:
        pencere9.setFixedSize(411, 517)
        pencere9.show()
        
def taksitg():
    # Bağlantıyı aç
    baglanti = sqlite3.connect('database.db')
    islem = baglanti.cursor()
    yid = idbul()
    try:
        islem.execute("insert into tutucu (id) values({})".format(yid))
    except Exception as eror:
        ui.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
    baglanti.commit()
    baglanti.close()
    if yid == None:
        pass
    else:
        pencere10.setFixedSize(201,331)
        pencere10.show()

def arama():
    yid = idbul()
    
    if yid == None:
        ui.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
    else:
        pencere11.idbul(yid)
        pencere11.setFixedSize(785, 517)
        pencere11.show()
    
    
def indirim_page():
    pencere7.setFixedSize(283, 326)
    pencere7.show()
    
# butonlar
ui.btnekle.clicked.connect(dkayitac)
ui.btnlistele.clicked.connect(guncelle)
ui.btnara.clicked.connect(kategoriye_gore_listele)
ui.btnsil.clicked.connect(kayit_sil)
ui.actionDetayl_Kay_t.triggered.connect(dkayitac)
ui.actionFiyat.triggered.connect(fguncelle)
ui.actionDers.triggered.connect(dersekle)
ui.save_exc.triggered.connect(ex_kayit)
ui.actionHesap_Makinesi.triggered.connect(hmac)
ui.btndersekle.clicked.connect(dersekle)
ui.btnfiyatg.clicked.connect(fguncelle)
ui.btnindirim.clicked.connect(indirim_page)
ui.sutun_btn.clicked.connect(kayit_listele)


contextMenu = QMenu()
mouse_position = QCursor.pos()  
action = contextMenu.exec(mouse_position)




def showContextMenu(pos):
    globalPos = ui.tbllistele.mapToGlobal(pos)
    contextMenu = QMenu(ui.tbllistele)

    # Tema rengine bak
    palette = ui.tbllistele.palette()
    bg_color = palette.color(QPalette.ColorRole.Base)
    is_light_theme = bg_color.lightness() > 128  # 0-255 arası: 128 üstü açıktır

    # İkona göre setle
    icon_path_prefix = "icons_light/" if is_light_theme else "icons_dark/"

    # İkonları çağır
    action1 = QAction(QIcon(icon_path_prefix + "delete.png"), "Kaydı Sil", ui.tbllistele)
    action2 = QAction(QIcon(icon_path_prefix + "add.png"), "Yeni Kayıt Ekle", ui.tbllistele)
    action4 = QAction(QIcon(icon_path_prefix + "edit.png"), "Görüntüle ve Güncelle", ui.tbllistele)
    action5 = QAction(QIcon(icon_path_prefix + "refresh.png"), "Yenile", ui.tbllistele)
    action6 = QAction(QIcon(icon_path_prefix + "payment.png"), "Ödeme Ekle", ui.tbllistele)
    action7 = QAction(QIcon(icon_path_prefix + "payment.png"), "Taksit Ekle", ui.tbllistele)
    action8 = QAction(QIcon(icon_path_prefix + "payment.png"), "Taksitleri Görüntüle", ui.tbllistele)
    action9 = QAction(QIcon(icon_path_prefix + "calling.png"), "Aramaları Görüntüle", ui.tbllistele)

    # Menüyü oluştur
    contextMenu.addAction(action1)
    contextMenu.addAction(action2)
    contextMenu.addAction(action4)
    contextMenu.addAction(action5)
    contextMenu.addAction(action6)
    contextMenu.addAction(action7)
    contextMenu.addAction(action8)
    contextMenu.addAction(action9)

    # Trigger bağlantıları
    action1.triggered.connect(kayit_sil)
    action2.triggered.connect(dkayitac)
    action4.triggered.connect(guncelle)
    action5.triggered.connect(kayit_listele)
    action6.triggered.connect(odeme)
    action7.triggered.connect(taksit)
    action8.triggered.connect(taksitg)
    action9.triggered.connect(arama)

    # Menü göster
    contextMenu.exec(globalPos)

    
ui.lnearaad.textChanged.connect(kategoriye_gore_listele)
ui.lnearagsm.textChanged.connect(kategoriye_gore_listele)
ui.lnearanot.textChanged.connect(kategoriye_gore_listele)
ui.lnearatarih.textChanged.connect(kategoriye_gore_listele)
ui.lnearaid.textChanged.connect(kategoriye_gore_listele)
ui.lnearameslek.textChanged.connect(kategoriye_gore_listele)
    

ui.tbllistele.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
ui.tbllistele.customContextMenuRequested.connect(showContextMenu)

class FirebaseListenerThread(QThread):
    yeni_cagri_signal = pyqtSignal(dict)  # Firebase'den gelen veriyi signal olarak yay

    def __init__(self, credential_path, db_url, ref_path='call_logs'):
        super().__init__()
        self.listener = FirebaseListener(credential_path, db_url, ref_path)

    def run(self):
        self.listener.start_listening(self._callback)

    def _callback(self, data):
        self.yeni_cagri_signal.emit(data)

if __name__ == "__main__":
    listener_thread = FirebaseListenerThread(
        credential_path='phonenumberdedected-firebase-adminsdk-fbsvc-155fea36cb.json',
        db_url=os.getenv('FIREBASE_DATABASE_URL')
    )
    listener_thread.yeni_cagri_signal.connect(yeni_cagri_geldi)
    listener_thread.start()


sys.exit(uygulama.exec())
baglanti.close()


