import sqlite3
from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QShowEvent, QCursor, QIcon, QAction  # Eksik importları ekledik
from PyQt6.QtWidgets import *
from datetime import datetime
from arama_ekrani import Ui_widget

baglanti = sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

# Veritabanı tablosunu oluştur
table = islem.execute("create table if not exists odemeler (kid text, ad text, tarih text, tutar text, id integer unique, PRIMARY KEY('id' AUTOINCREMENT))")
baglanti.commit()

class AramaPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.arama = Ui_widget()
        self.arama.setupUi(self)
        ui = self.arama
        ui.txt_hatamesaj.setVisible(False)
        # Tabloyu ayarlamak
        ui.tbl_aramalar.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.idler = []
        self.idf = "0"

        # Temizleme fonksiyonu
        def temizle():
            ui.tbl_aramalar.clear()
            ui.lne_baslik.clear()
            ui.lne_not.clear()
            ui.txt_hatamesaj.setVisible(False)
            ui.lne_tarih.clear()

        # Hata mesajı fonksiyonu
        def hatamesaj(msg, durum):
            ui.txt_hatamesaj.setVisible(True)
            ui.txt_hatamesaj.setText(msg)
            if durum == "Hata":
                ui.txt_hatamesaj.setStyleSheet("""color:red;""")
            elif durum == "Onay":
                ui.txt_hatamesaj.setStyleSheet("""color:green;""")
            elif durum is None:
                pass

        # Kapatma fonksiyonu
        def kapat():
            self.close()

        # Veritabanından veri çekme fonksiyonu
        def kayitcek(sutun, tablo):
            try:
                idf = self.idf
                sorgu = f"SELECT {sutun} FROM {tablo} WHERE id = ?"
                islem.execute(sorgu, (idf,))
                cikti = islem.fetchone()
                if cikti:
                    return str(cikti[0])  # Dönen değeri string'e çeviriyoruz
                else:
                    return ""  # Eğer veri yoksa boş döndür
            except Exception as e:
                print("kayitcek hatası:", e)
                return ""  # Hata durumunda boş döndür

        # Yazdırma fonksiyonu
        def yazdır():
            ui.lne_baslik.setText(kayitcek("ad", "kisiler"))
            now = datetime.now()
            qdatetime = QDateTime.fromString(now.strftime("%d.%m.%Y %H.%M"), "dd.MM.yyyy HH.mm")
            ui.lne_tarih.setDateTime(qdatetime)

        # Kayıtları listeleme fonksiyonu
        def kayit_listele(musteri_id=None):
            ui.tbl_aramalar.clearContents()
            ui.tbl_aramalar.setRowCount(0)
            ui.tbl_aramalar.setColumnCount(6)
            ui.tbl_aramalar.setHorizontalHeaderLabels(("Baslik", "GSM", "Not", "Tarih", "Kişi ID", "Kayıt ID"))

            # Eğer bir müşteri ID'si belirtilmişse, ona göre sorgu oluşturuyoruz
            if musteri_id:
                sorgu = "SELECT * FROM aramalar WHERE musteri_id = ? ORDER BY id DESC"
                islem.execute(sorgu, (musteri_id,))
            else:
                sorgu = "SELECT * FROM aramalar ORDER BY id DESC"
                islem.execute(sorgu)

            veriler = islem.fetchall()

            ui.tbl_aramalar.setRowCount(len(veriler))
            for indexSatir, kayitNumarasi in enumerate(veriler):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    ui.tbl_aramalar.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))


        kayit_listele(self.idf)

        # Kayıt ekleme işlemi
        def islemci():
            try:
                islem.execute("INSERT INTO aramalar (baslik, gsm, aciklama, tarih, musteri_id) VALUES (?, ?, ?, ?, ?)", 
                              (ui.lne_baslik.text(), kayitcek("gsm", "kisiler"), ui.lne_not.text(), ui.lne_tarih.text(), self.idf))
                baglanti.commit()
                ui.txt_hatamesaj.setVisible(False)
                temizle()
                yazdır()
                kayit_listele(self.idf)
            except Exception as eror:
                print("hata islemcide:", eror)
                hatamesaj("İşlem Başarısız Oldu.", "Hata")
            baglanti.commit()

        # Kayıt silme işlemi
        def kayit_sil():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setWindowTitle("Silme Onayı")
            msg.setText("Bu kayıt silinsin mi?")

            evet_buton = msg.addButton("Evet", QMessageBox.ButtonRole.YesRole)
            hayir_buton = msg.addButton("Hayır", QMessageBox.ButtonRole.NoRole)

            msg.exec()

            if msg.clickedButton() == evet_buton:
                try:
                    # Seçilen satırdaki öğeleri alıyoruz
                    secilen_kayit = ui.tbl_aramalar.selectedItems()
                    
                    if not secilen_kayit:
                        hatamesaj("Herhangi bir kayıt seçmediniz.", "Hata")
                        return

                    # Kayıt ID'sini almak için 6. sütunu (index 5) alıyoruz
                    silinecek_kayit = secilen_kayit[5].text()  # Kayıt ID'si 6. sütunda (5. indexte)
                    
                    if not silinecek_kayit.isdigit():  # ID'nin sayısal olduğundan emin olalım
                        hatamesaj("Geçersiz Kayıt ID'si.", "Hata")
                        return

                    sorgu1 = "DELETE FROM aramalar WHERE id = ?"
                    islem.execute(sorgu1, (silinecek_kayit,))
                    baglanti.commit()

                    kayit_listele(self.idf)  # Listeyi güncelliyoruz
                    hatamesaj("Kayıt başarıyla silindi.", "Onay")
                except Exception as eror:
                    print("Kayıt silinirken hata:", eror)
                    hatamesaj("Kayıt silinirken bir hata oluştu.", "Hata")
            else:
                hatamesaj("Silme işlemi iptal edildi.", "Onay")

        # Sağ tıklama menüsü
        def showContextMenu(pos):
            globalPos = ui.tbl_aramalar.mapToGlobal(pos)  # Mouse pozisyonunu alıyoruz
            contextMenu = QMenu(ui.tbl_aramalar)  # Sağ tıklama menüsünü oluşturuyoruz
            action1 = QAction(QIcon("icons/delete.png"), "Kaydı Sil", ui.tbl_aramalar)
            contextMenu.addAction(action1)  # Menüye Silme seçeneğini ekliyoruz
            action1.triggered.connect(kayit_sil)  # Silme işlemi gerçekleştiğinde kayit_sil fonksiyonunu çağırıyoruz
            contextMenu.exec(globalPos)  # Menüyü pozisyonda gösteriyoruz

        ui.tbl_aramalar.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        ui.tbl_aramalar.customContextMenuRequested.connect(showContextMenu)

        ui.btn_ekle.clicked.connect(islemci)

    def closeEvent(self, event):
        ui = self.arama
        ui.lne_tarih.clear()
        ui.txt_hatamesaj.setVisible(False)
        ui.lne_baslik.clear()
        ui.lne_not.clear()
        ui.tbl_aramalar.clear()

        islem.execute("DELETE FROM tutucu;")
        baglanti.commit()

        event.accept()  # Sayfanın kapanmasına izin verir.

    def showEvent(self, a0: QShowEvent) -> None:
        ui = self.arama

        def kayitcek(sutun, tablo):
            sorgu = "select {} from {} where id = ?".format(sutun, tablo)
            islem.execute(sorgu, (self.idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return 0  # Veri yoksa 0 döner

        def yazdır():
            ui.lne_baslik.setText(kayitcek("ad", "kisiler"))
            now = datetime.now()
            qdatetime = QDateTime.fromString(now.strftime("%d.%m.%Y %H.%M"), "dd.MM.yyyy HH.mm")
            ui.lne_tarih.setDateTime(qdatetime)

        def kayit_listele(musteri_id=None):
            ui.tbl_aramalar.clearContents()
            ui.tbl_aramalar.setRowCount(0)
            ui.tbl_aramalar.setColumnCount(6)
            ui.tbl_aramalar.setHorizontalHeaderLabels(("Baslik", "GSM", "Not", "Tarih", "Kişi ID", "Kayıt ID"))

            # Eğer bir müşteri ID'si belirtilmişse, ona göre sorgu oluşturuyoruz
            if musteri_id:
                sorgu = "SELECT * FROM aramalar WHERE musteri_id = ? ORDER BY id DESC"
                islem.execute(sorgu, (musteri_id,))
            else:
                sorgu = "SELECT * FROM aramalar ORDER BY id DESC"
                islem.execute(sorgu)

            veriler = islem.fetchall()

            ui.tbl_aramalar.setRowCount(len(veriler))
            for indexSatir, kayitNumarasi in enumerate(veriler):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    ui.tbl_aramalar.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))


        kayit_listele(self.idf)
        yazdır()

        print("Çalıştı aramalar Show")

        return super().showEvent(a0)
    
    def idbul(self, idf):
        try:
            self.idf = idf
        except Exception as eror:
            print("Guncelle {}".format(eror))

baglanti.commit()
