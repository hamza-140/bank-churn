import csv
import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, \
    QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QInputDialog
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

        # create a QTableWidget with 3 rows and 2 columns
        tableWidget = QTableWidget(self)
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(2)

        # set the header labels for the existing columns
        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Column 1"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Column 2"))

        # insert a new column at the second index
        tableWidget.insertColumn(1)
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Column 3"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())