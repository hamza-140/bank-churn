""" MADE BY SYED ALI HAMZA SHAH 20021519-140 SECTION C """
import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Paint(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)  # set window size and position

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(Qt.GlobalColor.red)
        qp.drawLine(50, 100, 50, 175)
        qp.drawLine(50, 175, 150, 175)
        # qp.drawLine(150, 175, 180, 150)
        # qp.drawLine(180, 150, 180, 70)
        # qp.drawLine(150, 175, 150, 100)
        # qp.drawLine(150, 100, 50, 100)
        # qp.drawLine(150, 100, 180, 70)
        # qp.drawLine(50, 100, 100, 50)
        # qp.drawLine(150, 100, 100, 50)
        # qp.drawLine(100, 50, 130, 20)
        # qp.drawLine(130, 20, 180, 70)
        # qp.drawEllipse(70, 110, 60, 60)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(Qt.GlobalColor.red)
        qp.setPen(pen)
        font = QtGui.QFont()
        font.setFamily('Serif')
        font.setBold(True)
        font.setPointSize(40)
        qp.setFont(font)
        qp.drawText(50, 300, 'HAPPY QUIZ!')
        qp.end()


if __name__ == '__main__':
    app = QApplication([])
    window = Paint()
    window.show()
    sys.exit(app.exec())
