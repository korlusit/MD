import sqlite3
import typing
from PyQt6 import *
import sys
import time
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget
from taksitlendirme import Ui_Form
from sqlite3 import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

baglanti=sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

def idbul():
    try:
        islem.execute("SELECT id FROM tutucu ORDER BY idt DESC LIMIT 1;")
        id = islem.fetchone()
        id = id[0]
        return id
    except Exception as eror:
        print("taksitlendirme id eror: {}".format(eror))
        
class TaksitPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.taksit = Ui_Form()
        self.taksit.setupUi(self)
        ui = self.taksit
        ui.msg_hata.setVisible(False)
        date_today = QDate.currentDate()
        ui.lne_tarih.setDate(date_today)
        ui.spn_taksit.setValue(1)
        
        def hatamesaj(msg):
            ui.msg_hata.setVisible(True)
            ui.msg_hata.setText(msg)
            
        def kapat():
            self.close()
            
        def temizle2():
            ui.lne_anlasilan.clear()
            ui.lne_tarih.setDate(date_today)
            ui.spn_taksit.clear()
            ui.spn_faiz.clear()
            ui.lne_tutar.clear()

        def kayit_ekle():
            Taksit = ui.spn_taksit.text()
            Faiz = ui.spn_faiz.text()
            Tutar = ui.lne_tutar.text()
            Tarih = ui.lne_tarih.text()

            try:
                if ui.lne_anlasilan.text() and ui.spn_taksit.text() != "0":
                    ui.msg_hata.setVisible(False)

                    # Kullanıcının girdiği tarihi datetime objesine çevir
                    tarih_dt = datetime.strptime(Tarih, "%d.%m.%Y")
                    
                    print("Taksit: ",Taksit)

                    for i in range(int(Taksit)):
                        if i == 0:
                            odeme_tarihi = tarih_dt
                        else:
                            odeme_tarihi = tarih_dt + relativedelta(months=i)

                        odeme_tarihi_str = odeme_tarihi.strftime('%Y-%m-%d')

                        ekle = "INSERT INTO taksit_odeme_tarih (son_odeme, musteri_id, tutar, oran, taksit, tarih) VALUES (?, ?, ?, ?, ?, ?)"
                        islem.execute(ekle, (odeme_tarihi_str, idbul(), Tutar, Faiz, Taksit, Tarih))
                        baglanti.commit()

                    temizle2()
                    ui.msg_hata.setVisible(False)
                    islem.execute("DELETE FROM tutucu;")
                    kapat()

                else:
                    hatamesaj("Lütfen Miktar ve Taksit kısımlarını doldurun")
                    print("miktar,taksit")

            except Exception as eror:
                print(eror)
                hatamesaj(f"Kayıt Başarısız Oldu: {eror}")
                        
        ui.btn_ekle.clicked.connect(kayit_ekle)

        def hesapla1():
            anlasilan = ui.lne_anlasilan.text()
            taksit = ui.spn_taksit.text()
            faiz = ui.spn_faiz.text()
            if anlasilan == '':
                anlasilan = 0
            x = float(anlasilan)
            y = float(taksit)
            z = float(faiz)
            if faiz == 0:
                tutar = x/y
            else:
                tutar = (x+((x*z)/100))/y
            tutar = str(tutar)
            ui.lne_tutar.setText(tutar)
                
        def gecis1():
            hesapla1()
            ui.spn_taksit.setFocus()
        def gecis2():
            hesapla1()
            ui.spn_faiz.setFocus()
        def gecis3():
            hesapla1()
            ui.lne_tarih.setFocus()
        def gecis4():
            ui.lne_anlasilan.setFocus()
            
        ui.lne_anlasilan.returnPressed.connect(gecis1)
        ui.spn_taksit.lineEdit().returnPressed.connect(gecis2)
        ui.spn_faiz.lineEdit().returnPressed.connect(gecis3)
        ui.lne_tarih.lineEdit().returnPressed.connect(gecis4)
    
    def closeEvent(self, event):
        ui = self.taksit
        ui.lne_anlasilan.clear()
        ui.lne_tarih.clear()
        ui.lne_tutar.clear()
        ui.spn_faiz.clear()
        ui.spn_taksit.clear()
        ui.msg_hata.clear()
        islem.execute("DELETE FROM tutucu;")
        baglanti.commit()
    
        event.accept()  # Sayfanın kapanmasına izin verir.