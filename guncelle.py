# Form implementation generated from reading ui file 'UiFormats\guncelle.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 517)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setKerning(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UiFormats\\../assets/mba_logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.label_baslik2 = QtWidgets.QLabel(parent=Form)
        self.label_baslik2.setGeometry(QtCore.QRect(10, 79, 171, 31))
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(15)
        font.setKerning(False)
        self.label_baslik2.setFont(font)
        self.label_baslik2.setObjectName("label_baslik2")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 110, 281, 271))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lne_meslek = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_meslek.setFont(font)
        self.lne_meslek.setStyleSheet("")
        self.lne_meslek.setText("")
        self.lne_meslek.setObjectName("lne_meslek")
        self.verticalLayout_2.addWidget(self.lne_meslek)
        self.lne_ad = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_ad.setFont(font)
        self.lne_ad.setStyleSheet("")
        self.lne_ad.setText("")
        self.lne_ad.setObjectName("lne_ad")
        self.verticalLayout_2.addWidget(self.lne_ad)
        self.lne_gsm = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_gsm.setFont(font)
        self.lne_gsm.setStyleSheet("")
        self.lne_gsm.setObjectName("lne_gsm")
        self.verticalLayout_2.addWidget(self.lne_gsm)
        self.lne_mail = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_mail.setFont(font)
        self.lne_mail.setStyleSheet("")
        self.lne_mail.setObjectName("lne_mail")
        self.verticalLayout_2.addWidget(self.lne_mail)
        self.cmbdurum = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.cmbdurum.setStyleSheet("")
        self.cmbdurum.setEditable(False)
        self.cmbdurum.setCurrentText("")
        self.cmbdurum.setObjectName("cmbdurum")
        self.cmbdurum.addItem("")
        self.cmbdurum.addItem("")
        self.cmbdurum.addItem("")
        self.cmbdurum.addItem("")
        self.cmbdurum.addItem("")
        self.verticalLayout_2.addWidget(self.cmbdurum)
        self.indirim_box = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.indirim_box.setObjectName("indirim_box")
        self.verticalLayout_2.addWidget(self.indirim_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmbders = QtWidgets.QComboBox(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbders.sizePolicy().hasHeightForWidth())
        self.cmbders.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setKerning(False)
        self.cmbders.setFont(font)
        self.cmbders.setObjectName("cmbders")
        self.horizontalLayout.addWidget(self.cmbders)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lne_dersler = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_dersler.setFont(font)
        self.lne_dersler.setObjectName("lne_dersler")
        self.verticalLayout_2.addWidget(self.lne_dersler)
        self.lne_not = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_not.setFont(font)
        self.lne_not.setStyleSheet("")
        self.lne_not.setObjectName("lne_not")
        self.verticalLayout_2.addWidget(self.lne_not)
        self.label_baslik2_2 = QtWidgets.QLabel(parent=Form)
        self.label_baslik2_2.setGeometry(QtCore.QRect(402, 79, 171, 31))
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(15)
        font.setKerning(False)
        self.label_baslik2_2.setFont(font)
        self.label_baslik2_2.setObjectName("label_baslik2_2")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(400, 110, 141, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_15 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.layoutWidget_3 = QtWidgets.QWidget(parent=Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(540, 110, 211, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.layoutWidget_3.setFont(font)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lne_anlasilan = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_anlasilan.setFont(font)
        self.lne_anlasilan.setStyleSheet("")
        self.lne_anlasilan.setObjectName("lne_anlasilan")
        self.verticalLayout_4.addWidget(self.lne_anlasilan)
        self.lne_odenen = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_odenen.setFont(font)
        self.lne_odenen.setStyleSheet("")
        self.lne_odenen.setObjectName("lne_odenen")
        self.verticalLayout_4.addWidget(self.lne_odenen)
        self.lne_gereken = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.lne_gereken.setFont(font)
        self.lne_gereken.setStyleSheet("")
        self.lne_gereken.setObjectName("lne_gereken")
        self.verticalLayout_4.addWidget(self.lne_gereken)
        self.lnetarih = QtWidgets.QDateEdit(parent=self.layoutWidget_3)
        self.lnetarih.setStyleSheet("")
        self.lnetarih.setObjectName("lnetarih")
        self.verticalLayout_4.addWidget(self.lnetarih)
        self.layoutWidget1 = QtWidgets.QWidget(parent=Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 110, 61, 271))
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_bolum_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_bolum_2.setFont(font)
        self.label_bolum_2.setObjectName("label_bolum_2")
        self.verticalLayout.addWidget(self.label_bolum_2)
        self.label_ad = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_ad.setFont(font)
        self.label_ad.setObjectName("label_ad")
        self.verticalLayout.addWidget(self.label_ad)
        self.label_gsm = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_gsm.setFont(font)
        self.label_gsm.setObjectName("label_gsm")
        self.verticalLayout.addWidget(self.label_gsm)
        self.label_mail = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_mail.setFont(font)
        self.label_mail.setObjectName("label_mail")
        self.verticalLayout.addWidget(self.label_mail)
        self.label_bolum = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_bolum.setFont(font)
        self.label_bolum.setObjectName("label_bolum")
        self.verticalLayout.addWidget(self.label_bolum)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_ders = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_ders.setFont(font)
        self.label_ders.setObjectName("label_ders")
        self.verticalLayout.addWidget(self.label_ders)
        self.label_ders_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_ders_2.setFont(font)
        self.label_ders_2.setObjectName("label_ders_2")
        self.verticalLayout.addWidget(self.label_ders_2)
        self.label_bolum_4 = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_bolum_4.setFont(font)
        self.label_bolum_4.setObjectName("label_bolum_4")
        self.verticalLayout.addWidget(self.label_bolum_4)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(350, 450, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Display")
        font.setPointSize(40)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.guncelle_Btn = QtWidgets.QPushButton(parent=Form)
        self.guncelle_Btn.setGeometry(QtCore.QRect(400, 320, 351, 31))
        self.guncelle_Btn.setObjectName("guncelle_Btn")
        self.label_baslik_2 = QtWidgets.QLabel(parent=Form)
        self.label_baslik_2.setEnabled(True)
        self.label_baslik_2.setGeometry(QtCore.QRect(400, 390, 351, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setKerning(False)
        self.label_baslik_2.setFont(font)
        self.label_baslik_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.label_baslik_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_baslik_2.setObjectName("label_baslik_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(parent=Form)
        self.graphicsView_3.setGeometry(QtCore.QRect(375, 56, 1, 380))
        self.graphicsView_3.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.radio_ekran = QtWidgets.QRadioButton(parent=Form)
        self.radio_ekran.setGeometry(QtCore.QRect(400, 360, 121, 17))
        self.radio_ekran.setObjectName("radio_ekran")
        self.yenile_Btn = QtWidgets.QPushButton(parent=Form)
        self.yenile_Btn.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.yenile_Btn.setObjectName("yenile_Btn")
        self.id_text = QtWidgets.QLabel(parent=Form)
        self.id_text.setGeometry(QtCore.QRect(10, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setKerning(False)
        self.id_text.setFont(font)
        self.id_text.setObjectName("id_text")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=Form)
        self.lcdNumber.setGeometry(QtCore.QRect(90, 420, 141, 31))
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Mode.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber.setProperty("intValue", 100000)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_bolum_3 = QtWidgets.QLabel(parent=Form)
        self.label_bolum_3.setGeometry(QtCore.QRect(10, 390, 59, 23))
        font = QtGui.QFont()
        font.setFamily("DecoType Naskh")
        font.setPointSize(12)
        font.setKerning(False)
        self.label_bolum_3.setFont(font)
        self.label_bolum_3.setObjectName("label_bolum_3")
        self.tarih_text = QtWidgets.QLabel(parent=Form)
        self.tarih_text.setGeometry(QtCore.QRect(70, 390, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setKerning(False)
        self.tarih_text.setFont(font)
        self.tarih_text.setStyleSheet("")
        self.tarih_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tarih_text.setObjectName("tarih_text")
        self.indirim_kaldir = QtWidgets.QPushButton(parent=Form)
        self.indirim_kaldir.setGeometry(QtCore.QRect(630, 85, 121, 21))
        self.indirim_kaldir.setObjectName("indirim_kaldir")
        self.guncelle_Btn_2 = QtWidgets.QPushButton(parent=Form)
        self.guncelle_Btn_2.setGeometry(QtCore.QRect(400, 280, 351, 31))
        self.guncelle_Btn_2.setObjectName("guncelle_Btn_2")
        self.layoutWidget.raise_()
        self.graphicsView_3.raise_()
        self.layoutWidget.raise_()
        self.label_baslik2.raise_()
        self.label_baslik2_2.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.label.raise_()
        self.guncelle_Btn.raise_()
        self.label_baslik_2.raise_()
        self.radio_ekran.raise_()
        self.yenile_Btn.raise_()
        self.id_text.raise_()
        self.lcdNumber.raise_()
        self.label_bolum_3.raise_()
        self.tarih_text.raise_()
        self.indirim_kaldir.raise_()
        self.guncelle_Btn_2.raise_()

        self.retranslateUi(Form)
        self.cmbdurum.setCurrentIndex(-1)
        self.cmbders.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Görüntüle ve Güncelle"))
        self.label_baslik2.setWhatsThis(_translate("Form", "<html><head/><body><p>asadsd</p></body></html>"))
        self.label_baslik2.setText(_translate("Form", "Hakkında:"))
        self.cmbdurum.setItemText(0, _translate("Form", "Kayıt"))
        self.cmbdurum.setItemText(1, _translate("Form", "Görüşme"))
        self.cmbdurum.setItemText(2, _translate("Form", "Olumlu"))
        self.cmbdurum.setItemText(3, _translate("Form", "Kararsız"))
        self.cmbdurum.setItemText(4, _translate("Form", "Olumsuz"))
        self.pushButton_2.setText(_translate("Form", "+"))
        self.pushButton_3.setText(_translate("Form", "-"))
        self.label_baslik2_2.setWhatsThis(_translate("Form", "<html><head/><body><p>asadsd</p></body></html>"))
        self.label_baslik2_2.setText(_translate("Form", "Ödeme Kontrol:"))
        self.label_11.setText(_translate("Form", "Anlaşılan Miktar:"))
        self.label_15.setText(_translate("Form", "Ödediği Tutar:"))
        self.label_16.setText(_translate("Form", "Ödemesi Gereken:"))
        self.label_18.setText(_translate("Form", "Son Ödeme Tarihi:"))
        self.label_bolum_2.setText(_translate("Form", "Meslek:"))
        self.label_ad.setText(_translate("Form", "Adı:"))
        self.label_gsm.setText(_translate("Form", "GSM:"))
        self.label_mail.setText(_translate("Form", "e-mail:"))
        self.label_bolum.setText(_translate("Form", "Durum"))
        self.label_3.setText(_translate("Form", "İndirim:"))
        self.label_ders.setText(_translate("Form", "Dersi:"))
        self.label_ders_2.setText(_translate("Form", "Dersler:"))
        self.label_bolum_4.setText(_translate("Form", "Ek Not:"))
        self.label.setText(_translate("Form", "MBA"))
        self.guncelle_Btn.setText(_translate("Form", "Güncelle"))
        self.label_baslik_2.setText(_translate("Form", "HATA MESAJI"))
        self.radio_ekran.setText(_translate("Form", "Ekran Açık Kalsın"))
        self.yenile_Btn.setText(_translate("Form", "Yenile"))
        self.id_text.setText(_translate("Form", "MBA ID:"))
        self.label_bolum_3.setText(_translate("Form", "Tarih:"))
        self.tarih_text.setText(_translate("Form", "Tarih"))
        self.indirim_kaldir.setText(_translate("Form", "İndirim Kaldır"))
        self.guncelle_Btn_2.setText(_translate("Form", "Taksit Bilgisini Görüntüle"))
