"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                     IMPORTS            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import csv
import sqlite3
import sys
import pandas as pd
from PyQt6.QtCharts import QChartView, QChart, QPieSlice, QPieSeries
from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                     MAIN WINDOW            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class MyMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Bank Churner Prediction")
        self.window = None
        self.setWindowIcon(QIcon('icon.png'))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                               TABLE            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        df = pd.read_csv('BankChurners.csv')
        customers = df.to_dict('records')
        self.table = QTableWidget(self)
        header = self.table.horizontalHeader()
        vertical = self.table.verticalHeader()
        self.table.setColumnCount(20)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(customers[0].keys())
        self.table.setRowCount(len(customers))
        column_names = []
        for i in customers[0].keys():
            column_names.append(i)
        row = 0
        for e in customers:
            [self.table.setItem(row, i, QTableWidgetItem(str(e['{0}'.format(column_names[i])]))) for i in range(20)]
            row += 1
        self.setCentralWidget(self.table)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             STYLESHEET            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.table.setStyleSheet("color:white;background-color:#373833")
        vertical.setStyleSheet("QHeaderView::section { color: #71B914;background-color: #262927; }")
        header.setStyleSheet(
            "QHeaderView::section {color: #71B914;background-color: #262927;border: 1px solid #71B914;font-weight:bold; }")

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             MAIN DOCK            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.dock = QDockWidget('Bank Churner System')
        self.dock.setStyleSheet("color:white;font-weight:bold;background-color:#262927")
        self.dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock)
        form = QWidget(self)
        layout = QFormLayout(form)
        form.setLayout(layout)
        self.dock.setWidget(form)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             TOOL BAR            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        toolbar = QToolBar('TOOLBAR')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        add_action = QAction(QIcon('./add.png'), '&Add', self)
        add_action.triggered.connect(self.add_dock)
        add_action.triggered.connect(self.dock.close)
        toolbar.addAction(add_action)
        delete_action = QAction(QIcon('delete.png'), '&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)

        edit_action = QAction(QIcon('edit.png'), '&Edit', self)
        edit_action.triggered.connect(self.edit_employee)
        toolbar.addAction(edit_action)

        search_action = QAction(QIcon('search.png'), '&Search', self)
        search_action.triggered.connect(self.search)
        toolbar.addAction(search_action)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             ADD BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        btn_add = QPushButton('ADD')
        btn_add.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        btn_add.setStyleSheet("color: #71B914;\n"
                              "border-radius: 8px;\n"
                              "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        btn_add.clicked.connect(self.add_dock)
        btn_add.clicked.connect(self.dock.close)
        btn_add.setFixedSize(212, 50)
        layout.addRow(btn_add)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             DELETE BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        delete_button = QPushButton('DELETE', form)
        delete_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        delete_button.setStyleSheet("color: #71B914;\n"
                                    "border-radius: 8px;\n"
                                    "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        delete_button.setFixedSize(212, 50)
        delete_button.clicked.connect(self.delete)
        layout.addRow(delete_button)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             EDIT BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        edit_button = QPushButton('EDIT', form)
        edit_button.clicked.connect(self.edit_employee)
        edit_button.setFixedSize(212, 50)
        edit_button.clicked.connect(self.dock.close)
        edit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        edit_button.setStyleSheet("color: #71B914;\n"
                                  "border-radius: 8px;\n"
                                  "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        layout.addRow(edit_button)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             SEARCH BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        search_button = QPushButton('SEARCH', form)
        search_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        search_button.setStyleSheet("color: #71B914;\n"
                                    "border-radius: 8px;\n"
                                    "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        search_button.setFixedSize(212, 50)
        search_button.clicked.connect(self.search)
        layout.addRow(search_button)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             CHART BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        chart = QPushButton('CHART', form)
        chart.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        chart.setStyleSheet("color: #71B914;\n"
                            "border-radius: 8px;\n"
                            "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        chart.setFixedSize(212, 50)
        chart.clicked.connect(self.bar_window)
        layout.addRow(chart)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            LIST WIDGET BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        list_w = QPushButton('LIST WIDGET', form)
        list_w.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        list_w.setStyleSheet("color: #71B914;\n"
                             "border-radius: 8px;\n"
                             "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        list_w.setFixedSize(212, 50)
        list_w.clicked.connect(self.list_widget)
        layout.addRow(list_w)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            PREDICTION BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        predict_btn = QPushButton('PREDICT', form)
        predict_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        predict_btn.setStyleSheet("color: #71B914;\n"
                             "border-radius: 8px;\n"
                             "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        predict_btn.setFixedSize(212, 50)
        predict_btn.clicked.connect(self.prediction)
        layout.addRow(predict_btn)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             EXIT BUTTON            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        exit_btn = QPushButton('EXIT', form)
        exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        exit_btn.setStyleSheet("color: #71B914;\n"
                               "border-radius: 8px;\n"
                               "background-color: #262927;border: 1px solid #71B914;font-weight:bold")
        exit_btn.setFixedSize(212, 50)
        exit_btn.clicked.connect(self.close)
        layout.addRow(exit_btn)

    def list_widget(self):
        self.window = ListWidget()
        self.window.show()

    def bar_window(self):
        self.window = BarChartWindow('BankChurners.csv', 'Gender')
        self.window.show()

    def prediction(self):
        self.window = PredictionWindow()
        # self.window.showMaximized()
        self.window.show()

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         SEARCH FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def search(self):
        search_text, ok = QInputDialog.getText(self, 'Search', 'Enter search text:')
        if ok:
            for row in range(self.table.rowCount()):
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    # print(item.text())
                    if item and search_text in item.text():
                        self.table.setRowHidden(row, False)
                        break
                    else:
                        self.table.setRowHidden(row, True)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         EDIT FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def edit_employee(self):
        self.current_row = self.table.currentRow()
        if self.current_row < 0:
            return QMessageBox.warning(self, 'Warning', 'Please select a record to edit')

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)
        self.client_num_update = QLineEdit(self.table.item(self.current_row, 0).text(), form)
        self.customer_age_update = QSpinBox(form, minimum=18, maximum=67)
        self.customer_age_update.setValue(int(self.table.item(self.current_row, 1).text()))
        self.gender_update = QComboBox(form)
        self.gender_update.addItems(["M", "F"])
        self.gender_update.setPlaceholderText("Choose Gender")
        self.gender_update.setCurrentText(self.table.item(self.current_row, 2).text())
        self.Dependent_count_update = QSpinBox(form)
        self.Dependent_count_update.setValue(int(float(self.table.item(self.current_row, 3).text())))
        self.Education_Level_update = QComboBox(form)
        self.Education_Level_update.addItems(["Graduate", "Doctorate", "College", "Uneducated", "High School"])
        self.Education_Level_update.setPlaceholderText('Choose Qualification')
        self.Education_Level_update.setCurrentText(self.table.item(self.current_row, 4).text())
        self.Martial_Status_update = QComboBox(form)
        self.Martial_Status_update.addItems(["Married", "Single", "Divorced"])
        self.Martial_Status_update.setPlaceholderText('Choose Martial Status')
        self.Martial_Status_update.setCurrentText(self.table.item(self.current_row, 5).text())
        self.Income_Category_box_update = QComboBox(form)
        self.Income_Category_box_update.addItems(['Less than $40k', '$40k - $80k', '$80k - $120k', '$120k+'])
        self.Income_Category_box_update.setPlaceholderText('Choose Income Category')
        self.Income_Category_box_update.setCurrentText(self.table.item(self.current_row, 6).text())
        self.card_update = QComboBox(form)
        self.card_update.addItems(['Platinum', 'Gold', 'Silver', 'Blue'])
        self.card_update.setPlaceholderText('Choose Card Catagory')
        self.card_update.setCurrentText(self.table.item(self.current_row, 7).text())
        self.months_update = QSpinBox(form)
        self.months_update.setValue(int(float(self.table.item(self.current_row, 8).text())))
        self.relation_update = QSpinBox(form)
        self.relation_update.setValue(int(float(self.table.item(self.current_row, 9).text())))
        self.inactive_update = QSpinBox(form)
        self.inactive_update.setValue(int(float(self.table.item(self.current_row, 10).text())))
        self.active_update = QSpinBox(form)
        self.active_update.setValue(int(float(self.table.item(self.current_row, 11).text())))
        self.credit_limit_update = QLineEdit(form)
        self.credit_limit_update.setText(self.table.item(self.current_row, 12).text())
        self.credit_limit_update.setValidator(QIntValidator())
        self.credit_limit_update.setMaxLength(6)
        self.Total_Revolving_Bal_update = QLineEdit(form)
        self.Total_Revolving_Bal_update.setValidator(QIntValidator())
        self.Total_Revolving_Bal_update.setText(self.table.item(self.current_row, 13).text())
        self.open_Bal_update = QLineEdit(form)
        self.open_Bal_update.setValidator(QIntValidator())
        # self.open_Bal_update.setMaxLength(6)
        self.open_Bal_update.setText(self.table.item(self.current_row, 14).text())
        self.total_amtQ4toQ1_update = QLineEdit(form)
        self.total_amtQ4toQ1_update.setValidator(QDoubleValidator(0.99, 1.99, 2))
        # self.total_amtQ4toQ1_update.setMaxLength(3)
        self.total_amtQ4toQ1_update.setText(self.table.item(self.current_row, 15).text())
        self.total_transc_amt_update = QLineEdit(form)
        self.total_transc_amt_update.setValidator(QIntValidator())
        # self.total_transc_amt_update.setMaxLength(6)
        self.total_transc_amt_update.setText(self.table.item(self.current_row, 16).text())
        self.total_transc_count_update = QSpinBox(form)
        self.total_transc_count_update.setValue(int(float(self.table.item(self.current_row, 17).text())))
        self.total_countQ4toQ1_update = QLineEdit(form)
        self.total_countQ4toQ1_update.setValidator(QDoubleValidator(0.99, 1.99, 2))
        # self.total_countQ4toQ1_update.setMaxLength(3)
        self.total_countQ4toQ1_update.setText((self.table.item(self.current_row, 18).text()))
        self.utilization_update = QLineEdit(form)
        self.utilization_update.setValidator(QDoubleValidator(0.000, 0.999, 4))
        self.utilization_update.setText(self.table.item(self.current_row, 19).text())

        layout.addRow("Client No. : ", self.client_num_update)
        layout.addRow("Customer Age : ", self.customer_age_update)
        layout.addRow("Gender : ", self.gender_update)
        layout.addRow("Dependents : ", self.Dependent_count_update)
        layout.addRow("Education : ", self.Education_Level_update)
        layout.addRow("Martial Status : ", self.Martial_Status_update)
        layout.addRow("Income Category ", self.Income_Category_box_update)
        layout.addRow("Card Category ", self.card_update)
        layout.addRow("Duration ", self.months_update)
        layout.addRow('Products Relation:', self.relation_update)
        layout.addRow('InActive Months :', self.inactive_update)
        layout.addRow('No. of Contacts :', self.active_update)
        layout.addRow('Credit Limit : ', self.credit_limit_update)
        layout.addRow('Total Revolving Balance :', self.Total_Revolving_Bal_update)
        layout.addRow('Avg Open to Buy Balance :', self.open_Bal_update)
        layout.addRow('Total Amount Q4 to Q1 :', self.total_amtQ4toQ1_update)
        layout.addRow('Total Trans Amount :', self.total_transc_amt_update)
        layout.addRow('Total Trans Count :', self.total_transc_count_update)
        layout.addRow('Total Count Q4 to Q1 :', self.total_countQ4toQ1_update)
        layout.addRow("Avg Utilization Ratio :", self.utilization_update)

        btn_update = QPushButton('Update', self)
        btn_update.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "border-radius: 8px;\n"
                                 "background-color: 	#5bc0de;")
        btn_update.setFixedSize(285, 50)
        self.lable = QLabel(" ")
        self.lable.setStyleSheet("padding-top : 10px;")
        layout.addRow(self.lable)
        layout.addRow(btn_update)
        btn_update.clicked.connect(lambda: self.update_employee(self.current_row))
        btn_cancel = QPushButton('Cancel', self)
        btn_cancel.setFixedSize(285, 50)
        btn_cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "border-radius: 8px;\n"
                                 "background-color: 	#5bc0de;")
        layout.addRow(btn_cancel)
        self.edit_dock = QDockWidget('Edit Customer')
        self.scroll = QScrollBar()
        self.edit_dock.setWidget(self.scroll)
        self.edit_dock.setObjectName('Edit Customer')
        self.edit_dock.setStyleSheet("color:white")
        self.edit_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.edit_dock)
        self.edit_dock.setWidget(form)
        btn_cancel.clicked.connect(self.edit_dock.close)
        btn_cancel.clicked.connect(self.dock.show)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         UPDATE FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def update_employee(self, row):
        self.table.setItem(row, 0, QTableWidgetItem(self.client_num_update.text()))
        self.table.setItem(row, 1, QTableWidgetItem(self.customer_age_update.text()))
        self.table.setItem(row, 2, QTableWidgetItem(self.gender_update.currentText()))
        self.table.setItem(row, 3, QTableWidgetItem(self.Dependent_count_update.text()))
        self.table.setItem(row, 4, QTableWidgetItem(self.Education_Level_update.currentText()))
        self.table.setItem(row, 5, QTableWidgetItem(self.Martial_Status_update.currentText()))
        self.table.setItem(row, 6, QTableWidgetItem(self.Income_Category_box_update.currentText()))
        self.table.setItem(row, 7, QTableWidgetItem(self.card_update.currentText()))
        self.table.setItem(row, 8, QTableWidgetItem(self.months_update.text()))
        self.table.setItem(row, 9, QTableWidgetItem(self.relation_update.text()))
        self.table.setItem(row, 10, QTableWidgetItem(self.inactive_update.text()))
        self.table.setItem(row, 11, QTableWidgetItem(self.active_update.text()))
        self.table.setItem(row, 12, QTableWidgetItem(self.credit_limit_update.text()))
        self.table.setItem(row, 13, QTableWidgetItem(self.Total_Revolving_Bal_update.text()))
        self.table.setItem(row, 14, QTableWidgetItem(self.open_Bal_update.text()))
        self.table.setItem(row, 15, QTableWidgetItem(self.total_amtQ4toQ1_update.text()))
        self.table.setItem(row, 16, QTableWidgetItem(self.total_transc_amt_update.text()))
        self.table.setItem(row, 17, QTableWidgetItem(self.total_transc_count_update.text()))
        self.table.setItem(row, 18, QTableWidgetItem(self.total_countQ4toQ1_update.text()))
        self.table.setItem(row, 19, QTableWidgetItem(self.utilization_update.text()))
        self.save()
        self.save_DB()
        self.edit_dock.close()
        self.dock.show()

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         DELETE FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def delete(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Warning', 'Please select a record to delete')

        button = QMessageBox.question(
            self,
            'Confirmation',
            'Are you sure that you want to delete the selected row?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        button.setStyleSheet("QMessageBox { background-color: %s }" % QColor(255,255,255).name())
        # self.setStyleSheet("QMessageBox {color:red;}")
        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)
            self.save()
            self.save_DB()

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         VALID FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def valid(self):
        CLIENTNUM = self.CLIENTNUM.text().strip()
        Custormer_Age = self.Custormer_Age.text().strip()

        if not CLIENTNUM:
            QMessageBox.critical(self, 'Error', 'Please enter the Client Number')
            self.CLIENTNUM.setFocus()
            return False

        if not Custormer_Age:
            QMessageBox.critical(self, 'Error', 'Please enter the Age')
            self.Custormer_Age.setFocus()
            return False

        try:
            age = int(self.Custormer_Age.text().strip())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter a valid age')
            self.Custormer_Age.setFocus()
            return False

        if age <= 0 or age >= 67:
            QMessageBox.critical(
                self, 'Error', 'The valid age is between 1 and 67')
            return False

        return True

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         SAVE FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def save(self):
        with open('BankChurners.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header row
            header_row = []
            for column in range(self.table.columnCount()):
                header_row.append(self.table.horizontalHeaderItem(column).text())
            writer.writerow(header_row)

            # Write the data rows
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         SAVE DATABASE FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def save_DB(self):
        # connect to the database
        conn = sqlite3.connect('Banklogin.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE RECORDS')

        # create a new table called 'bank_data'
        cursor.execute('''CREATE TABLE RECORDS
                         (CLIENTNUM TEXT, Customer_Age INTEGER, Gender TEXT,
                          Dependent_count INTEGER, Education_Level TEXT, Marital_Status TEXT,
                          Income_Category TEXT, Card_Category TEXT, Months_on_book INTEGER,
                          Total_Relationship_Count INTEGER, Months_Inactive_12_mon INTEGER,
                          Contacts_Count_12_mon INTEGER, Credit_Limit REAL, Total_Revolving_Bal INTEGER,
                          Avg_Open_To_Buy REAL, Total_Amt_Chng_Q4_Q1 REAL, Total_Trans_Amt INTEGER,
                          Total_Trans_Ct INTEGER, Total_Ct_Chng_Q4_Q1 REAL, Avg_Utilization_Ratio REAL)''')

        # open the CSV file and insert the data into the 'bank_data' table
        with open('BankChurners.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip header row
            for row in reader:
                cursor.execute('''INSERT INTO RECORDS
                                  (CLIENTNUM, Customer_Age, Gender,
                                   Dependent_count, Education_Level, Marital_Status,
                                   Income_Category, Card_Category, Months_on_book,
                                   Total_Relationship_Count, Months_Inactive_12_mon,
                                   Contacts_Count_12_mon, Credit_Limit, Total_Revolving_Bal,
                                   Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt,
                                   Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)

        # commit changes and close connection
        conn.commit()
        conn.close()

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         ADD FORM            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def add_dock(self):
        self.new_dock = QDockWidget('New Customer')
        self.new_dock.setStyleSheet('color:white')
        self.new_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.new_dock)

        form = QWidget(self)
        layout = QFormLayout(form)
        form.setLayout(layout)
        self.CLIENTNUM = QLineEdit(form)
        self.CLIENTNUM.setValidator(QIntValidator())
        self.CLIENTNUM.setMaxLength(9)
        self.Gender = QComboBox(form)
        self.Gender.addItems(["M", "F"])
        self.Gender.setPlaceholderText("Choose Gender")
        self.Gender.setCurrentIndex(-1)
        self.Custormer_Age = QSpinBox(form, minimum=18, maximum=67)
        # self.Custormer_Age.setValue()
        self.Dependent_count = QSpinBox(form)
        self.Dependent_count.clear()
        self.Education_Level = QComboBox(form)
        self.Education_Level.addItems(["Graduate", "Doctorate", "College", "Uneducated", "High School"])
        self.Education_Level.setPlaceholderText('Choose Qualification')
        self.Education_Level.setCurrentIndex(-1)
        self.Martial_Status = QComboBox(form)
        self.Martial_Status.addItems(["Married", "Single", "Divorced"])
        self.Martial_Status.setPlaceholderText('Choose Martial Status')
        self.Martial_Status.setCurrentIndex(-1)
        self.Income = QLineEdit(form)
        self.Income.setValidator(QIntValidator())
        self.Income.returnPressed.connect(self.category)
        self.Income_Category = "Less than $40K"
        self.Income_Category_box = QLineEdit()
        self.Income_Category_box.setText(self.Income_Category)
        self.Income_Category_box.setReadOnly(True)
        self.card = QLineEdit()
        self.card_category = "Blue"
        self.card.setText(self.card_category)
        self.card.setReadOnly(True)
        self.months = QSpinBox(form)
        self.months.clear()
        self.relation = QSpinBox(form)
        self.relation.clear()
        self.inactive = QSpinBox(form)
        self.inactive.clear()
        self.active = QSpinBox(form)
        self.active.clear()
        self.credit_limit = QLineEdit(form)
        self.credit_limit.setValidator(QIntValidator())
        self.credit_limit.setMaxLength(6)
        self.Total_Revolving_Bal = QLineEdit(form)
        self.Total_Revolving_Bal.setValidator(QIntValidator())
        self.Total_Revolving_Bal.setMaxLength(6)
        self.open_Bal = QLineEdit(form)
        self.open_Bal.setValidator(QIntValidator())
        self.open_Bal.setMaxLength(6)
        self.total_amtQ4toQ1 = QLineEdit(form)
        self.total_amtQ4toQ1.setValidator(QDoubleValidator(0.99, 1.99, 2))
        self.total_amtQ4toQ1.setMaxLength(3)
        self.total_transc_amt = QLineEdit(form)
        self.total_transc_amt.setValidator(QIntValidator())
        self.total_transc_amt.setMaxLength(6)
        self.total_transc_count = QSpinBox(form)
        self.total_countQ4toQ1 = QLineEdit(form)
        self.total_countQ4toQ1.setValidator(QDoubleValidator(0.99, 1.99, 2))
        self.total_countQ4toQ1.setMaxLength(3)
        self.utilization = QLineEdit(form)
        self.utilization.setValidator(QDoubleValidator(0.000, 0.999, 4))

        layout.addRow('Client No:', self.CLIENTNUM)
        layout.addRow('Customer Age:', self.Custormer_Age)
        layout.addRow('Gender:', self.Gender)
        layout.addRow('No. of Dependents :', self.Dependent_count)
        layout.addRow('Education : ', self.Education_Level)
        layout.addRow('Martial Status :', self.Martial_Status)
        layout.addRow('Income :', self.Income)
        layout.addRow('Income Category : ', self.Income_Category_box)
        layout.addRow('Card Category', self.card)
        layout.addRow('Duration :', self.months)
        layout.addRow('Products Relation:', self.relation)
        layout.addRow('InActive Months :', self.inactive)
        layout.addRow('No. of Contacts :', self.active)
        layout.addRow('Credit Limit : ', self.credit_limit)
        layout.addRow('Total Revolving Balance :', self.Total_Revolving_Bal)
        layout.addRow('Avg Open to Buy Balance :', self.open_Bal)
        layout.addRow('Total Amount Q4 to Q1 :', self.total_amtQ4toQ1)
        layout.addRow('Total Trans Amount :', self.total_transc_amt)
        layout.addRow('Total Trans Count :', self.total_transc_count)
        layout.addRow('Total Count Q4 to Q1 :', self.total_countQ4toQ1)
        layout.addRow("Avg Utilization Ratio :", self.utilization)

        btn_add = QPushButton('Add')
        btn_add.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        btn_add.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "border-radius: 8px;\n"
                              "background-color: 	#5bc0de;")
        btn_add.setFixedSize(285, 50)
        cancel = QPushButton('Cancel')
        cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
                             "border-radius: 8px;\n"
                             "background-color: 	#5bc0de;")
        cancel.setFixedSize(285, 50)
        self.lable = QLabel(" ")
        self.lable.setStyleSheet("padding-top : 10px;")
        layout.addRow(self.lable)
        layout.addRow(btn_add)
        layout.addRow(cancel)
        btn_add.clicked.connect(self.add_employee)
        btn_add.clicked.connect(self.new_dock.close)
        cancel.clicked.connect(self.new_dock.close)
        btn_add.clicked.connect(self.dock.show)
        cancel.clicked.connect(self.dock.show)
        self.new_dock.setWidget(form)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         CARD CATEGORY FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def category(self):
        if int(self.Income.text()) >= 120000:
            self.Income_Category_box.setText("$120K +")
            self.card.setText("Platinum")
        elif int(self.Income.text()) < 120000 and int(self.Income.text()) > 80000:
            self.Income_Category_box.setText("$80K - $120K")
            self.card.setText("Gold")
        elif int(self.Income.text()) < 80000 and int(self.Income.text()) > 40000:
            self.Income_Category_box.setText("$40K - $80K")
            self.card.setText("Silver")
        else:
            self.Income_Category_box.setText("Less than $40K")
            self.card.setText("Blue")

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         ADD FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def add_employee(self):
        if not self.valid():
            return
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.CLIENTNUM.text()))
        self.table.setItem(row, 1, QTableWidgetItem(self.Custormer_Age.text()))
        self.table.setItem(row, 2, QTableWidgetItem(self.Gender.currentText()))
        self.table.setItem(row, 3, QTableWidgetItem(self.Dependent_count.text()))
        self.table.setItem(row, 4, QTableWidgetItem(self.Education_Level.currentText()))
        self.table.setItem(row, 5, QTableWidgetItem(self.Martial_Status.currentText()))
        self.table.setItem(row, 6, QTableWidgetItem(self.Income_Category_box.text()))
        self.table.setItem(row, 7, QTableWidgetItem(self.card.text()))
        self.table.setItem(row, 8, QTableWidgetItem(self.months.text()))
        self.table.setItem(row, 9, QTableWidgetItem(self.relation.text()))
        self.table.setItem(row, 10, QTableWidgetItem(self.inactive.text()))
        self.table.setItem(row, 11, QTableWidgetItem(self.active.text()))
        self.table.setItem(row, 12, QTableWidgetItem(self.credit_limit.text()))
        self.table.setItem(row, 13, QTableWidgetItem(self.Total_Revolving_Bal.text()))
        self.table.setItem(row, 14, QTableWidgetItem(self.open_Bal.text()))
        self.table.setItem(row, 15, QTableWidgetItem(self.total_amtQ4toQ1.text()))
        self.table.setItem(row, 16, QTableWidgetItem(self.total_transc_amt.text()))
        self.table.setItem(row, 17, QTableWidgetItem(self.total_transc_count.text()))
        self.table.setItem(row, 18, QTableWidgetItem(self.total_countQ4toQ1.text()))
        self.table.setItem(row, 19, QTableWidgetItem(self.utilization.text()))
        self.save()
        self.save_DB()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         LIST WIDGET CLASS            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class ListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(18, 35, 46);color:white;")
        self.resize(820, 602)
        layout = QVBoxLayout(self)
        self.box = QLineEdit(self)
        self.labels = ["CLIENTNUM : ", "Customer_Age : ", "Gender : ",
                       "Dependent_count : ", "Education_Level : ", "Marital_Status : ",
                       "Income_Category", "Card_Category", "Months_on_book",
                       "Total_Relationship_Count", "Months_Inactive_12_mon",
                       "Contacts_Count_12_mon", "Credit_Limit", "Total_Revolving_Bal",
                       "Avg_Open_To_Buy", "Total_Amt_Chng_Q4_Q1", "Total_Trans_Amt",
                       "Total_Trans_Ct", "Total_Ct_Chng_Q4_Q1", "Avg_Utilization_Ratio "]
        self.listwidget = QListWidget(self)
        layout.addWidget(self.listwidget)
        self.box.setStyleSheet("background-color:white;color:rgb(18, 35, 46)")
        layout.addWidget(self.box)
        btn = QPushButton("SEARCH FROM DATABASE")
        btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                          "border-radius: 8px;\n"
                          "background-color: rgb(32, 54, 71);")
        btn.setFixedSize(212, 50)
        layout.addWidget(btn)
        btn.clicked.connect(self.db)
        # add the record to the listwidget
        self.setLayout(layout)

    def db(self):
        self.listwidget.clear()
        conn = sqlite3.connect('Banklogin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM RECORDS WHERE CLIENTNUM={0}'.format(self.box.text()))
        record = cursor.fetchone()
        conn.close()
        print(len(record))
        print(len(self.labels))
        for i in range(len(record)):
            print(str(record[i]))
            item = QListWidgetItem(self.labels[i] + str(record[i]))
            self.listwidget.addItem(item)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         CHART CLASS            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class BarChartWindow(QWidget):
    def __init__(self, csv_file, column_name):
        super().__init__()
        self.setWindowTitle('Chart')
        self.csv_file = csv_file
        self.setWindowIcon(QIcon('icon.png'))
        self.column_name = column_name
        self.setStyleSheet("background-color: rgb(18, 35, 46);")
        self.create_bar_chart()

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         GENDER FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def create_bar_chart(self):
        # Read the CSV file
        with open(self.csv_file, newline='') as file:
            reader = csv.DictReader(file)
            data = [row[self.column_name] for row in reader]

        # Count the number of males and females
        counts = {'Male': 0, 'Female': 0}
        for gender in data:
            if gender == 'M':
                counts['Male'] += 1
            elif gender == 'F':
                counts['Female'] += 1

        # Create a bar chart
        series = QPieSeries()
        series.append("Male", counts['Male'])
        series.append("Female", counts['Female'])

        # adding slice
        slice = QPieSlice()
        slice = series.slices()[1]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        # slice.setPen(QPen(Qt.GlobalColor.red, 2))
        slice.setBrush(Qt.GlobalColor.blue)

        chart = QChart()
        chart.setBackgroundBrush(qRgb(18, 35, 46))
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        # chart.setAnimationOptions(QChart.animationOptions(QChart.SeriesAnimations))
        chart.setTitle("Gender Comparison")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        chartview = QChartView(chart)
        # chartview.setRenderHint(QPainter.Antialiasing)

        # Set up the main window and add the chart view to it
        layout = QVBoxLayout(self)
        layout.addWidget(chartview)
        label = QLabel("Female: {0}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMale: {1}".format(counts['Female'], counts['Male']))
        label.setStyleSheet("color:blue")
        layout.addWidget(label)
        self.resize(800, 600)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                ADD FORM CLASS            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class PedictForm(QMainWindow):
    def __init__(self):
        super().__init__()
        form = QWidget(self)
        layout = QFormLayout(form)
        form.setLayout(layout)
        self.Custormer_Age = QSpinBox(form, minimum=18, maximum=67)
        self.Dependent_count = QSpinBox(form)
        self.months = QSpinBox(form)
        self.relation = QSpinBox(form)
        self.inactive = QSpinBox(form)
        self.active = QSpinBox(form)
        self.credit_limit = QLineEdit(form)
        self.credit_limit.setValidator(QIntValidator())
        self.credit_limit.setMaxLength(8)
        self.Total_Revolving_Bal = QLineEdit(form)
        self.Total_Revolving_Bal.setValidator(QIntValidator())
        self.Total_Revolving_Bal.setMaxLength(8)
        self.open_Bal = QLineEdit(form)
        self.open_Bal.setValidator(QIntValidator())
        self.open_Bal.setMaxLength(8)
        self.total_amtQ4toQ1 = QLineEdit(form)
        self.total_amtQ4toQ1.setValidator(QDoubleValidator(0.01, 9.99, 3))
        self.total_amtQ4toQ1.setMaxLength(5)
        self.total_transc_amt = QLineEdit(form)
        self.total_transc_amt.setValidator(QIntValidator())
        self.total_transc_amt.setMaxLength(6)
        self.total_transc_count = QSpinBox(form)
        self.total_countQ4toQ1 = QLineEdit(form)
        self.total_countQ4toQ1.setValidator(QDoubleValidator(0.01, 9.99, 3))
        self.total_countQ4toQ1.setMaxLength(3)
        self.utilization = QLineEdit(form)
        self.utilization.setValidator(QDoubleValidator(0.000, 0.999, 4))
        layout.addRow('Customer Age:', self.Custormer_Age)
        layout.addRow('No. of Dependents :', self.Dependent_count)
        # layout.addRow('Martial Status :', self.Martial_Status
        # layout.addRow('Income :', self.Income)
        # layout.addRow('Income Category : ', self.Income_Category_box)
        # layout.addRow('Card Category', self.card)
        layout.addRow('Duration :', self.months)
        layout.addRow('Products Relation:', self.relation)
        layout.addRow('InActive Months :', self.inactive)
        layout.addRow('No. of Contacts :', self.active)
        layout.addRow('Credit Limit : ', self.credit_limit)
        layout.addRow('Total Revolving Balance :', self.Total_Revolving_Bal)
        layout.addRow('Avg Open to Buy Balance :', self.open_Bal)
        layout.addRow('Total Amount Q4 to Q1 :', self.total_amtQ4toQ1)
        layout.addRow('Total Trans Amount :', self.total_transc_amt)
        layout.addRow('Total Trans Count :', self.total_transc_count)
        layout.addRow('Total Count Q4 to Q1 :', self.total_countQ4toQ1)
        layout.addRow("Avg Utilization Ratio :", self.utilization)

        btn_add = QPushButton('PREDICT')
        btn_add.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        btn_add.setStyleSheet("color: rgb(255, 255, 255);\n"
                              "border-radius: 8px;\n"
                              "background-color: 	#5bc0de;")
        btn_add.setFixedSize(285, 50)
        cancel = QPushButton('Cancel')
        cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
                             "border-radius: 8px;\n"
                             "background-color: 	#5bc0de;")
        cancel.setFixedSize(285, 50)
        self.lable = QLabel(" ")
        self.lable.setStyleSheet("padding-top : 10px;")
        layout.addRow(self.lable)
        layout.addRow(btn_add)
        layout.addRow(cancel)
        btn_add.clicked.connect(self.result)
        cancel.clicked.connect(self.close)
        self.setCentralWidget(form)

    def result(self):
        import numpy as np
        import pandas as pd
        from xgboost import XGBClassifier

        from ml import scaler, req_cols

        model = XGBClassifier()
        model.load_model('model_file.bin')
        # Creating dummy data
        dummy_data = np.array([[int(self.Custormer_Age.text()), int(self.Dependent_count.text()), int(self.months.text()), self.relation, self.inactive, self.active, self.credit_limit,self.Total_Revolving_Bal,self.open_Bal,self.total_amtQ4toQ1, self.total_transc_amt, self.total_countQ4toQ1, self.total_transc_count,self.utilization]])
        # dummy_data = np.array([[10, 1, 10, 4, 2, 3, 1000, 1000, 1000, 0.8, 4000, 40, 0.5, 0.3]])
        # Scaling the dummy data
        dummy_data_scaled = scaler.transform(dummy_data[:, :len(req_cols)])

        # Converting it to a DataFrame
        dummy_df = pd.DataFrame(dummy_data_scaled, columns=req_cols)

        # Creating dummy columns for categorical variables (if any)
        # Here, we don't have any categorical columns, so no dummy columns are created

        # Predicting the target variable using the trained model
        prediction = model.predict(dummy_df)
        if int(prediction) == 0:
            self.lable.setText('Trustable Customer')
        else:
            self.lable.setText('Churn Customer')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                LIST WIDGET PREDICTION CLASS            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class LISTWIDGETPREDICTION(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(18, 35, 46);color:white;")
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('List Widget')
        self.resize(820, 602)
        layout = QVBoxLayout(self)
        self.box = QLineEdit(self)
        self.labels = ["CLIENTNUM : ","Attrition Flag : ", "Customer_Age : ", "Gender : ",
                       "Dependent_count : ", "Education_Level : ", "Marital_Status : ",
                       "Income_Category : ", "Card_Category : ", "Months_on_book : ",
                       "Total_Relationship_Count : ", "Months_Inactive_12_mon : ",
                       "Contacts_Count_12_mon : ", "Credit_Limit : ", "Total_Revolving_Bal : ",
                       "Avg_Open_To_Buy : ", "Total_Amt_Chng_Q4_Q1 : ", "Total_Trans_Amt : ",
                       "Total_Trans_Ct : ", "Total_Ct_Chng_Q4_Q1 : ", "Avg_Utilization_Ratio : "]
        self.listwidget = QListWidget(self)
        layout.addWidget(self.listwidget)
        self.box.setStyleSheet("background-color:white;color:rgb(18, 35, 46)")
        layout.addWidget(self.box)
        btn = QPushButton("SEARCH FROM DATABASE")
        btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                          "border-radius: 8px;\n"
                          "background-color: rgb(32, 54, 71);")
        btn.setFixedSize(212, 50)
        layout.addWidget(btn)
        btn.clicked.connect(self.db)
        # add the record to the listwidget
        self.setLayout(layout)

    def db(self):
        self.listwidget.clear()
        conn = sqlite3.connect('Banklogin.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM PREDICTS WHERE CLIENTNUM={0}'.format(self.box.text()))
        record = cursor.fetchone()
        conn.close()
        print(len(record))
        print(len(self.labels))
        for i in range(len(record)):
            print(str(record[i]))
            item = QListWidgetItem(self.labels[i] + str(record[i]))
            self.listwidget.addItem(item)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         PREDICTION CLASS            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class PredictionWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.showMaximized()
        self.setWindowTitle("Bank Churner Prediction")
        self.window = None
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                               TABLE            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        df = pd.read_csv('BankChurners.csv')
        customers = df.to_dict('records')
        self.setObjectName("MainWindow")
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: rgb(38, 41, 39);\n"
                                   "color: rgb(255, 255, 255);")
        self.menuMain = QtWidgets.QMenu(parent=self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionSearch = QtGui.QAction(parent=self)
        self.actionSearch.setObjectName("actionSearch")
        # self.actionPredict = QtGui.QAction(parent=self)
        # self.actionPredict.setObjectName("actionPredict")
        self.actionSearch.triggered.connect(self.save)
        self.actionSearch.triggered.connect(self.save_DB)
        self.actionSearch.triggered.connect(self.searchFlag)
        self.actionExit = QtGui.QAction(parent=self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.close)
        self.menuMain.addAction(self.actionSearch)
        self.menuMain.addSeparator()
        # self.menuMain.addAction(self.actionPredict)
        # self.actionPredict.triggered.connect(self.predict)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionExit)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi()


        self.table = QTableWidget(self)
        header = self.table.horizontalHeader()
        vertical = self.table.verticalHeader()
        self.table.setColumnCount(20)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(customers[0].keys())
        self.table.setRowCount(len(customers))
        column_names = []
        for i in customers[0].keys():
            column_names.append(i)
        row = 0
        for e in customers:
            [self.table.setItem(row, i, QTableWidgetItem(str(e['{0}'.format(column_names[i])]))) for i in range(20)]
            row += 1
        data = pd.read_csv('BankChurners.csv')
        import numpy as np
        # import pandas as pd
        from xgboost import XGBClassifier

        from ml import scaler, req_cols

        model = XGBClassifier()
        model.load_model('model_file.bin')
        req_cols = ['Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
                    'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
                    'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
                    'Total_Ct_Chng_Q4_Q1',
                    'Avg_Utilization_Ratio']
        predicts = []
        for j in range(len(data)):
            predicts.append(np.array([
                data['Customer_Age'][j],
                data['Dependent_count'][j],
                data['Months_on_book'][j],
                data['Total_Relationship_Count'][j],
                data['Months_Inactive_12_mon'][j],
                data['Contacts_Count_12_mon'][j],
                data['Credit_Limit'][j],
                data['Total_Revolving_Bal'][j],
                data['Avg_Open_To_Buy'][j],
                data['Total_Amt_Chng_Q4_Q1'][j],
                data['Total_Trans_Amt'][j],
                data['Total_Trans_Ct'][j],
                data['Total_Ct_Chng_Q4_Q1'][j],
                data['Avg_Utilization_Ratio'][j]
            ]))

        # Scaling the dummy data
        predicts_scaled = []
        for k in range(0, len(data)):
            predicts_scaled.append(scaler.transform(np.array(predicts[k]).reshape(1, -1)))

        predicts_df = []
        # Converting it to a DataFrame
        for i in range(0, len(data)):
            predicts_df.append(pd.DataFrame(predicts_scaled[i], columns=req_cols))

        self.prediction = []
        for i in range(0, len(data)):
            self.prediction.append(model.predict(predicts_df[i]))

        self.table.insertColumn(1)
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Attrition_Flag"))
        for i in range(0, len(data)):
            self.table.setItem(i, 1, QTableWidgetItem(str(self.prediction[i][0])))
        self.setCentralWidget(self.table)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             STYLESHEET            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        self.table.setStyleSheet("color:white;background-color:#373833")
        vertical.setStyleSheet("QHeaderView::section { color: #71B914;background-color: #262927; }")
        header.setStyleSheet(
            "QHeaderView::section {color: #71B914;background-color: #262927;border: 1px solid "
            "#71B914;font-weight:bold; }")

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                             MAIN DOCK            
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Prediction"))
        self.menuMain.setTitle(_translate("self", "Main"))
        self.actionSearch.setText(_translate("self", "Search"))
        # self.actionPredict.setText(_translate("self", "Predict"))
        self.actionExit.setText(_translate("self", "Exit"))

    def searchFlag(self):
        self.window = LISTWIDGETPREDICTION()
        self.window.show()

    def predict(self):
        self.window = PedictForm()
        self.window.show()

    def save(self):
        with open('BankChurnerPrediction1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header row
            header_row = []
            for column in range(self.table.columnCount()):
                header_row.append(self.table.horizontalHeaderItem(column).text())
            writer.writerow(header_row)

            # Write the data rows
            for row in range(self.table.rowCount()):
                row_data = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)

    def save_DB(self):
        # connect to the database
        conn = sqlite3.connect('Banklogin.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE PREDICTS')

        cursor.execute('''CREATE TABLE PREDICTS
                             (CLIENTNUM TEXT, Attrition_Flag INTEGER, Customer_Age INTEGER, Gender TEXT,
                              Dependent_count INTEGER, Education_Level TEXT, Marital_Status TEXT,
                              Income_Category TEXT, Card_Category TEXT, Months_on_book INTEGER,
                              Total_Relationship_Count INTEGER, Months_Inactive_12_mon INTEGER,
                              Contacts_Count_12_mon INTEGER, Credit_Limit REAL, Total_Revolving_Bal INTEGER,
                              Avg_Open_To_Buy REAL, Total_Amt_Chng_Q4_Q1 REAL, Total_Trans_Amt INTEGER,
                              Total_Trans_Ct INTEGER, Total_Ct_Chng_Q4_Q1 REAL, Avg_Utilization_Ratio REAL)''')

        # open the CSV file and insert the data into the 'bank_data' table
        with open('BankChurnerPrediction1.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip header row
            for row in reader:
                cursor.execute('''INSERT INTO PREDICTS
                                      (CLIENTNUM, Attrition_Flag, Customer_Age, Gender,
                                       Dependent_count, Education_Level, Marital_Status,
                                       Income_Category, Card_Category, Months_on_book,
                                       Total_Relationship_Count, Months_Inactive_12_mon,
                                       Contacts_Count_12_mon, Credit_Limit, Total_Revolving_Bal,
                                       Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt,
                                       Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio)
                                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)

        # commit changes and close connection
        conn.commit()
        conn.close()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    SIGNUP PAGE            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(820, 602)
        self.setWindowTitle('Sign Up')
        self.setWindowIcon(QIcon('icon.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(820, 602))
        self.setMaximumSize(QtCore.QSize(820, 602))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(11)
        self.setFont(font)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.setStyleSheet("background-color: rgb(18, 35, 46);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 410, 602))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.frame.setFont(font)
        self.frame.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.frame.setStyleSheet("background-color: rgb(0, 124, 199);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(60, 140, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(18, 35, 46);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(18, 35, 46);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 310, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 400, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border-radius: 8px;\n"
                                      "background-color: rgb(32, 54, 71);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.new_user)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.w = None
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 450, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(18, 35, 46);")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 100, 191, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("moneywise2.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(540, 280, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(23)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 238, 238);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 360, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(238, 251, 251);")
        self.label_6.setObjectName("label_6")
        self.retranslateUi(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.label_2.setText(_translate("MainWindow", "New Username"))
        self.label_3.setText(_translate("MainWindow", "New Password"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.pushButton.clicked.connect(self.new_user)
        self.label_5.setText(_translate("MainWindow", "MONEYWISE"))
        self.label_6.setText(_translate("MainWindow", "Snap Into A Banking!"))

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         NEW USER DB FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def new_user(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        connection = sqlite3.connect("Banklogin.db")
        try:
            # Execute the INSERT query with the new username and password values
            connection.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
            # Commit the changes to the database
            connection.commit()
            print("New user added successfully!")
        except sqlite3.IntegrityError:
            # Handle the exception when the username already exists in the database
            print("Username already exists in the database.")
        connection.close()
        self.window = Login()
        self.window.show()
        self.close()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LOGIN PAGE            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(820, 602)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Login')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(820, 602))
        self.setMaximumSize(QtCore.QSize(820, 602))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(11)
        self.setFont(font)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.setStyleSheet("background-color: #373833;color:white")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 410, 602))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.frame.setFont(font)
        self.frame.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.frame.setStyleSheet("background-color: #EAF8E1;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(60, 100, 141, 71))
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 154, 70, 3))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background-color: #383837;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #383837;font-weight:bold")
        # self.label.setFont(QFont.bold())
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.lineEdit.setFont(font)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(62, 260, 300, 3))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background-color: rgb(113, 185, 20);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(62, 345, 300, 3))
        self.line2.setAutoFillBackground(False)
        self.line2.setStyleSheet("background-color: rgb(113, 185, 20);")
        self.line2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lineEdit.setFrame(False)
        self.lineEdit.setStyleSheet("QLineEdit:focus { border: none; } ; color: #2A2A29;")
        self.lineEdit.setStyleSheet("color: #2A2A29;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(18, 35, 46);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(18, 35, 46);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 310, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.lineEdit_2.setFont(font)
        # self.lineEdit_2.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setStyleSheet("color: #2A2A29;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 400, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border-radius: 8px;\n"
                                      "background-color: #2A2A29;")
        self.pushButton.setObjectName("pushButton")
        # self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        # self.pushButton_2.setGeometry(QtCore.QRect(252, 350, 111, 28))
        # self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        # self.pushButton_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        # self.pushButton_2.setStyleSheet("color: #2A2A29;font-weight:bold")
        # self.pushButton_2.setDefault(False)
        # self.pushButton_2.setFlat(True)
        # self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 450, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.w = None
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_3.setStyleSheet("color: #2A2A29;font-weight:bold")
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.new_record)
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(60, 450, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(18, 35, 46);")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 100, 191, 161))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("moneywise2.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 280, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(23)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #71B914;font-weight:bold")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 360, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #fff;")
        self.label_6.setObjectName("label_6")
        self.retranslateUi(self)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         SIGNUP PAGE FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def new_record(self):
        self.window = Signup()
        self.window.show()
        self.close()

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                         LOGIN PAGE FUNCTION            
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    def loginCheck(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # print(len(username))
        # if len(username) == 0:
        #     empty = QMessageBox.critical(
        #         self,
        #         "Login Issue",
        #         "Fill out the username",
        #         # buttons=QMessageBox.StandardButton.ok,
        #         defaultButton=QMessageBox.StandardButton.Ok,
        #     )
        # elif len(password) == 0:
        #     empty = QMessageBox.critical(
        #         self,
        #         "Login Issue",
        #         "Fill out the username",
        #         # buttons=QMessageBox.StandardButton.ok,
        #         defaultButton=QMessageBox.StandardButton.Ok,
        #     )

        connection = sqlite3.connect("Banklogin.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        if len(result.fetchall()) > 0:
            self.welcomeWindowShow()
        else:
            not_found = QMessageBox.critical(
                self,
                "Login Issue",
                "No User Found !",
                defaultButton=QMessageBox.StandardButton.Ok,
            )
        connection.close()

    def welcomeWindowShow(self):
        self.window = MyMainWindow()
        self.window.showMaximized()
        self.window.setStyleSheet("background-color: rgb(18, 35, 46)")
        self.window.show()
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(self.loginCheck)
        self.lineEdit_2.returnPressed.connect(self.loginCheck)
        # self.pushButton_2.setText(_translate("MainWindow", "Forgot Password?"))
        self.pushButton_3.setText(_translate("MainWindow", "Register"))
        self.label_7.setText(_translate("MainWindow", "Don\'t have an account?"))
        self.label_5.setText(_translate("MainWindow", "MONEYWISE"))
        self.label_6.setText(_translate("MainWindow", "Snap Into A Banking!"))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    MAIN DRIVER            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

if __name__ == '__main__':
    app = QApplication([])
    window = Login()
    window.show()
    sys.exit(app.exec())
