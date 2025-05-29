import time

from Ders_Ekle import Ui_Form
import sqlite3
from PyQt6.QtWidgets import QWidget

baglanti = sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()


class DersPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Ders = Ui_Form()
        self.Ders.setupUi(self)
        ui = self.Ders
        islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
        for row in islem.fetchall():
            ui.Dersler_Box.addItem(row[0])
        ui.Dersler_Box.setCurrentIndex(-1)
        ui.Secilen_Text.setVisible(False)
        ui.Cikar_Btn.setVisible(False)
        ui.Durum_Metni.setVisible(False)
        ui.Durum_Metni_2.setVisible(False)

        def boxguncelle():
            ui.Dersler_Box.clear()
            islem.execute("SELECT DISTINCT dersler FROM fiyatlar;")
            for row in islem.fetchall():
                ui.Dersler_Box.addItem(row[0])
            ui.Dersler_Box.setCurrentIndex(-1)

        def temizle():
            ui.Dersler_Box.setCurrentIndex(-1)
            ui.Cikar_Btn.setVisible(False)
            ui.Secilen_Text.setVisible(False)
            ui.Ders_fiyati.clear()
            ui.Ders_adi.clear()

        def ders_Ekle():
            try:

                eklenen = ui.Ders_adi.text()
                fiyati = ui.Ders_fiyati.text()
                if len(eklenen) > 1 or len(fiyati) > 0:
                    ekle = "insert into fiyatlar (dersler,fiyatları) values(?,?)"
                    islem.execute(ekle, (eklenen, fiyati))
                    baglanti.commit()
                    boxguncelle()
                    ui.Durum_Metni.setVisible(True)
                    ui.Durum_Metni.setText("Ders Başarıyla Eklendi.")
                    ui.Durum_Metni.setStyleSheet("border: 1px solid green; border-radius: 15px;color: green;")
                    temizle()
                elif len(eklenen) < 2 or len(fiyati) > 0:
                    ui.Durum_Metni.setVisible(True)
                    ui.Durum_Metni.setText("Dersin Adı En Az iki Karakter Olmalı. ")
                    ui.Durum_Metni.setStyleSheet("border: 1px solid red; border-radius: 15px;color: red;")
                else:
                    ui.Durum_Metni.setVisible(True)
                    ui.Durum_Metni.setText("Ders Ve Fiyatı Eklemek Zorunludur. ")
                    ui.Durum_Metni.setStyleSheet("border: 1px solid red; border-radius: 15px;color: red;")

            except:
                ui.Durum_Metni.setVisible(True)
                ui.Durum_Metni.setText("Eklenirken Bir Hata Oluştu.")
                ui.Durum_Metni.setStyleSheet("border: 1px solid red; border-radius: 15px;color: red;")

        def ders_Sec():
            secilen = ui.Dersler_Box.currentText()
            ui.Secilen_Text.setText(secilen)
            ui.Secilen_Text.setVisible(True)
            ui.Cikar_Btn.setVisible(True)

            return secilen

        def ders_Sil():
            secilen = ders_Sec()
            islem.execute("DELETE FROM fiyatlar WHERE dersler = '{}';".format(secilen))
            baglanti.commit()
            boxguncelle()
            islem.execute("SELECT EXISTS(SELECT 1 FROM fiyatlar WHERE dersler = '{}')".format(secilen))
            kontrol = islem.fetchone()[0]
            if kontrol == 1:
                ui.Durum_Metni_2.setVisible(True)
                ui.Durum_Metni_2.setText("Ders Silinemedi Tekrar Deneyin.")
                ui.Durum_Metni_2.setStyleSheet("border: 1px solid red; border-radius: 15px;color: red;")
            else:
                ui.Durum_Metni_2.setVisible(True)
                ui.Durum_Metni_2.setText("Ders Başarıyla Silindi.")
                ui.Durum_Metni_2.setStyleSheet("border: 1px solid green; border-radius: 15px;color: green;")
                temizle()

        ui.Sec_Btn.clicked.connect(ders_Sec)
        ui.Ekle_Btn.clicked.connect(ders_Ekle)
        ui.Cikar_Btn.clicked.connect(ders_Sil)


baglanti.commit()
