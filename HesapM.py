import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout,
    QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MBA Hesap Makinesi")
        self.setFixedSize(300, 200)
        self.initUI()

    def initUI(self):
        self.current = ''
        frame = QVBoxLayout()

        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)  # ✅ DÜZENLENDİ
        self.display.setMaxLength(15)

        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        frame.addWidget(self.display)

        grid = QGridLayout()
        grid.setSpacing(5)
        frame.addLayout(grid)

        self.setLayout(frame)

        names = [
            'Temizle', 'Sil', 'Çık', u"\N{DIVISION SIGN}",
            '7', '8', '9', u"\N{MULTIPLICATION SIGN}",
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '00', '.', '='
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.resize(10, 10)
            button.clicked.connect(self.press_btn)
            grid.addWidget(button, *position)

    def press_btn(self):
        button_text = self.sender()
        text = button_text.text()

        if text == 'Temizle':
            self.current = ''
            self.display.setText(self.current)
        elif text == 'Sil':
            self.current = self.current[:-1]
            self.display.setText(self.current)
        elif text == 'Çık':
            self.close()
        elif text == '=':
            try:
                expr = self.current.replace(u"\N{DIVISION SIGN}", '/').replace(u"\N{MULTIPLICATION SIGN}", '*')
                self.current = str(eval(expr))
                self.display.setText(self.current)
            except Exception as e:
                QMessageBox.about(self, 'Hesap Makinesi', 'Bir Hata Oluştu: ' + str(e))
        else:
            self.current += text
            self.display.setText(self.current)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Hesap = Example()
    Hesap.show()
    sys.exit(app.exec())
