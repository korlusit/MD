import sqlite3
import typing
from PyQt6 import *
import sys
import time
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import QShowEvent
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QWidget
from guncelle import Ui_Form
from taksit_goruntuleme_sayfasi import TaksitgPage

baglanti=sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists kisiler (ad text, tarih text, gsm text, bolum text, eknot text, unvan text, ders text,id	integer unique,PRIMARY KEY('id' AUTOINCREMENT))")
baglanti.commit()
        
app = QApplication(sys.argv) 
pencere10 = TaksitgPage()

class GuncellePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.guncelle = Ui_Form()
        self.guncelle.setupUi(self)
        ui = self.guncelle
        ui.label_baslik_2.setVisible(False)
        islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
        for row in islem.fetchall():
            ui.cmbders.addItem(row[0])
        ui.cmbders.setCurrentIndex(-1)
        islem.execute("SELECT DISTINCT ad FROM indirimler;")
        for row in islem.fetchall():
            ui.indirim_box.addItem(row[0])
        ui.indirim_box.setCurrentIndex(-1)
        self.idf = 0
            
        
        def temizle():
           ui.lne_ad .clear()
           ui.tarih_text.clear()
           ui.lne_gsm.clear()
           ui.cmbdurum.setCurrentIndex(-1)
           ui.lne_not.clear()
           ui.lne_meslek.clear()
           ui.cmbders.setCurrentIndex(-1)
           ui.lne_mail.clear()
           ui.lne_anlasilan.clear()
           ui.lne_odenen.clear()
           ui.lne_gereken.clear()
           ui.lcdNumber.display(0)
           ui.lnetarih.clear()
            
        
        def hatamesaj(msg):
            ui.label_baslik_2.setVisible(True)
            ui.label_baslik_2.setText(msg)
            
        def kapat():
            self.close()
            
            
        def kayitcek(sutun, tablo):
            idf = self.idf
            sorgu = "select {} from {} where id = ?".format(sutun, tablo)
            islem.execute(sorgu, (idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return 0
            
        def kayitcek2(sutun, tablo, secilen):
            idf = secilen
            sorgu = "select {} from {} where ad = ?".format(sutun, tablo)
            islem.execute(sorgu, (idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return 0

        def guncelle():
            Ad = ui.lne_ad .text()
            Gsm = ui.lne_gsm.text()
            Bolum = ui.cmbdurum.currentIndex()
            EkNot = ui.lne_not.text()
            Unvan = ui.lne_meslek.text()
            Ders = ui.cmbders.currentIndex()
            Mail = ui.lne_mail.text()
            Anlasilan = ui.lne_anlasilan.text()
            Odenen = ui.lne_odenen.text()
            Gereken = ui.lne_gereken.text()
            Son_Odeme = ui.lnetarih.text()
            
            if Ad == "":
                Ad = "Yok"
                
            if Son_Odeme == "1.01.2000":
                Son_Odeme = "Belirlenmedi"
                
            if Bolum == -1:
                deger = kayitcek("bolum","kisiler")
                Bolum = deger
            else:
                Bolum = ui.cmbdurum.currentText()
                
            if Ders == -1:
                deger = kayitcek("ders","kisiler")
                Ders = deger
            else:
                Ders = ui.cmbders.currentText()
                
            Tarih = kayitcek("tarih","kisiler")
            
                
            
            try:
                if ui.lne_ad.text() and ui.lne_gsm.text():
                                            
                    ui.label_baslik_2.setVisible(False)
                    ekle = "UPDATE kisiler SET ad ='{}',gsm ='{}',bolum ='{}',eknot ='{}',unvan ='{}',ders ='{}' WHERE id = '{}'".format(Ad, Gsm, Bolum, EkNot, Unvan, Ders,self.idf)
                    islem.execute(ekle)
                    baglanti.commit()
                    #islem.execute("""select id from kisiler""")
                    #id = islem.lastrowid  # Son eklenen satırın ID'sini alır

                    try:
                        ekle2 = "UPDATE detay SET email ='{}',anlasilan ='{}',odenen ='{}',gereken ='{}',son_odeme ='{}' WHERE id = '{}'".format(Mail,Anlasilan,Odenen,Gereken,Son_Odeme,self.idf)
                    
                        islem.execute(ekle2)
                        baglanti.commit()
                        
                    except Exception as eror:
                        print(eror)
                    
                    islem.execute("DELETE FROM tutucu;")
                    baglanti.commit()
                    
                else:
                    hatamesaj("Lütfen Ad ve GSM ve kısımlarını doldurun")
                    print("AD,GSM,UNVAN")
            

            except Exception as error:
                print(error)
                hatamesaj("Kayıt Başarısız Oldu.")
                
            
            if ui.radio_ekran.isChecked():
                pass
            else:
                kapat()
                self.dersler.clear()
            temizle()
        
        def yazdır():
            ui.lne_ad .setText(kayitcek("ad","kisiler"))
            ui.tarih_text.setText(kayitcek("tarih","kisiler"))
            ui.lne_gsm.setText(kayitcek("gsm","kisiler"))
            ui.cmbdurum.setCurrentText(kayitcek("bolum","kisiler"))
            ui.lne_not.setText(kayitcek("eknot","kisiler"))
            ui.lne_meslek.setText(kayitcek("unvan","kisiler"))
            ui.cmbders.setCurrentText(kayitcek("ders","kisiler"))
            ders = ui.cmbders.currentText()
            ui.lne_mail.setText(kayitcek("email","detay"))
            ui.lne_anlasilan.setText(kayitcek("anlasilan","detay"))
            anlasilan = ui.lne_anlasilan.text()
            ui.lne_odenen.setText(kayitcek("odenen","detay"))
            odenen = int(ui.lne_odenen.text()) if ui.lne_odenen.text().isdigit() else 0
            ui.lne_gereken.setText(kayitcek("gereken","detay"))
            ui.lcdNumber.display(self.idf)
            veri = kayitcek("son_odeme","detay")
            veri = veri.replace(".", " ")  # Noktaları kaldır
            parcalar = veri.split()  # Parçalara ayır
            if parcalar == ['YOK'] or ['Belirlenmedi']:
               parcalar = ['0','0','0']
            ui.lnetarih.setDate(QDate(int(parcalar[0]), int(parcalar[1]), int(parcalar[2])))
            try:
                if anlasilan == "YOK" or "" or " " or None:
                    islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = '{}';".format(ders))
                    fiyat = islem.fetchone()
                    anlasilan = fiyat[0]
            except:
                pass
            try:
                if ui.lne_gereken.text() != "Taksitlendirilmiş":
                    gereken = float(anlasilan) - float(odenen)
                    gereken = str(gereken)
                    ui.lne_gereken.setText(gereken)
                else:
                    ui.lne_gereken.setText("Taksitlendirilmiş")
                    ui.lne_anlasilan.setText("Taksitlendirilmiş")
                    ui.lne_odenen.setText("Taksitlendirilmiş")
            except:
                ui.lne_gereken.setText("Taksitlendirilmiş Olabilir")
                     
        ui.guncelle_Btn.clicked.connect(guncelle)
        ui.yenile_Btn.clicked.connect(yazdır)
        
        def hesapla1():
            if ui.lne_gereken.text() != "Taksitlendirilmiş":
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
            if ui.lne_gereken.text() != "Taksitlendirilmiş":
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
            if ui.lne_gereken.text() != "Taksitlendirilmiş":
                fiyat = ui.lne_anlasilan.text()      
                tutucu.append(fiyat)
                if secim == True:
                    yfiyat = tutucu[0]
                    if yfiyat == None:
                        indirim_ad = ui.indirim_box.currentText()
                        indirim = kayitcek2("yuzde","indirimler",indirim_ad)
                        fiyat2 = float(yfiyat) / 100
                        fiyat2 = fiyat2 * float(indirim)
                        fiyat3 = float(yfiyat) - fiyat2
                        ui.lne_anlasilan.setText(str(fiyat3))
                if secim == False:
                    ui.lne_anlasilan.setText(tutucu[0])
                    ui.indirim_box.setCurrentIndex(-1)
                    
        def taksitg():
            # Bağlantıyı aç
            baglanti = sqlite3.connect('database.db')
            islem = baglanti.cursor()
            yid = self.idf
            try:
                islem.execute("insert into tutucu (id) values({})".format(yid))
            except Exception as eror:
                ui.label_baslik_2.setText("Herhangi Bir Kayıt Seçmediniz")
            baglanti.commit()
            baglanti.close()
            if yid == None:
                pass
            else:
                pencere10.setFixedSize(201,331)
                pencere10.show()
            
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
        ui.guncelle_Btn_2.clicked.connect(taksitg)
        
    
    def closeEvent(self, event):
        ui = self.guncelle
        ui.lne_ad .clear()
        ui.tarih_text.clear()
        ui.lne_gsm.clear()
        ui.cmbdurum.setCurrentIndex(-1)
        ui.lne_not.clear()
        ui.lne_meslek.clear()
        ui.cmbders.setCurrentIndex(-1)
        ui.lne_mail.clear()
        ui.lne_anlasilan.clear()
        ui.lne_odenen.clear()
        ui.lne_gereken.clear()
        ui.lcdNumber.display(0)
        ui.lnetarih.clear()
        islem.execute("DELETE FROM tutucu;")
        baglanti.commit()
        self.dersler.clear()
    
        event.accept()  # Sayfanın kapanmasına izin verir.
        
    def showEvent(self, a0: QShowEvent) -> None:
        ui = self.guncelle
        def kayitcek(sutun, tablo):
            idf = self.idf
            sorgu = "select {} from {} where id = ?".format(sutun, tablo)
            islem.execute(sorgu, (idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return "Yok"
            
        
        def yazdır():
            ui.lne_ad .setText(kayitcek("ad","kisiler"))
            ui.tarih_text.setText(kayitcek("tarih","kisiler"))
            ui.lne_gsm.setText(kayitcek("gsm","kisiler"))
            ui.cmbdurum.setCurrentText(kayitcek("bolum","kisiler"))
            ui.lne_not.setText(kayitcek("eknot","kisiler"))
            ui.lne_meslek.setText(kayitcek("unvan","kisiler"))
            ui.lne_dersler.setText(kayitcek("ders","kisiler"))
            ders = ui.cmbders.currentText()
            ui.lne_mail.setText(kayitcek("email","detay"))
            ui.lne_anlasilan.setText(kayitcek("anlasilan","detay"))
            anlasilan = ui.lne_anlasilan.text()
            ui.lne_odenen.setText(kayitcek("odenen","detay"))
            odenen = int(ui.lne_odenen.text()) if ui.lne_odenen.text().isdigit() else 0
            ui.lne_gereken.setText(kayitcek("gereken","detay"))
            ui.lcdNumber.display(self.idf)
            veri = kayitcek("son_odeme","detay")
            veri = veri.replace(".", " ")  # Noktaları kaldır
            parcalar = veri.split()  # Parçalara ayır
            if parcalar == ['YOK'] or ['Belirlenmedi']:
               parcalar = ['0','0','0']
            ui.lnetarih.setDate(QDate(int(parcalar[0]), int(parcalar[1]), int(parcalar[2])))
            try:
                if anlasilan == "YOK" or "" or " " or None:
                    islem.execute("SELECT Fiyatları FROM fiyatlar WHERE Dersler = '{}';".format(ders))
                    fiyat = islem.fetchone()
                    anlasilan = fiyat[0]
            except:
                pass
            try:
                if ui.lne_gereken.text() != "Taksitlendirilmiş":
                    gereken = float(anlasilan) - float(odenen)
                    gereken = str(gereken)
                    ui.lne_gereken.setText(gereken)
                else:
                    ui.lne_gereken.setText("Taksitlendirilmiş")
            except:
                ui.lne_gereken.setText("Taksitlendirilmiş Olabilir")    
           
        yazdır()
        
        print("Çalıştı Show Event")
        
        return super().showEvent(a0)
    
    def idbul(self, idf):
        try:
            self.idf = idf
        except Exception as eror:
            print("Guncelle {}".format(eror))

        
        
        
baglanti.commit()


