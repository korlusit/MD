import sys
import time
import sqlite3
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from taksit_goruntuleme_sayfasi import *
from User_Interface_max import *
from kayit_ekrani import *
from Fiyat_Belirleme import *
from Ders_Guncelle import *
from taksit_ekleme_sayfasi import *
from Guncelleme import *
from indirim_ekrani import *
from odeme_ekrani import *
from db_to_xlsx import *
from HesapM import *
from splash import *
from sifre_giris import Ui_Form
from arama_gor_ekrani import *
from datetime import datetime
from PyQt6.QtCore import QEvent
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QPalette, QColor
from dotenv import load_dotenv
from cagri_dinleyici import FirebaseListener
from CagriDetayPenceresi import *
from main import MainPage
import logging


uygulama = QApplication(sys.argv)

pencere = MainPage()
splash = MovieSplashScreen("assets/mba3.png")
splash.show()

QtCore.QTimer.singleShot(3500, splash.close)
time.sleep(3)

pencere.showMaximized()

class FirebaseListenerThread(QThread):
    yeni_cagri_signal = pyqtSignal(dict)  # Firebase'den gelen veriyi signal olarak yay

    def __init__(self, credential_path, db_url, ref_path='call_logs'):
        super().__init__()
        self.listener = FirebaseListener(credential_path, db_url, ref_path)

    def run(self):
        self.listener.start_listening(self._callback)

    def _callback(self, data):
        self.yeni_cagri_signal.emit(data)

if __name__ == "__main__":
    listener_thread = FirebaseListenerThread(
        credential_path='phonenumberdedected-firebase-adminsdk-fbsvc-155fea36cb.json',
        db_url=os.getenv('FIREBASE_DATABASE_URL')
    )
    listener_thread.yeni_cagri_signal.connect(pencere.yeni_cagri_geldi)
    listener_thread.start()
    
sys.exit(uygulama.exec())





