from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QObject, pyqtSignal
from cagri_ekrani import Ui_widget
from kayitcek import gsm_kayitcek, normalize_gsm
from Guncelleme import GuncellePage
from arama_gor_ekrani import AramaPage
from kayit_ekrani import kayitPage
import sys

pencere6 = GuncellePage()
pencere11 = AramaPage()
pencere3 = kayitPage()

class CagriPenceresi(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.cagri = Ui_widget()
        self.cagri.setupUi(self)
        ui = self.cagri
        self.numara = "0"
        self.idf = "0"
        
        print("Global: ",self.idf)
    
    def veriyi_goster(self, veri: dict):
        numara_raw = veri.get('phone') or veri.get('phoneNumber') or "Numara yok"
        numara = normalize_gsm(numara_raw)
        self.numara = numara
        cagri = veri.get('callType')
        yid =gsm_kayitcek("id", "kisiler", numara)
        self.idf = yid
        print("Alıcı: ",yid)
        self.cagri.btn_ekle.clicked.connect(self.arama)

        saat = veri.get('time') or veri.get('timestamp') or "Saat yok"
        ad = gsm_kayitcek("ad", "kisiler", numara)

        self.cagri.lbl_gsm.setText(numara_raw)  # Kullanıcıya orijinal formatı göster
        self.cagri.lbl_tarih.setText(saat)
        self.cagri.lbl_ad.setText(str(ad))
        if cagri == "outgoing":
            self.cagri.lbl_tur.setText(str("Giden Çağrı"))
        else:
            self.cagri.lbl_tur.setText(str("Gelen Çağrı"))
            
        if str(ad) == "0":
            self.cagri.btn_gor.clicked.connect(self.dkayitac)
            self.cagri.btn_gor.setText("Yeni Kayıt")
            self.cagri.btn_ekle.setEnabled(False)
            self.cagri.lbl_ad.setText("Bilinmiyor")
        else:
            self.cagri.btn_gor.clicked.connect(self.guncelle)
        
    def guncelle(self):
        pencere6.idbul(self.idf)
        print("Fonksiyon: ",self.idf)
        pencere6.setFixedSize(785, 517)
        pencere6.show()
        
    def arama(self):
        pencere11.idbul(self.idf)
        pencere11.setFixedSize(785, 517)
        pencere11.show()
    
    def dkayitac(self,numara):
        pencere3.numara_ver(self.numara)
        pencere3.setFixedSize(801, 517)
        pencere3.show()    

        



    def closeEvent(self, event):
        print("Pencere kapatıldı, listener durdurulmalı!")
        # Buraya listener'ı durduracak kodu ekle
        event.accept()
