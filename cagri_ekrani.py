# Form implementation generated from reading ui file 'UiFormats\cagri_ekrani.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(512, 145)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UiFormats\\../assets/mba_logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        widget.setWindowIcon(icon)
        self.lbl_tur = QtWidgets.QLabel(parent=widget)
        self.lbl_tur.setGeometry(QtCore.QRect(0, 0, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_tur.setFont(font)
        self.lbl_tur.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_tur.setObjectName("lbl_tur")
        self.lbl_gsm = QtWidgets.QLabel(parent=widget)
        self.lbl_gsm.setGeometry(QtCore.QRect(270, 50, 231, 20))
        self.lbl_gsm.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_gsm.setObjectName("lbl_gsm")
        self.lbl_ad = QtWidgets.QLabel(parent=widget)
        self.lbl_ad.setGeometry(QtCore.QRect(10, 50, 241, 20))
        self.lbl_ad.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_ad.setObjectName("lbl_ad")
        self.btn_ekle = QtWidgets.QPushButton(parent=widget)
        self.btn_ekle.setGeometry(QtCore.QRect(10, 90, 241, 24))
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_gor = QtWidgets.QPushButton(parent=widget)
        self.btn_gor.setGeometry(QtCore.QRect(260, 90, 241, 24))
        self.btn_gor.setObjectName("btn_gor")
        self.lbl_tarih = QtWidgets.QLabel(parent=widget)
        self.lbl_tarih.setGeometry(QtCore.QRect(10, 120, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbl_tarih.setFont(font)
        self.lbl_tarih.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_tarih.setObjectName("lbl_tarih")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Aramalar"))
        self.lbl_tur.setText(_translate("widget", "Çağrı Türü"))
        self.lbl_gsm.setText(_translate("widget", "TextLabel"))
        self.lbl_ad.setText(_translate("widget", "TextLabel"))
        self.btn_ekle.setText(_translate("widget", "Çağrı Ekle"))
        self.btn_gor.setText(_translate("widget", "Detaylı Gör"))
        self.lbl_tarih.setText(_translate("widget", "TextLabel"))
