import time

from indirim import Ui_Form
import sqlite3
from PyQt6.QtWidgets import QWidget

baglanti = sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()


class IndirimPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Indirim = Ui_Form()
        self.Indirim.setupUi(self)
        ui = self.Indirim
        ui.secilen_text.setVisible(False)
        ui.btn_cikar.setVisible(False)
        ui.durum_metni2.setVisible(False)
        islem.execute("SELECT DISTINCT ad FROM indirimler;")
        for row in islem.fetchall():
            ui.cmb_indirim.addItem(row[0])
        ui.cmb_indirim.setCurrentIndex(-1)
        ui.cmb_indirim.setCurrentText("Bir İndirim Seç")
        ui.lne_indirim_ad.setFocus()
        
        def temizle():
            ui.lne_indirim_ad.clear()
            ui.lne_indirim_yuzde.clear()
            
        def string_to_int(s):
            try:
                num = int(s)
                return num
            except ValueError:
                return None
        
        def txtveriekle(veri1,veri2):
            try:
                ekle = "insert into indirimler (ad,yuzde) values(?,?)"
                islem.execute(ekle,(veri1,veri2))
                baglanti.commit()
                ui.durum_metni1.setText("İndirim Eklendi.")
                ui.durum_metni2.setStyleSheet("""
                                            color:green;
                                            """)
                temizle()
            except Exception as eror:
                ui.durum_metni1.setText("Kayıt Başarısız Oldu.")
                ui.durum_metni1.setStyleSheet("""
                                              color:red;
                                              """)
                print(eror)
        
        def indirim_ekle():
            try:
                ad = ui.lne_indirim_ad.text()
                if len(ad) < 3 or len(ad) > 20:
                    ui.durum_metni1.setText("Ad, 3-20 karakter aralığında olmalı.")
                    ui.durum_metni1.setStyleSheet("""
                                              color:red;
                                              """)
                    temizle()
                else:
                    yuzde = ui.lne_indirim_yuzde.text()
                    result = string_to_int(yuzde)
                    if result is not None or int(yuzde) >= 0 or int(yuzde) <= 100:
                        ad = f"{ad} {yuzde}%"
                        print(ad,yuzde)
                        txtveriekle(ad,yuzde)
                        ui.cmb_indirim.clear()
                        islem.execute("SELECT DISTINCT ad FROM indirimler;")
                        for row in islem.fetchall():
                            ui.cmb_indirim.addItem(row[0])
                        ui.cmb_indirim.setCurrentIndex(-1)
                        ui.cmb_indirim.setCurrentText("Bir İndirim Seç")
                    else:
                        ui.durum_metni1.setText("Yuzde, 0-100 arasında bir sayı olmalı")
                        ui.durum_metni1.setStyleSheet("""
                                                    color:red;
                                                    """)
                        temizle()
                        
                    
            except Exception as eror:
                print(eror)
                
        def indirimsec():
            secilen = ui.cmb_indirim.currentText()
            ui.secilen_text.setText(secilen)
            ui.secilen_text.setVisible(True)
            ui.btn_cikar.setVisible(True)
            
        def indirimsil():
            try:
                silinen = ui.secilen_text.text()
                sil = "delete from indirimler where ad = '{}'".format(silinen)
                islem.execute(sil)
                baglanti.commit
                ui.durum_metni2.setVisible(True)
                ui.durum_metni2.setText("Başarıyla Silindi.")
                ui.durum_metni2.setStyleSheet("""
                                              color:green;
                                              """)
                ui.cmb_indirim.clear()
                islem.execute("SELECT DISTINCT ad FROM indirimler;")
                for row in islem.fetchall():
                    ui.cmb_indirim.addItem(row[0])
                ui.cmb_indirim.setCurrentIndex(-1)
                ui.cmb_indirim.setCurrentText("Bir İndirim Seç")
                
            except Exception as eror:
                print(eror)
                ui.durum_metni2.setVisible(True)
                ui.durum_metni2.setText("Silinme İşleminde Bir Hata Oluştu.")
                ui.durum_metni2.setStyleSheet("""
                                              color:red;
                                              """)
            
        def event2():
            ui.durum_metni1.setText("* Lütfen 0-100 arasında bir sayı girin,'%' işaretini kullanmayın.")
            ui.lne_indirim_yuzde.setFocus()
            
        def event3():
            ui.durum_metni1.setText("* Lütfen 0-100 arasında bir sayı girin,'%' işaretini kullanmayın.")
            indirim_ekle()
            
        
        ui.lne_indirim_ad.returnPressed.connect(event2)
        ui.lne_indirim_yuzde.returnPressed.connect(event3)
            
        
        ui.ekle_buton.clicked.connect(indirim_ekle)
        ui.btn_sec.clicked.connect(indirimsec)
        ui.btn_cikar.clicked.connect(indirimsil)
        
baglanti.commit()
            
            