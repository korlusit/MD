import sqlite3
from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget
from odeme import Ui_widget

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

class OdemePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.odeme = Ui_widget()
        self.odeme.setupUi(self)
        ui = self.odeme
        ui.txt_hatamesaj.setVisible(False)
        date_today = QDate.currentDate()
            
        
        def temizle():
            ui.txt_ad.clear()
            ui.txt_anlasilan.clear()
            ui.txt_gereken.clear()
            ui.txt_hatamesaj.setVisible(False)
            ui.txt_id.clear()
            ui.txt_odenen.clear()
            ui.txt_tarih.clear()
            ui.lne_tutar.clear()
            
            
        
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
            ui.txt_anlasilan.setText(kayitcek("anlasilan","detay"))
            ui.txt_odenen.setText(kayitcek("odenen","detay"))
            ui.txt_tarih.setText(date_today.toString(Qt.ISODate))
            ui.txt_gereken.setText(kayitcek("gereken","detay"))
            

        def islemci(secenek):
            try:
                Ad = kayitcek("ad","kisiler")
                Tarih = ui.txt_tarih.text()
                Tutar = ui.lne_tutar.text()
                number = int(Tutar)
                print("Girilen değer bir sayı:", number)
                Odenen = kayitcek("odenen","detay")
                Anlasilan = kayitcek("anlasilan","detay")
            
                if secenek == "ekle":    
                    Odenen = float(Odenen) + float(Tutar)
                elif secenek == "cikar":
                    Odenen = float(Odenen) - float(Tutar)
                
                Gereken = float(Anlasilan) - Odenen
                Odenen = str(Odenen)
                Gereken = str(Gereken)
                
            except ValueError as eror:
                pass
                
            try:
                if ui.lne_tutar.text():
                                            
                    sorgu = "UPDATE detay SET odenen ='{}',gereken ='{}' WHERE id = '{}'".format(Odenen, Gereken, idbul())
                    islem.execute(sorgu)
                    baglanti.commit()
                    
                    sorgu2 = "insert into odemeler (kid,ad,tarih,tutar) values(?,?,?,?)"
                    islem.execute(sorgu2, (idbul(), Ad, Tarih, Tutar))
                    baglanti.commit()
                    ui.txt_hatamesaj.setVisible(False)
                    
                else:
                    hatamesaj("Lütfen 'Tutar' kısmını doldurun","hata")
                    print("AD,GSM,UNVAN")
            

            except Exception as error:
                print(error)
                hatamesaj("Ödeme Başarısız Oldu.","hata")
                
            
            
            if ui.txt_hatamesaj.isVisible():
                ui.lne_tutar.clear()
            else:
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
        ui = self.odeme
        ui.txt_ad.clear()
        ui.txt_anlasilan.clear()
        ui.txt_gereken.clear()
        ui.txt_hatamesaj.setVisible(False)
        ui.txt_id.clear()
        ui.txt_odenen.clear()
        ui.txt_tarih.clear()
        ui.lne_tutar.clear()
    
        islem.execute("DELETE FROM tutucu;")
        baglanti.commit()
    
        event.accept()  # Sayfanın kapanmasına izin verir.
        
    def showEvent(self, a0: QShowEvent) -> None:
        ui = self.odeme
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
            ui.txt_anlasilan.setText(kayitcek("anlasilan","detay"))
            ui.txt_odenen.setText(kayitcek("odenen","detay"))
            ui.txt_tarih.setText(date_today.toString(Qt.DateFormat.ISODate))
            ui.txt_gereken.setText(kayitcek("gereken","detay"))
            
        yazdır()
        
        print("Çalıştı odeme Show")
        
        return super().showEvent(a0)

baglanti.commit()


