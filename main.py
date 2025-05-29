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
from PyQt6.QtWidgets import QMessageBox, QPushButton
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


baglanti = sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

class MainPage(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.main.statusbar.setPalette(palette)
        
        pixmap = QPixmap('assets/mba4.png')
        self.main.logo.setPixmap(pixmap)
        self.main.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
        
        self.kayit_listele()
        self.boya()
        
        islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
        for row in islem.fetchall():
            self.main.lnesecders.addItem(row[0])
        self.main.lnesecders.setCurrentIndex(-1)
        self.aktif_pencereler = []
        
        self.main.lnearaad.returnPressed.connect(self.kategoriye_gore_listele)
        self.main.lnesecdurum.currentTextChanged.connect(self.kategoriye_gore_listele)
        self.main.lnesecders.currentTextChanged.connect(self.kategoriye_gore_listele)
        self.main.lnearagsm.returnPressed.connect(self.kategoriye_gore_listele)
        self.main.lnearaid.returnPressed.connect(self.kategoriye_gore_listele)
        self.main.lnearanot.returnPressed.connect(self.kategoriye_gore_listele)
        self.main.lnearatarih.returnPressed.connect(self.kategoriye_gore_listele)
        self.main.lnearameslek.returnPressed.connect(self.kategoriye_gore_listele)
        self.main.btnekle.clicked.connect(self.dkayitac)
        self.main.btnlistele.clicked.connect(self.guncelle)
        self.main.btnara.clicked.connect(self.kategoriye_gore_listele)
        self.main.btnsil.clicked.connect(self.kayit_sil)
        self.main.actionDetayl_Kay_t.triggered.connect(self.dkayitac)
        self.main.actionFiyat.triggered.connect(self.fguncelle)
        self.main.actionDers.triggered.connect(self.dersekle)
        self.main.save_exc.triggered.connect(self.ex_kayit)
        self.main.actionHesap_Makinesi.triggered.connect(self.hmac)
        self.main.btndersekle.clicked.connect(self.dersekle)
        self.main.btnfiyatg.clicked.connect(self.fguncelle)
        self.main.btnindirim.clicked.connect(self.indirim_page)
        self.main.sutun_btn.clicked.connect(self.kayit_listele)
        self.main.lnearaad.textChanged.connect(self.kategoriye_gore_listele)
        self.main.lnearagsm.textChanged.connect(self.kategoriye_gore_listele)
        self.main.lnearanot.textChanged.connect(self.kategoriye_gore_listele)
        self.main.lnearatarih.textChanged.connect(self.kategoriye_gore_listele)
        self.main.lnearaid.textChanged.connect(self.kategoriye_gore_listele)
        self.main.lnearameslek.textChanged.connect(self.kategoriye_gore_listele)
        
        self.main.tbllistele.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.main.tbllistele.customContextMenuRequested.connect(self.showContextMenu)
        
    def change_cell_color(self,table_widget, row, column, color):
        item = table_widget.item(row, column)
        if item is not None:
            item.setBackground(color)
            
    def change_cell_text_color(self,table_widget, row, column, color):
        item = table_widget.item(row, column)
        if item is not None:
            item.setForeground(color)
    
    def odeme_gunu_gelenler(self):
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
    
    def odeme_gunu_gecenler(self):
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
    
    def boya(self):
        gelenler = self.odeme_gunu_gelenler()
        gecenler = self.odeme_gunu_gecenler()
        for row in range(self.main.tbllistele.rowCount()):
            for col in range(self.main.tbllistele.columnCount()):
                item = self.main.tbllistele.item(row, col)
                if item is not None:
                    if item.text() == "Görüşme":
                        self.change_cell_color(self.main.tbllistele, row, col, QColor(255, 165, 0))
                        self.change_cell_text_color(self.main.tbllistele, row, col, QColor(255, 255, 255))
                    elif item.text() == "Kayıt":
                        self.change_cell_color(self.main.tbllistele, row, col, QColor(0, 255, 0))
                        self.change_cell_text_color(self.main.tbllistele, row, col, QColor(0, 0, 0))
                    elif item.text() in [str(g) for g in gelenler]:
                        self.change_cell_color(self.main.tbllistele, row, col, QColor(255, 0, 0))
                        self.change_cell_text_color(self.main.tbllistele, row, col, QColor(255, 255, 255))
                    elif item.text() in [str(g) for g in gecenler]:
                        self.change_cell_color(self.main.tbllistele, row, col, QColor(139, 0, 0))
                        self.change_cell_text_color(self.main.tbllistele, row, col, QColor(255, 255, 255))

    def kayit_listele(self):
        self.main.tbllistele.clearContents()
        self.main.tbllistele.setRowCount(0)
        self.main.tbllistele.setColumnCount(8)
        self.main.tbllistele.setHorizontalHeaderLabels(("Ad", "Tarih", "GSM", "Durum", "Ek Not", "Meslek", "Ders", "ID"))

        sorgu = "SELECT * FROM kisiler ORDER BY id DESC"
        islem.execute(sorgu)
        veriler = islem.fetchall()

        self.main.tbllistele.setRowCount(len(veriler))
        for indexSatir, kayitNumarasi in enumerate(veriler):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.main.tbllistele.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

        self.main.lnearaad.clear()
        self.main.lnesecdurum.setCurrentIndex(-1)
        self.main.lnesecders.setCurrentIndex(-1)
        self.main.lnearagsm.clear()
        self.main.lnearaid.clear()
        self.main.lnearanot.clear()
        self.main.lnearatarih.clear()
        self.main.lnearameslek.clear()
        self.boya()
        
    def kategoriye_gore_listele(self):
        arama_kriterleri = []
        sorgu_kosulları = []
        parametreler = []

        if self.main.lnearaad.text():
            arama_kriterleri.append(("ad", self.main.lnearaad.text()))
        if self.main.lnearatarih.text():
            arama_kriterleri.append(("tarih", self.main.lnearatarih.text()))
        if self.main.lnearagsm.text():
            arama_kriterleri.append(("gsm", self.main.lnearagsm.text()))
        if self.main.lnesecdurum.currentIndex() != -1 and self.main.lnesecdurum.currentText() != "Hepsi":
            arama_kriterleri.append(("bolum", self.main.lnesecdurum.currentText()))
        if self.main.lnearanot.text():
            arama_kriterleri.append(("eknot", self.main.lnearanot.text()))
        if self.main.lnearameslek.text():
            arama_kriterleri.append(("unvan", self.main.lnearameslek.text()))
        if self.main.lnesecders.currentIndex() != -1 and self.main.lnesecders.currentText() != "Hepsi":
            arama_kriterleri.append(("ders", self.main.lnesecders.currentText()))
        if self.main.lnearaid.text():
            arama_kriterleri.append(("ad", self.main.lnearaid.text()))

        
        if arama_kriterleri:
            sorgu = "SELECT * FROM kisiler WHERE "
            
            
            for kriter, deger in arama_kriterleri:
                sorgu_kosulları.append(f"{kriter} LIKE ?")
                parametreler.append(f"%{deger}%")
            
            
            sorgu += " AND ".join(sorgu_kosulları)
            sorgu += " ORDER BY id DESC"

            
            try:
                islem.execute(sorgu, parametreler)
                veriler = islem.fetchall()

                
                self.main.tbllistele.clearContents()
                self.main.tbllistele.setRowCount(len(veriler))
                for indexSatir, kayitNumarasi in enumerate(veriler):
                    for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                        self.main.tbllistele.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
            except sqlite3.OperationalError as e:
                print(f"Hata: {e}")
            self.boya()
        else:
            self.main.tbllistele.clear()
            self.kayit_listele()
    
    def kayit_sil(self):
        msg = QMessageBox(pencere)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle("Silme Onayı")
        msg.setText("Bu kayıt silinsin mi?")

        evet_buton = msg.addButton("Evet", QMessageBox.ButtonRole.YesRole)
        hayir_buton = msg.addButton("Hayır", QMessageBox.ButtonRole.NoRole)

        msg.exec()

        if msg.clickedButton() == evet_buton:
            try:
                secilen_kayit = self.main.tbllistele.selectedItems()
                if not secilen_kayit:
                    self.main.statusbar.showMessage("Herhangi bir kayıt seçmediniz.", 4000)
                    return
                
                silinecek_kayit = secilen_kayit[7].text()

                sorgu1 = "DELETE FROM kisiler WHERE id = ?"
                sorgu2 = "DELETE FROM detay WHERE ID = ?"

                islem.execute(sorgu1, (silinecek_kayit,))
                islem.execute(sorgu2, (silinecek_kayit,))
                baglanti.commit()

                self.main.statusbar.showMessage("Kayıt başarıyla silindi.", 5000)
                self.kayit_listele()

            except Exception as eror:
                self.main.statusbar.showMessage("Kayıt silinirken bir hata oluştu.", 4000)
                print(eror)
        else:
            self.main.statusbar.showMessage("Silme işlemi iptal edildi.", 2000)
    
    
    
    def yeni_cagri_geldi(self,cagri_verisi):
        pencere = CagriPenceresi()
        pencere.veriyi_goster(cagri_verisi)
        pencere.setFixedSize(512, 145)
        pencere.show()
        self.aktif_pencereler.append(pencere)
        
    def ex_kayit(self):
        try:
            excel()
            QMessageBox.information(pencere,"Dosya Kayıt Oldu","Kaydetiğiniz dosyayı Masaüstünde 'Excel' klasörü içerisinde bulabilirsiniz.")
        except:
            self.main.statusbar.showMessage("Excel dosyası kayıt edilirken bir hata oluştu.",2000)
    def dkayitac(self):
        pencere3.setFixedSize(801, 517)
        pencere3.show()
        
    def fguncelle(self):
        pencere4.setFixedSize(399, 299)
        pencere4.show()

    def dersekle(self):
        pencere5.setFixedSize(779, 360)
        pencere5.show()
        
    
    def idbul(self):
        try:
            current_row = self.main.tbllistele.currentRow()
            if current_row == -1:
                raise Exception("Herhangi bir satır seçilmedi.")

            item = self.main.tbllistele.item(current_row, 7)  # ID sütunu
            if item is None:
                raise Exception("Seçilen satırda ID bilgisi yok.")
            
            return item.text()
        except Exception as e:
            self.main.statusbar.showMessage(f"Kayıt seçimi hatalı: {e}", 4000)
            return None


                
        
        
    def kayitcek(self,sutun, tablo):
        idf = self.idbul()
        sorgu = "select {} from {} where id = ?".format(sutun, tablo)
        islem.execute(sorgu, (idf,))
        cikti = islem.fetchone()
        if cikti:
            return cikti[0]  
        else:
            return "Yok"
        
    def hmac(self):
        Hesap.show(self)
        
    def guncelle(self):
        yid = self.idbul()
        
        if yid == None:
            self.main.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
        else:
            pencere6.idbul(yid)
            pencere6.setFixedSize(785, 517)
            pencere6.show()
            

    def odeme(self):
        
        baglanti = sqlite3.connect('database.db')
        islem = baglanti.cursor()
        yid = self.idbul()
        try:
            islem.execute("insert into tutucu (id) values({})".format(yid))
        except Exception as eror:
            self.main.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
        baglanti.commit()
        baglanti.close()
        if yid == None:
            pass
        else:
            pencere8.setFixedSize(201, 331)
            pencere8.show()
            
    def taksit(self):
        
        baglanti = sqlite3.connect('database.db')
        islem = baglanti.cursor()
        yid = self.idbul()
        try:
            islem.execute("insert into tutucu (id) values({})".format(yid))
        except Exception as eror:
            self.main.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
        baglanti.commit()
        baglanti.close()
        if yid == None:
            pass
        else:
            pencere9.setFixedSize(411, 517)
            pencere9.show()
            
    def taksitg(self):
        
        baglanti = sqlite3.connect('database.db')
        islem = baglanti.cursor()
        yid = self.idbul()
        try:
            islem.execute("insert into tutucu (id) values({})".format(yid))
        except Exception as eror:
            self.main.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
        baglanti.commit()
        baglanti.close()
        if yid == None:
            pass
        else:
            pencere10.setFixedSize(201,331)
            pencere10.show()

    def arama(self):
        yid = self.idbul()
        
        if yid == None:
            self.main.statusbar.showMessage("Herhangi Bir Kayıt Seçmediniz",4000)
        else:
            pencere11.idbul(yid)
            pencere11.setFixedSize(785, 517)
            pencere11.show()
        
        
    def indirim_page(self):
        pencere7.setFixedSize(283, 326)
        pencere7.show()
    
    contextMenu = QMenu()
    mouse_position = QCursor.pos()  
    action = contextMenu.exec(mouse_position)
    
    def showContextMenu(self,pos):
        globalPos = self.main.tbllistele.mapToGlobal(pos)
        contextMenu = QMenu(self.main.tbllistele)

        
        palette = self.main.tbllistele.palette()
        bg_color = palette.color(QPalette.ColorRole.Base)
        is_light_theme = bg_color.lightness() > 128  

        
        icon_path_prefix = "icons_light/" if is_light_theme else "icons_dark/"

        
        action1 = QAction(QIcon(icon_path_prefix + "delete.png"), "Kaydı Sil", self.main.tbllistele)
        action2 = QAction(QIcon(icon_path_prefix + "add.png"), "Yeni Kayıt Ekle", self.main.tbllistele)
        action4 = QAction(QIcon(icon_path_prefix + "edit.png"), "Görüntüle ve Güncelle", self.main.tbllistele)
        action5 = QAction(QIcon(icon_path_prefix + "refresh.png"), "Yenile", self.main.tbllistele)
        action6 = QAction(QIcon(icon_path_prefix + "payment.png"), "Ödeme Ekle", self.main.tbllistele)
        action7 = QAction(QIcon(icon_path_prefix + "payment.png"), "Taksit Ekle", self.main.tbllistele)
        action8 = QAction(QIcon(icon_path_prefix + "payment.png"), "Taksitleri Görüntüle", self.main.tbllistele)
        action9 = QAction(QIcon(icon_path_prefix + "calling.png"), "Aramaları Görüntüle", self.main.tbllistele)

        
        contextMenu.addAction(action1)
        contextMenu.addAction(action2)
        contextMenu.addAction(action4)
        contextMenu.addAction(action5)
        contextMenu.addAction(action6)
        contextMenu.addAction(action7)
        contextMenu.addAction(action8)
        contextMenu.addAction(action9)

        
        action1.triggered.connect(self.kayit_sil)
        action2.triggered.connect(self.dkayitac)
        action4.triggered.connect(self.guncelle)
        action5.triggered.connect(self.kayit_listele)
        action6.triggered.connect(self.odeme)
        action7.triggered.connect(self.taksit)
        action8.triggered.connect(self.taksitg)
        action9.triggered.connect(self.arama)

        
        contextMenu.exec(globalPos)
    
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
    main_page = MainPage()
    listener_thread.yeni_cagri_signal.connect(main_page.yeni_cagri_geldi)
    listener_thread.start()

main_widget = MainPage()
splash = MovieSplashScreen("assets/mba3.png")
splash.show()

QtCore.QTimer.singleShot(3500, splash.close)
time.sleep(3)
main_widget.showMaximized()  # BU SATIR KRİTİK!
sys.exit(uygulama.exec())


