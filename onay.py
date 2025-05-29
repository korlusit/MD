import typing
from PyQt6 import QtCore
import sys
import time
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QWidget
from sifre_giris import Ui_Form 

class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()  # Ui_Form sınıfını örnekleyin
        self.loginform.setupUi(self)  # setupUi metodunu çağırın
        self.onaymi = False
        
        def kontrol():
            ui = self.loginform
            uo = self
            kadi = ui.k_adi.text()
            gkodu = ui.g_kodu.text()
            
            
            if kadi == "ozlem" or "mustafa" or "talha" or "burhan":
                pass
            else:
                ui.info.setStyleSheet("color: red")
                ui.info.setText("Kullanıcı Adı Yanlış")
                
            if kadi == "ozlem" and gkodu == "Oz2023":
                ui.info.setStyleSheet("color: green")
                ui.info.setText("Giriş Başarılı.")
                uo.onaymi = True
                LoginPage().close
                    
            elif kadi == "mustafa" and gkodu == "Ms2023":
                ui.info.setStyleSheet("color: green")
                ui.info.setText("Giriş Başarılı.")
                uo.onaymi = True
                LoginPage().close
                    
            elif kadi == "talha" and gkodu == "335462":
                ui.info.setStyleSheet("color: green")
                ui.info.setText("Giriş Başarılı.")
                uo.onaymi = True
                LoginPage().close
                    
            elif kadi == "burhan" and gkodu == "5343107721":
                ui.info.setStyleSheet("color: green")
                ui.info.setText("Giriş Başarılı.")
                uo.onaymi = True
                LoginPage().close
            else:
                ui.info.setStyleSheet("color: red")  
                ui.info.setText("Şifre Yanlış.")

            return uo.onaymi
        
        self.interpage = kontrol()
        self.loginform.btn_onay.clicked.connect(kontrol)
    
    

uygulama = QApplication(sys.argv)
pencere = LoginPage()
pencere.show()
sys.exit(uygulama.exec_())
            
    
    

                
        
    



        

                


    