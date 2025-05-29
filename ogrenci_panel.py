import typing
from PyQt6 import *
import sys
import time
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget
from ogrenci_kontrol import Ui_Form
import sqlite3


baglanti = sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()


table = islem.execute("create table if not exists kisiler (ad text, tarih text, gsm text, bolum text, eknot text, unvan text, ders text,id	integer unique,PRIMARY KEY('id' AUTOINCREMENT))")
baglanti.commit()


class ogrenciPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ogrenciform = Ui_Form()
        self.ogrenciform.setupUi(self)
        ui = self.ogrenciform
        
        def id_bul():
            sorgu = "SELECT id FROM tutucu ORDER BY id DESC LIMIT 1"
            islem.execute(sorgu)
            son_satir_id = islem.fetchone()[0]
            print("Son satırdaki id:", son_satir_id)
            idf = son_satir_id
            return idf        

        def kayitcek(sutun,tablo):
            idf = id_bul()
            sorgu = "select {} from {} where id = ?".format(sutun, tablo)
            print(idf)
            islem.execute(sorgu,(idf,))


        def kayityaz():
            idf = id_bul()
            baglanti = sqlite3.connect("database.db")
            baglanti.commit()

            ad = kayitcek("ad","kisiler")
            tarih = kayitcek("tarih","kisiler")
            gsm = kayitcek("gsm","kisiler")
            bolum = kayitcek("bolum","kisiler")
            eknot = kayitcek("eknot","kisiler")
            unvan = kayitcek("unvan","kisiler")
            ders = kayitcek("ders","kisiler")

            email = kayitcek("email","detay")
            anlasilan = kayitcek("anlasilan","detay")
            odenen = kayitcek("odenen","detay")
            gereken = kayitcek("gereken","detay")
            alacagi = kayitcek("alacagi","detay")
            son_odeme = kayitcek("son_odeme","detay")
            
            if anlasilan == "YOK":
                anlasilan = "0"
            if odenen == "YOK":
                odenen = "0"
            if gereken == "YOK":
                gereken = int(anlasilan) - int(odenen)
            if alacagi == "YOK":
                alacagi = int(odenen) - (anlasilan)
                if alacagi <= 0:
                    alacagi = "Yok"
            
            ui.label_ad2.setText(ad)
            ui.label_tarih2.setText(tarih)
            ui.label_bolum2.setText(bolum)
            ui.label_label_gsm2.setText(gsm)
            ui.label_not2.setText(eknot)
            ui.label_unvan2.setText(unvan)
            ui.label_ders2.setText(ders)
            ui.label_mail2.setText(email)
            ui.label_anlaslan2.setText(anlasilan)
            ui.label_odenen2.setText(odenen)
            ui.label_gereken2.setText(gereken)
            ui.label_alacagi2.setText(alacagi)
            ui.label_sonodeme2.setText(son_odeme)
            
        kayityaz()
            
            
            
            
            
        
        
#silid = "delete from tutucu"
#islem.execute(silid)
baglanti.commit()