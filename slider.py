import sys
import logging
import random
import datetime
import sqlite3
import requests
import xml.etree.ElementTree as ET
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QComboBox, QCompleter, QLabel, QTableWidgetItem
from PyQt6.QtCore import QStringListModel, Qt, QTimer
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import QDateTime



def get_exchange_rates():
    try:
        url = "https://www.tcmb.gov.tr/kurlar/today.xml"
        response = requests.get(url)
        response.encoding = 'utf-8'
        root = ET.fromstring(response.text)

        currencies = {'TRY': 1.0}
        for currency in root.findall('Currency'):
            code = currency.get('CurrencyCode')
            forex_selling = currency.find('ForexSelling').text
            if forex_selling:
                currencies[code] = float(forex_selling.replace(',', '.'))

        return currencies
    except Exception as e:
        return {}

class get_education:
    name = []
    price = []

    @staticmethod
    def load():
        try:
            conn = sqlite3.connect("database.db")  # veya senin dosyan neyse
            cursor = conn.cursor()
            cursor.execute("SELECT Dersler, Fiyatları FROM fiyatlar")
            rows = cursor.fetchall()

            get_education.name = [row[0] for row in rows]
            get_education.price = [row[1] for row in rows]

            conn.close()
        except Exception as e:
            get_education.name = []
            get_education.price = []



class MarqueeLabel(QLabel):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setFont(QFont("Arial", 14))
        self.setStyleSheet("background-color: black; color: white;")
        self.setFixedHeight(30)

        self.items = items
        self.text = "   ".join(items)
        self.offset = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scrollText)
        self.timer.start(30)

    def scrollText(self):
        self.offset += 2
        text_width = self.fontMetrics().horizontalAdvance(self.text)

        # Metin ekran dışına tamamen çıktıysa sıfırla
        if self.offset >= text_width:
            self.offset = 0

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("black"))
        painter.setPen(QColor("white"))
        painter.setFont(self.font())

        text_width = self.fontMetrics().horizontalAdvance(self.text)
        x = -self.offset

        # Sonsuz scroll için 2 kopya yan yana çiziliyor
        painter.drawText(x, self.height() - 10, self.text)
        painter.drawText(x + text_width, self.height() - 10, self.text)

