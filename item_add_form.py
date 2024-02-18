# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 01:42:11 2022
@author: Najeeb Ur Rehmab, Assistant Porfessor, University of Gujrat
"""

from PyQt6.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
    QDateEdit,
    QPushButton,
    #QPlainTextDocumentLayout,
    #QTextDocument,
)
from mysql_connectivity import *

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit



class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QFormLayout()

        self.name = QLineEdit()
        self.price = QSpinBox( minimum=0, maximum=1000)
        self.message = QLabel()
        self.message.setText("")
        self.save = QPushButton("Save")
        self.save.setToolTip('This is a <b>QPushButton</b> widget. <br>Click Here to Calculate')
        
        layout.addRow("Item Name",self.name)
        layout.addRow("Item Price 2",self.price)
        layout.addRow(self.message)

        '''
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Age:", QLineEdit())
        layout.addRow("Job:", QLineEdit())
        layout.addRow("Hobbies:", QLineEdit())
        '''

        #QSpinBox(form, minimum=18, maximum=67)

        
        layout.addRow(self.save)
        
        self.save.clicked.connect(self.testClick)
        self.setLayout(layout)
        
    def testClick(self):
            print(self.name.text())
            print(self.price.text())

            a = self.save.text()
            b = int(self.price.text())

            #sum = a + b
            #print("Sum is ",sum)
            
            #text = str(sum) + " = " + str(a) +" + " + str(b)
            
            #self.message.setText(text)
            #calc.setText("Press to clear")
            q = insertQuery(self.name.text(),self.price.text())
            print(q)
            mycursor.execute(q)
            print(mycursor.rowcount, "Record Inserted(s)")
            text = str(mycursor.rowcount) + " - Record Inserted(s)"
            self.message.setText(text)
            mydb.commit()




            
application = QApplication([])
mainWindwo = MyMainWindow()
mainWindwo.show()
application.exec()