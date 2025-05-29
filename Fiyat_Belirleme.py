from Fiyat_Guncelle import Ui_Form
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
from sqlite3 import *

baglanti=sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists fiyatlar (dersler text, fiyatları text,id integer unique,PRIMARY KEY('id' AUTOINCREMENT))")
baglanti.commit()

class FiyatPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Fiyat = Ui_Form()
        self.Fiyat.setupUi(self)
        ui = self.Fiyat
        ui.Secilen_Ders.setVisible(False)
        ui.Mevcut_Fiyat.setVisible(False)
        ui.Text_3.setVisible(False)
        ui.Text_4.setVisible(False)
        ui.Guncelle_Edit.setVisible(False)
        ui.Guncelle_Btn.setVisible(False)
        islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
        for row in islem.fetchall():
            ui.Dersler_Box.addItem(row[0])
        ui.Dersler_Box.setCurrentIndex(-1)
        
        def Seç():
            mevcut = ui.Dersler_Box.currentText()
            islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = '{}';".format(mevcut))
            fiyat = islem.fetchone()
            return fiyat
            
        def yazdır():
            mevcut = ui.Dersler_Box.currentText()
            fiyat = Seç()
            ui.Secilen_Ders.setText(mevcut)
            ui.Mevcut_Fiyat.setText(fiyat[0])
            ui.Secilen_Ders.setVisible(True)
            ui.Mevcut_Fiyat.setVisible(True)
            ui.Text_3.setVisible(True)
            ui.Text_4.setVisible(True)
            ui.Guncelle_Edit.setVisible(True)
            ui.Guncelle_Btn.setVisible(True)

    
        def Fiyat_Guncelle():
            pencere = QWidget()
            
            y_fiyat = ui.Guncelle_Edit.text()
            mevcut = ui.Dersler_Box.currentText()
            islem.execute("SELECT id FROM fiyatlar WHERE dersler = '{}';".format(mevcut))
            secilen_id = islem.fetchone()[0]
            islem.execute("UPDATE fiyatlar SET fiyatları = '{}' WHERE id = '{}';".format(y_fiyat, secilen_id))
            baglanti.commit()
            yazdır()
                
        ui.Guncelle_Btn.clicked.connect(Fiyat_Guncelle)
        ui.Sec_Btn.clicked.connect(yazdır)
        
            
     
baglanti.commit()
        

        

            
            
            
            

            