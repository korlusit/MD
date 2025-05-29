import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
import qtawesome as qta

class HoverButton(QPushButton):
    def __init__(self, text, icon_normal, icon_hover):
        super().__init__(text)
        self.icon_normal = icon_normal
        self.icon_hover = icon_hover
        self.setIcon(self.icon_normal)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 16px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                color: blue;
            }
        """)

    def enterEvent(self, event):
        self.setIcon(self.icon_hover)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self.icon_normal)
        super().leaveEvent(event)

class GunesliMetin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İkon Hover Değiştirme")

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        icon_normal = qta.icon('fa5s.sun', color='white')
        icon_hover = qta.icon('fa5s.sun', color='blue')

        btn = HoverButton("  Güneşli Metin", icon_normal, icon_hover)
        btn.clicked.connect(lambda: print("Güneşli Metin tıklandı"))

        layout.addWidget(btn)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = GunesliMetin()
    pencere.show()
    sys.exit(app.exec())
