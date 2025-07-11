# Form implementation generated from reading ui file 'UiFormats\User_Interface_max.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(1887, 992)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UiFormats\\../assets/mba_logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setTabletTracking(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tbllistele = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tbllistele.setEnabled(True)
        self.tbllistele.setGeometry(QtCore.QRect(370, 60, 1490, 921))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbllistele.sizePolicy().hasHeightForWidth())
        self.tbllistele.setSizePolicy(sizePolicy)
        self.tbllistele.setBaseSize(QtCore.QSize(0, 0))
        self.tbllistele.setMouseTracking(False)
        self.tbllistele.setTabletTracking(False)
        self.tbllistele.setAcceptDrops(False)
        self.tbllistele.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tbllistele.setStyleSheet("")
        self.tbllistele.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tbllistele.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tbllistele.setLineWidth(1)
        self.tbllistele.setAutoScrollMargin(16)
        self.tbllistele.setTabKeyNavigation(True)
        self.tbllistele.setAlternatingRowColors(False)
        self.tbllistele.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tbllistele.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tbllistele.setShowGrid(True)
        self.tbllistele.setGridStyle(QtCore.Qt.PenStyle.CustomDashLine)
        self.tbllistele.setWordWrap(True)
        self.tbllistele.setCornerButtonEnabled(True)
        self.tbllistele.setRowCount(200)
        self.tbllistele.setColumnCount(8)
        self.tbllistele.setObjectName("tbllistele")
        self.tbllistele.horizontalHeader().setCascadingSectionResizes(False)
        self.tbllistele.horizontalHeader().setDefaultSectionSize(180)
        self.btnara = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnara.setGeometry(QtCore.QRect(370, 40, 31, 21))
        self.btnara.setStyleSheet("border:none;\n"
"background-color:#004626;\n"
"color:white;")
        self.btnara.setObjectName("btnara")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-50, -310, 391, 5000))
        self.frame.setStyleSheet("border: 1px solid black;\n"
"background-color: #004201;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btnekle = QtWidgets.QPushButton(parent=self.frame)
        self.btnekle.setGeometry(QtCore.QRect(50, 370, 341, 31))
        self.btnekle.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnekle.setObjectName("btnekle")
        self.btnsil = QtWidgets.QPushButton(parent=self.frame)
        self.btnsil.setGeometry(QtCore.QRect(50, 430, 341, 31))
        self.btnsil.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnsil.setObjectName("btnsil")
        self.btndetay = QtWidgets.QPushButton(parent=self.frame)
        self.btndetay.setGeometry(QtCore.QRect(50, 460, 341, 31))
        self.btndetay.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btndetay.setObjectName("btndetay")
        self.btnlistele = QtWidgets.QPushButton(parent=self.frame)
        self.btnlistele.setGeometry(QtCore.QRect(50, 400, 341, 31))
        self.btnlistele.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnlistele.setObjectName("btnlistele")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(60, 340, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"color:white;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 510, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;\n"
"color:white\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.btnfiyatg = QtWidgets.QPushButton(parent=self.frame)
        self.btnfiyatg.setGeometry(QtCore.QRect(50, 540, 341, 31))
        self.btnfiyatg.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnfiyatg.setObjectName("btnfiyatg")
        self.btnindirim = QtWidgets.QPushButton(parent=self.frame)
        self.btnindirim.setGeometry(QtCore.QRect(50, 570, 341, 31))
        self.btnindirim.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnindirim.setObjectName("btnindirim")
        self.btndersekle = QtWidgets.QPushButton(parent=self.frame)
        self.btndersekle.setGeometry(QtCore.QRect(50, 600, 341, 31))
        self.btndersekle.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btndersekle.setObjectName("btndersekle")
        self.btnrapor = QtWidgets.QPushButton(parent=self.frame)
        self.btnrapor.setGeometry(QtCore.QRect(50, 700, 341, 31))
        self.btnrapor.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnrapor.setObjectName("btnrapor")
        self.btngelirgider = QtWidgets.QPushButton(parent=self.frame)
        self.btngelirgider.setGeometry(QtCore.QRect(50, 730, 341, 31))
        self.btngelirgider.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btngelirgider.setObjectName("btngelirgider")
        self.btnpersoneller = QtWidgets.QPushButton(parent=self.frame)
        self.btnpersoneller.setGeometry(QtCore.QRect(50, 760, 341, 31))
        self.btnpersoneller.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnpersoneller.setObjectName("btnpersoneller")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(60, 670, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none;\n"
"color:white\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.logo = QtWidgets.QLabel(parent=self.frame)
        self.logo.setGeometry(QtCore.QRect(70, 910, 301, 281))
        self.logo.setStyleSheet("border:none;")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.btnpersoneller_2 = QtWidgets.QPushButton(parent=self.frame)
        self.btnpersoneller_2.setGeometry(QtCore.QRect(50, 790, 341, 31))
        self.btnpersoneller_2.setStyleSheet("color:white;\n"
"background-color: #004221;\n"
"")
        self.btnpersoneller_2.setObjectName("btnpersoneller_2")
        self.lnearaad = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lnearaad.setGeometry(QtCore.QRect(400, 40, 180, 20))
        self.lnearaad.setTabletTracking(False)
        self.lnearaad.setAutoFillBackground(False)
        self.lnearaad.setStyleSheet("border:1px solid black;")
        self.lnearaad.setInputMask("")
        self.lnearaad.setText("")
        self.lnearaad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lnearaad.setObjectName("lnearaad")
        self.lnearatarih = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lnearatarih.setGeometry(QtCore.QRect(580, 40, 180, 20))
        self.lnearatarih.setTabletTracking(False)
        self.lnearatarih.setStyleSheet("border:1px solid black;")
        self.lnearatarih.setInputMask("")
        self.lnearatarih.setText("")
        self.lnearatarih.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lnearatarih.setObjectName("lnearatarih")
        self.lnearagsm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lnearagsm.setGeometry(QtCore.QRect(760, 40, 180, 20))
        self.lnearagsm.setTabletTracking(False)
        self.lnearagsm.setStyleSheet("border:1px solid black;")
        self.lnearagsm.setInputMask("")
        self.lnearagsm.setText("")
        self.lnearagsm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lnearagsm.setObjectName("lnearagsm")
        self.lnearanot = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lnearanot.setGeometry(QtCore.QRect(1120, 40, 180, 20))
        self.lnearanot.setTabletTracking(False)
        self.lnearanot.setStyleSheet("border:1px solid black;")
        self.lnearanot.setInputMask("")
        self.lnearanot.setText("")
        self.lnearanot.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lnearanot.setObjectName("lnearanot")
        self.sutun_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sutun_btn.setGeometry(QtCore.QRect(1829, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sutun_btn.setFont(font)
        self.sutun_btn.setStyleSheet("border:none;\n"
"background-color:#004626;\n"
"color:white;")
        self.sutun_btn.setObjectName("sutun_btn")
        self.lnesecders = QtWidgets.QComboBox(parent=self.centralwidget)
        self.lnesecders.setGeometry(QtCore.QRect(1480, 40, 181, 21))
        self.lnesecders.setStyleSheet("")
        self.lnesecders.setObjectName("lnesecders")
        self.lnesecders.addItem("")
        self.lnesecdurum = QtWidgets.QComboBox(parent=self.centralwidget)
        self.lnesecdurum.setGeometry(QtCore.QRect(940, 40, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setKerning(False)
        self.lnesecdurum.setFont(font)
        self.lnesecdurum.setAutoFillBackground(False)
        self.lnesecdurum.setStyleSheet("")
        self.lnesecdurum.setObjectName("lnesecdurum")
        self.lnesecdurum.addItem("")
        self.lnesecdurum.addItem("")
        self.lnesecdurum.addItem("")
        self.lnesecdurum.addItem("")
        self.lnesecdurum.addItem("")
        self.lnesecdurum.addItem("")
        self.lnearaid = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lnearaid.setGeometry(QtCore.QRect(1660, 40, 171, 20))
        self.lnearaid.setTabletTracking(False)
        self.lnearaid.setStyleSheet("border:1px solid black;")
        self.lnearaid.setInputMask("")
        self.lnearaid.setText("")
        self.lnearaid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lnearaid.setObjectName("lnearaid")
        self.lnearameslek = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lnearameslek.setGeometry(QtCore.QRect(1300, 40, 180, 20))
        self.lnearameslek.setTabletTracking(False)
        self.lnearameslek.setStyleSheet("border:1px solid black;")
        self.lnearameslek.setInputMask("")
        self.lnearameslek.setText("")
        self.lnearameslek.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lnearameslek.setObjectName("lnearameslek")
        self.wdg_slider = QtWidgets.QWidget(parent=self.centralwidget)
        self.wdg_slider.setGeometry(QtCore.QRect(310, 0, 1641, 26))
        self.wdg_slider.setObjectName("wdg_slider")
        self.tbllistele.raise_()
        self.wdg_slider.raise_()
        self.frame.raise_()
        self.btnara.raise_()
        self.lnearaad.raise_()
        self.lnearatarih.raise_()
        self.lnearagsm.raise_()
        self.lnearanot.raise_()
        self.sutun_btn.raise_()
        self.lnesecders.raise_()
        self.lnesecdurum.raise_()
        self.lnearaid.raise_()
        self.lnearameslek.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1887, 23))
        self.menubar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.menubar.setStyleSheet("background-color: #004626;\n"
"border:1px solid black;\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-color: rgb(170, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(parent=self.menubar)
        self.menuDosya.setGeometry(QtCore.QRect(302, 102, 155, 74))
        self.menuDosya.setStyleSheet("")
        self.menuDosya.setObjectName("menuDosya")
        self.menuAra_lar = QtWidgets.QMenu(parent=self.menubar)
        self.menuAra_lar.setObjectName("menuAra_lar")
        self.menuDersler = QtWidgets.QMenu(parent=self.menuAra_lar)
        self.menuDersler.setObjectName("menuDersler")
        self.menuEkran = QtWidgets.QMenu(parent=self.menubar)
        self.menuEkran.setObjectName("menuEkran")
        self.menuAyarlar = QtWidgets.QMenu(parent=self.menubar)
        self.menuAyarlar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.menuAyarlar.setObjectName("menuAyarlar")
        self.menuKay_t = QtWidgets.QMenu(parent=self.menubar)
        self.menuKay_t.setObjectName("menuKay_t")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setStyleSheet("background-color:#004626;\n"
"border:1px solid black;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionM_teri_Ekleme = QtGui.QAction(parent=MainWindow)
        self.actionM_teri_Ekleme.setObjectName("actionM_teri_Ekleme")
        self.actionPersonel_Ekleme = QtGui.QAction(parent=MainWindow)
        self.actionPersonel_Ekleme.setObjectName("actionPersonel_Ekleme")
        self.actionE_itmen_Ekleme = QtGui.QAction(parent=MainWindow)
        self.actionE_itmen_Ekleme.setObjectName("actionE_itmen_Ekleme")
        self.save_exc = QtGui.QAction(parent=MainWindow)
        self.save_exc.setObjectName("save_exc")
        self.actionDetayl_Kay_t = QtGui.QAction(parent=MainWindow)
        self.actionDetayl_Kay_t.setObjectName("actionDetayl_Kay_t")
        self.actionHesap_Makinesi = QtGui.QAction(parent=MainWindow)
        self.actionHesap_Makinesi.setObjectName("actionHesap_Makinesi")
        self.actionNotlar = QtGui.QAction(parent=MainWindow)
        self.actionNotlar.setObjectName("actionNotlar")
        self.actionFiyat = QtGui.QAction(parent=MainWindow)
        self.actionFiyat.setObjectName("actionFiyat")
        self.actionDers = QtGui.QAction(parent=MainWindow)
        self.actionDers.setObjectName("actionDers")
        self.actionG_ncelle = QtGui.QAction(parent=MainWindow)
        self.actionG_ncelle.setObjectName("actionG_ncelle")
        self.menuDosya.addAction(self.save_exc)
        self.menuDersler.addAction(self.actionFiyat)
        self.menuDersler.addAction(self.actionDers)
        self.menuAra_lar.addAction(self.actionHesap_Makinesi)
        self.menuAra_lar.addAction(self.actionNotlar)
        self.menuAra_lar.addAction(self.menuDersler.menuAction())
        self.menuAyarlar.addAction(self.actionG_ncelle)
        self.menuKay_t.addAction(self.actionDetayl_Kay_t)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuKay_t.menuAction())
        self.menubar.addAction(self.menuAra_lar.menuAction())
        self.menubar.addAction(self.menuEkran.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())

        self.retranslateUi(MainWindow)
        self.lnesecders.setCurrentIndex(-1)
        self.lnesecdurum.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mimari Bilişim Akademisi Veritabanı - Beta 0.8"))
        self.tbllistele.setSortingEnabled(False)
        self.btnara.setText(_translate("MainWindow", "Ara"))
        self.btnekle.setText(_translate("MainWindow", "Kayıt Ekle"))
        self.btnsil.setText(_translate("MainWindow", "Sil"))
        self.btndetay.setText(_translate("MainWindow", "Detay"))
        self.btnlistele.setText(_translate("MainWindow", "Güncelle"))
        self.label.setText(_translate("MainWindow", "Kayıt İşlemleri"))
        self.label_2.setText(_translate("MainWindow", "Ders İşlemleri"))
        self.btnfiyatg.setText(_translate("MainWindow", "Fiyat Güncelle"))
        self.btnindirim.setText(_translate("MainWindow", "İndirim Belirle"))
        self.btndersekle.setText(_translate("MainWindow", "Ders Ekle/Çıkar"))
        self.btnrapor.setText(_translate("MainWindow", "Yönetim Raporu"))
        self.btngelirgider.setText(_translate("MainWindow", "Gelir Gider Tablosu"))
        self.btnpersoneller.setText(_translate("MainWindow", "Personeller"))
        self.label_6.setText(_translate("MainWindow", "Yönetim İşlemleri"))
        self.btnpersoneller_2.setText(_translate("MainWindow", "Analizler"))
        self.lnearaad.setPlaceholderText(_translate("MainWindow", "Ada Göre"))
        self.lnearatarih.setPlaceholderText(_translate("MainWindow", "Tarihe Göre"))
        self.lnearagsm.setPlaceholderText(_translate("MainWindow", "GSM\'ye Göre"))
        self.lnearanot.setPlaceholderText(_translate("MainWindow", "Ek Nota Göre"))
        self.sutun_btn.setText(_translate("MainWindow", "İptal"))
        self.lnesecders.setPlaceholderText(_translate("MainWindow", "Derse Göre"))
        self.lnesecders.setItemText(0, _translate("MainWindow", "Hepsi"))
        self.lnesecdurum.setPlaceholderText(_translate("MainWindow", "Duruma Göre"))
        self.lnesecdurum.setItemText(0, _translate("MainWindow", "Kayıt"))
        self.lnesecdurum.setItemText(1, _translate("MainWindow", "Görüşme"))
        self.lnesecdurum.setItemText(2, _translate("MainWindow", "Olumlu"))
        self.lnesecdurum.setItemText(3, _translate("MainWindow", "Kararsız"))
        self.lnesecdurum.setItemText(4, _translate("MainWindow", "Olumsuz"))
        self.lnesecdurum.setItemText(5, _translate("MainWindow", "Hepsi"))
        self.lnearaid.setPlaceholderText(_translate("MainWindow", "ID ye Göre"))
        self.lnearameslek.setPlaceholderText(_translate("MainWindow", "Mesleğe Göre"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuAra_lar.setTitle(_translate("MainWindow", "Araçlar"))
        self.menuDersler.setTitle(_translate("MainWindow", "Dersler"))
        self.menuEkran.setTitle(_translate("MainWindow", "Ekran"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuKay_t.setTitle(_translate("MainWindow", "Yeni Kayıt"))
        self.actionM_teri_Ekleme.setText(_translate("MainWindow", "Müşteri Ekleme"))
        self.actionPersonel_Ekleme.setText(_translate("MainWindow", "Personel Ekleme"))
        self.actionE_itmen_Ekleme.setText(_translate("MainWindow", "Eğitmen Ekleme"))
        self.save_exc.setText(_translate("MainWindow", "Ecxel Olarak Kaydet"))
        self.actionDetayl_Kay_t.setText(_translate("MainWindow", "Detaylı Kayıt"))
        self.actionHesap_Makinesi.setText(_translate("MainWindow", "Hesap Makinesi"))
        self.actionNotlar.setText(_translate("MainWindow", "Notlar"))
        self.actionFiyat.setText(_translate("MainWindow", "Fiyat Güncelle"))
        self.actionDers.setText(_translate("MainWindow", "Ders Ekle/Çıkar"))
        self.actionG_ncelle.setText(_translate("MainWindow", "Güncelle"))
