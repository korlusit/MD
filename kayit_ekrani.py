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
from detayli_kayit import Ui_Form
from sqlite3 import *
from taksit_ekleme_sayfasi import TaksitPage

baglanti=sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists kisiler (ad text, tarih text, gsm text, bolum text, eknot text, unvan text, ders text,id	integer unique,PRIMARY KEY('id' AUTOINCREMENT))")
baglanti.commit()

app = QApplication(sys.argv) 
pencere9 = TaksitPage()

class kayitPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kayit = Ui_Form()
        self.kayit.setupUi(self)
        ui = self.kayit
        ui.label_baslik_2.setVisible(False)
        date_today = QDate.currentDate()
        ui.lnetarih.setDate(date_today)
        islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
        for row in islem.fetchall():
            ui.cmbders.addItem(row[0])
        ui.cmbders.setCurrentIndex(-1)
        ui.cmbders_2.setCurrentIndex(-1)
        islem.execute("SELECT DISTINCT ad FROM indirimler;")
        for row in islem.fetchall():
            ui.indirim_box.addItem(row[0])
        ui.indirim_box.setCurrentIndex(-1)
        
        def hatamesaj(msg):
            ui.label_baslik_2.setVisible(True)
            ui.label_baslik_2.setText(msg)
            
            
        def kapat():
            self.close()
            self.dersler.clear()
            
        def temizle2():
            ui.lne_ad.clear()
            ui.lnetarih.setDate(date_today)
            ui.lne_gsm.clear()
            ui.cmbders_2.setCurrentIndex(-1)
            ui.lne_dersler.clear()
            ui.lne_not.clear()
            ui.lne_meslek.clear()
            ui.cmbders.setCurrentIndex(-1)
            ui.lne_mail.clear()
            ui.lne_anlasilan.clear()
            ui.lne_odenen.clear()
            ui.lne_gereken.clear()
            ui.lnetarih_2.clear()
            self.dersler.clear()
                        
        def kayitcek2(sutun, tablo, secilen):
            idf = secilen
            sorgu = "select {} from {} where ad = ?".format(sutun, tablo)
            islem.execute(sorgu, (idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return 0
        
        def taksitle_kayit_ekle():
            Ad = ui.lne_ad.text()
            Tarih = ui.lnetarih.text()
            Gsm = ui.lne_gsm.text()
            Bolum = ui.cmbders_2.currentText()
            EkNot = ui.lne_not.text()
            Unvan = ui.lne_meslek.text()
            Ders = ui.lne_dersler.text()
            Mail = ui.lne_mail.text()
            Anlasilan = ui.lne_anlasilan.text()
            Odenen = ui.lne_odenen.text()
            Gereken = ui.lne_gereken.text()
            Son_Odeme = ui.lnetarih_2.text()
            closeKey = False
            
            if Ders == "YOK" or "" or " " or None:
                pass
            else:
                if Anlasilan == "YOK" or "" or " " or None:
                    islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = '{}';".format(Ders))
                    fiyat = islem.fetchone()
                    Anlasilan = fiyat[0]
                
                if Gereken == "YOK" or "" or " " or None or '' or ' ':
                    if Odenen == "YOK" or "" or " " or None or '' or ' ':
                        Odenen  = 0
                    Gereken = int(Anlasilan) - int(Odenen)
                    Gereken = str(Gereken)
            
            if Ad == "":
                Ad = "Yok"
            if Son_Odeme == "1.01.2000":
                Son_Odeme = "Belirlenmedi"
                
            try:
                if ui.lne_ad.text() and ui.lne_gsm.text():
                    
                    ui.label_baslik_2.setVisible(False)
                    baglanti = sqlite3.connect('database.db')
                    islem = baglanti.cursor()
                    ekle = "insert into kisiler (ad,tarih,gsm,bolum,eknot,unvan,ders) values(?,?,?,?,?,?,?)"
                    islem.execute(ekle, (Ad, Tarih, Gsm, Bolum, EkNot, Unvan, Ders))
                    #islem.execute("""select id from kisiler""")
                    id = islem.lastrowid  # Son eklenen satırın ID'sini alır

                    ekle2 = "insert into detay (ID,email,anlasilan,odenen,gereken,son_odeme) values(?,?,?,?,?,?)"
                    
                    islem.execute(ekle2,(id,Mail,Anlasilan,Odenen,"Taksitlendirilmiş",Son_Odeme))
                    baglanti.commit()
                    temizle2()
                    ui.label_baslik_2.setVisible(False)
                    closeKey = True
                    
                else:
                    hatamesaj("Lütfen Ad, GSM, ve Unvan kısımlarını doldurun")
                    print("AD,GSM,UNVAN")
            
            except Exception as error:
                print(error)
                hatamesaj("Kayıt Başarısız Oldu.")
            
            try:
                baglanti = sqlite3.connect('database.db')
                islem = baglanti.cursor()
                islem.execute("insert into tutucu (id) values({})".format(id))
                baglanti.commit()
            except Exception as eror:
                ui.label_baslik_2.setText(f"Bir Hata Oluştu:{eror}")
            
            if ui.radio_ekran.isChecked():
                temizle2()
            elif ui.label_baslik_2.setVisible == True:
                hatamesaj("Lütfen Ad, GSM, ve Unvan kısımlarını doldurun")
                print("AD,GSM,UNVAN - 2")    
            elif closeKey == True:
                if id == None:
                    pass
                else:
                    pencere9.setFixedSize(411, 517)
                    pencere9.show() 
            else:
                kapat()
                pass
            
        def kayit_ekle():
            Ad = ui.lne_ad.text()
            Tarih = ui.lnetarih.text()
            Gsm = ui.lne_gsm.text()
            Bolum = ui.cmbders_2.currentText()
            EkNot = ui.lne_not.text()
            Unvan = ui.lne_meslek.text()
            Ders = ui.lne_dersler.text()
            Mail = ui.lne_mail.text()
            Anlasilan = ui.lne_anlasilan.text()
            Odenen = ui.lne_odenen.text()
            Gereken = ui.lne_gereken.text()
            Son_Odeme = ui.lnetarih_2.text()
            closeKey = False
            
            if Ders == "YOK" or "" or " " or None:
                pass
            else:
                if Anlasilan == "YOK" or "" or " " or None:
                    islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = '{}';".format(Ders))
                    fiyat = islem.fetchone()
                    Anlasilan = fiyat[0]
                
                if Gereken == "YOK" or "" or " " or None or '' or ' ':
                    if Odenen == "YOK" or "" or " " or None or '' or ' ':
                        Odenen  = 0
                    Gereken = int(Anlasilan) - int(Odenen)
                    Gereken = str(Gereken)
            
            if Ad == "":
                Ad = "Yok"
            if Son_Odeme == "1.01.2000":
                Son_Odeme = "Belirlenmedi"
                
            try:
                if ui.lne_ad.text() and ui.lne_gsm.text():
                        
                    ui.label_baslik_2.setVisible(False)
                    ekle = "insert into kisiler (ad,tarih,gsm,bolum,eknot,unvan,ders) values(?,?,?,?,?,?,?)"
                    islem.execute(ekle, (Ad, Tarih, Gsm, Bolum, EkNot, Unvan, Ders))
                    #islem.execute("""select id from kisiler""")
                    id = islem.lastrowid  # Son eklenen satırın ID'sini alır

                    ekle2 = "insert into detay (ID,email,anlasilan,odenen,gereken,son_odeme) values(?,?,?,?,?,?)"
                    
                    islem.execute(ekle2,(id,Mail,Anlasilan,Odenen,Gereken,Son_Odeme))
                    baglanti.commit()
                    temizle2()
                    ui.label_baslik_2.setVisible(False)
                    closeKey = True
                    
                    
            
            
                else:
                    hatamesaj("Lütfen Ad, GSM, ve Unvan kısımlarını doldurun")
                    print("AD,GSM,UNVAN")
            

            except Exception as error:
                print(error)
                hatamesaj("Kayıt Başarısız Oldu.")
                
            
            if ui.radio_ekran.isChecked():
                temizle2()
            elif ui.label_baslik_2.setVisible == True:
                hatamesaj("Lütfen Ad, GSM, ve Unvan kısımlarını doldurun")
                print("AD,GSM,UNVAN - 2")    
            elif closeKey == True:
                kapat()
                self.dersler.clear()
            else:
                pass
                
        ui.pushButton.clicked.connect(kayit_ekle)
        ui.btn_taksit.clicked.connect(taksitle_kayit_ekle)

        def hesapla1():
            anlasilan = ui.lne_anlasilan.text()
            odenen = ui.lne_odenen.text()
            if odenen == '':
                odenen = 0
            if anlasilan == '':
                anlasilan = 0
            gereken = float(anlasilan) - float(odenen)
            gereken = str(gereken)
            ui.lne_gereken.setText(gereken)
            ui.lne_odenen.setFocus()
            
        def hesapla2():
            anlasilan = ui.lne_anlasilan.text()
            odenen = ui.lne_odenen.text()
            if odenen == '':
                odenen = 0
            if anlasilan == '':
                anlasilan = 0
            gereken = float(anlasilan) - float(odenen)
            gereken = str(gereken)
            ui.lne_gereken.setText(gereken)
            ui.lne_gereken.setFocus()
        
        self.dersler = []

        def hesapla3():
            try:
                secilenders = ui.cmbders.currentText()

                # Aynı dersi iki kez eklememek için kontrol
                if secilenders and secilenders not in self.dersler:
                    self.dersler.append(secilenders)

                # UI'da dersleri + ile birleştirerek göster
                ui.lne_dersler.setText(" + ".join(self.dersler))

                # Toplam fiyatı hesapla
                toplam_fiyat = 0
                for ders in self.dersler:
                    islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = ?", (ders,))
                    sonuc = islem.fetchone()
                    if sonuc:
                        toplam_fiyat += float(sonuc[0])

                # Toplam fiyatı yaz
                ui.indirim_box.setCurrentIndex(-1)
                ui.lne_anlasilan.setText(str(toplam_fiyat))

                # Gereken tutarı hesapla
                odenen = ui.lne_odenen.text()
                if not odenen:
                    odenen = 0

                gereken = float(toplam_fiyat) - float(odenen)
                ui.lne_gereken.setText(str(gereken))

            except Exception as eror:
                print(eror, "Hesapla")
                
        def dersi_cikar_ve_guncelle():
            try:
                secilenders = ui.cmbders.currentText()

                # Ders listesinde varsa çıkar
                if secilenders in self.dersler:
                    self.dersler.remove(secilenders)

                # UI'da dersleri + ile birleştirerek göster
                ui.lne_dersler.setText(" + ".join(self.dersler))

                # Toplam fiyatı güncelle
                toplam_fiyat = 0
                for ders in self.dersler:
                    islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = ?", (ders,))
                    sonuc = islem.fetchone()
                    if sonuc:
                        toplam_fiyat += float(sonuc[0])

                # Güncellenmiş fiyatı yaz
                ui.lne_anlasilan.setText(str(toplam_fiyat))

                # Gereken tutarı yeniden hesapla
                odenen = ui.lne_odenen.text()
                if not odenen:
                    odenen = 0

                gereken = float(toplam_fiyat) - float(odenen)
                ui.lne_gereken.setText(str(gereken))

            except Exception as eror:
                print(eror, "Ders Çıkarma")

        
        tutucu = []
        
        def hesapla4(secim):
            try:
                if secim == True:
                    fiyat = ui.lne_anlasilan.text()      
                    tutucu.append(fiyat)
                    yfiyat = tutucu[-1]
                    indirim_ad = ui.indirim_box.currentText()
                    indirim = kayitcek2("yuzde","indirimler",indirim_ad)
                    fiyat2 = float(yfiyat) / 100
                    fiyat2 = fiyat2 * float(indirim)
                    fiyat3 = float(yfiyat) - fiyat2
                    ui.lne_anlasilan.setText(str(fiyat3))
                if secim == False:
                    ui.lne_anlasilan.setText(tutucu[-1])
                    ui.indirim_box.setCurrentIndex(-1)
            except Exception as eror:
                print(eror)
                pass


            
        def hesapla5():
            hesapla4(False)
            hesapla2()
            
        def hesapla6():
            hesapla4(True)
            hesapla2()
            
        def gecis1():
            ui.lne_gsm.setFocus()
        def gecis2():
            ui.lne_mail.setFocus()
        def gecis3():
            ui.lne_not.setFocus()
        def gecis4():
            ui.lne_anlasilan.setFocus()
        def gecis5():
            ui.lne_ad.setFocus()
            
            
        ui.indirim_kaldir.clicked.connect(hesapla5)
        ui.indirim_box.currentIndexChanged.connect(hesapla6)
        ui.pushButton_2.clicked.connect(hesapla3)
        ui.pushButton_3.clicked.connect(dersi_cikar_ve_guncelle)
        ui.lne_ad.returnPressed.connect(gecis1)
        ui.lne_gsm.returnPressed.connect(gecis2)
        ui.lne_mail.returnPressed.connect(gecis3)
        ui.lne_not.returnPressed.connect(gecis4)
        ui.lne_anlasilan.returnPressed.connect(hesapla1)
        ui.lne_odenen.returnPressed.connect(hesapla2)
        ui.lne_gereken.returnPressed.connect(gecis5)
        
    def closeEvent(self, event):
        ui = self.kayit
        ui.lne_ad.clear()
        ui.lne_gsm.clear()
        ui.cmbders_2.setCurrentIndex(-1)
        ui.lne_dersler.clear()
        ui.lne_not.clear()
        ui.lne_meslek.clear()
        ui.cmbders.setCurrentIndex(-1)
        ui.lne_mail.clear()
        ui.lne_anlasilan.clear()
        ui.lne_odenen.clear()
        ui.lne_gereken.clear()
        ui.lnetarih_2.clear()
        self.dersler.clear()
        islem.execute("DELETE FROM tutucu;")
        baglanti.commit()
    
        event.accept()  # Sayfanın kapanmasına izin verir.
        
    def numara_ver(self, numara):
        try:
            self.kayit.lne_gsm.setText(numara)
        except Exception as eror:
            print("Guncelle {}".format(eror))


