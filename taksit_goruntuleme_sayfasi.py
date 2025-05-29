import sqlite3
from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget
from taksit_goruntule import Ui_widget
from datetime import *

baglanti=sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists odemeler (kid text,ad text, tarih text,tutar text,id	integer unique,PRIMARY KEY('id' AUTOINCREMENT))")
baglanti.commit()

def idbul():
    try:
        islem.execute("SELECT id FROM tutucu ORDER BY idt DESC LIMIT 1;")
        id = islem.fetchone()
        id = id[0]
        return id
    except Exception as eror:
        print(eror)

class TaksitgPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.taksitg = Ui_widget()
        self.taksitg.setupUi(self)
        ui = self.taksitg
        ui.txt_hatamesaj.setVisible(False)
        date_today = QDate.currentDate()
        self.idler = []
        
        def temizle():
            ui.txt_ad.clear()
            ui.txt_toplam.clear()
            ui.txt_kalan.clear()
            ui.txt_hatamesaj.setVisible(False)
            ui.txt_id.clear()
            ui.txt_taksit.clear()
            ui.txt_tarih.clear()
            ui.cmb_sec.clear()
            ui.cmb_sec.setCurrentIndex(-1)

        def hatamesaj(msg,durum):
            ui.txt_hatamesaj.setVisible(True)
            ui.txt_hatamesaj.setText(msg)
            if durum == "Hata":
                ui.txt_hatamesaj.setStyleSheet("""
                                              color:red;
                                              """)
            elif durum == "Onay":
                ui.txt_hatamesaj.setStyleSheet("""
                                              color:green;
                                              """)
            elif durum == None:
                pass
            
        def kapat():
            self.close()
            
        def kayitcek(sutun, tablo):
            try:
                idf = idbul()
                sorgu = f"SELECT {sutun} FROM {tablo} WHERE id = ?"
                islem.execute(sorgu, (idf,))
                cikti = islem.fetchone()
                return str(cikti[0]) if cikti else ""
            except Exception as e:
                print("kayitcek hatası:", e)
                return ""

            
        def yazdır():
            ui.txt_ad.setText(kayitcek("ad","kisiler"))
            ui.txt_id.setText(str(idbul()))
            islem.execute("SELECT son_odeme, taksit, tutar, oran, id FROM taksit_odeme_tarih WHERE musteri_id = ?", (idbul(),))
            veriler = islem.fetchall()

            if not veriler:
                hatamesaj("Bu müşteriye ait taksit verisi bulunamadı.", "Hata")
                return
            son_odemeler = []
            taksitler = []
            tutarlar = []
            oranlar = []
            
            for son_odeme, taksit, tutar, oran, id in veriler:
                son_odemeler.append(son_odeme)
                taksitler.append(taksit)
                tutarlar.append(tutar)
                oranlar.append(oran)
                self.idler.append(id)
            
            for row in son_odemeler:
                ui.cmb_sec.addItem(row)
            
            si = ui.cmb_sec.currentIndex()
            
            ui.txt_kalan.setText(str(len(taksitler)))
            ui.txt_taksit.setText(str(tutarlar[si]))
            ui.txt_toplam.setText(str(tutarlar[si]*taksitler[si]))
            ui.cmb_sec.setCurrentIndex(0)
            ui.txt_tarih.setText(str(datetime.now().strftime("%Y-%m-%d")))
                
        def islemci(secenek):
            try:
                tarih = datetime.now().strftime("%Y-%m-%d")
                idi = self.idler[ui.cmb_sec.currentIndex()]

                if secenek == "ekle":
                    islem.execute("INSERT INTO odemeler (kid, ad, tarih, tutar) VALUES (?, ?, ?, ?)", (str(idi), ui.txt_ad.text(), str(tarih),ui.txt_taksit.text() ))
                    baglanti.commit()
                    islem.execute("DELETE FROM taksit_odeme_tarih WHERE id = ?", (idi,))
                    baglanti.commit()
                    ui.txt_hatamesaj.setVisible(False)
                elif secenek == "cikar":
                    islem.execute("DELETE FROM taksit_odeme_tarih WHERE id = ?", (idi,))
                    baglanti.commit()
                    ui.txt_hatamesaj.setVisible(False)
                
            except Exception as eror:
                print("hata islemcide:",eror)
                hatamesaj("İşlem Başarısız Oldu.","hata")
            
            kapat()
            temizle()
            islem.execute("DELETE FROM tutucu;")
            baglanti.commit()
                
            
        def ekle():
            islemci("ekle")
            
        def cikar():
            islemci("cikar")
                
        ui.btn_ekle.clicked.connect(ekle)
        ui.btn_cikar.clicked.connect(cikar)
        
    def closeEvent(self, event):
        ui = self.taksitg
        ui.txt_ad.clear()
        ui.txt_hatamesaj.setVisible(False)
        ui.txt_id.clear()
        ui.txt_tarih.clear()
        ui.cmb_sec.clear()
    
        islem.execute("DELETE FROM tutucu;")
        baglanti.commit()
    
        event.accept()  # Sayfanın kapanmasına izin verir.
        
    def showEvent(self, a0: QShowEvent) -> None:
        ui = self.taksitg
        date_today = QDate.currentDate()
        def kayitcek(sutun, tablo):
            idf = idbul()
            sorgu = "select {} from {} where id = ?".format(sutun, tablo)
            islem.execute(sorgu, (idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return 0
        
        def yazdır():
            ui.txt_ad .setText(kayitcek("ad","kisiler"))
            ui.txt_id.setText(str(idbul()))
            islem.execute("SELECT son_odeme, taksit, tutar, oran, id FROM taksit_odeme_tarih WHERE musteri_id = ?", (idbul(),))
            veriler = islem.fetchall()
            if not veriler:
                ui.txt_hatamesaj.setVisible(True)
                ui.txt_hatamesaj.setText("Bu müşteriye ait taksit verisi bulunamadı.")
                return
            son_odemeler = []
            taksitler = []
            tutarlar = []
            oranlar = []
            
            self.idler.clear()
            for son_odeme, taksit, tutar, oran, id in veriler:
                son_odemeler.append(son_odeme)
                taksitler.append(taksit)
                tutarlar.append(tutar)
                oranlar.append(oran)
                self.idler.append(id)
            
            for row in son_odemeler:
                ui.cmb_sec.addItem(row)
            
            si = 0
            
            ui.txt_kalan.setText(str(len(taksitler)))
            ui.txt_taksit.setText(str(tutarlar[si]))
            ui.txt_toplam.setText(str(tutarlar[si]*taksitler[si]))
            ui.cmb_sec.setCurrentIndex(0)
            ui.txt_tarih.setText(str(datetime.now().strftime("%Y-%m-%d")))
           
        yazdır()
        
        print("Çalıştı odeme Show")
        
        return super().showEvent(a0)

baglanti.commit()


