import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel Viewer")

        # Excel dosyasını oku
        excel_data = pd.read_excel("Excel\\denemekayit.xlsx")

        # Verileri QTableWidget'a aktar
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(excel_data.shape[0])
        self.tableWidget.setColumnCount(excel_data.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(excel_data.columns)

        for i in range(excel_data.shape[0]):
            for j in range(excel_data.shape[1]):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(excel_data.iloc[i, j])))

        # Ana pencere düzeni
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
