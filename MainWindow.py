import csv
# import form
import pandas as pd
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
global a
class FormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Churn Prediction")
        self.layout=QFormLayout()
        self.setLayout(self.layout)
        self.setGeometry(110,50,1000,600)
        # self.CLIENTNUM=QLabel("Client Number:")

        #
        # # self.label21 = QLabel("compressionratio:")
        # # layout.addWidget(self.label21, 6, 4)
        # #
        # # self.label22 = QLabel("horsepower:")
        # # layout.addWidget(self.label22, 7, 0)
        # #
        # # self.label23 = QLabel("peakrpm:")
        # # layout.addWidget(self.label23, 7, 2)
        # #
        # # self.label24 = QLabel("citympg:")
        # # layout.addWidget(self.label24, 7, 4)
        # #
        # # self.label25 = QLabel("highwaympg:")
        # # layout.addWidget(self.label25, 8, 0)
        # #
        # # self.label26 = QLabel("price:")
        # # layout.addWidget(self.label26, 8, 2)
        #
        # #Inputs
        #
        # self.input1=QLineEdit(self.CLIENTNUM,self)
        # # self.input1.addItems(["Foo", "Bar", "Baz"])
        # # ...anything else like signals and slots connections
        # layout.addWidget(self.input1, 0, 1)
        #
        # self.input1 = QLineEdit()
        # layout.addWidget(self.input1, 0, 1)
        #
        # self.input2 = QLineEdit()
        # layout.addWidget(self.input2,0, 3)
        #
        # self.input3 = QComboBox()
        # self.input3.addItems(["volvo", "alfa-romero","opel","audi","chevrolet","dodge","honda","isuzu","jaguar","mazda","buick","mercury","nisan","porsche","peugeot","plymouth","renault","subaru","toyota","saab","volkswagen"])
        # layout.addWidget(self.input3, 0, 5)
        #
        # self.input4 = QComboBox()
        # self.input4.addItems(["gas", "diesel"])
        # layout.addWidget(self.input4, 1, 1)
        #
        # self.input5 = QComboBox()
        # self.input5.addItems(["turbo","std"])
        # layout.addWidget(self.input5, 1, 3)
        #
        # self.input6 = QLineEdit()
        # layout.addWidget(self.input6, 1, 5)
        #
        # self.input7 = QComboBox()
        # self.input7.addItems(["convertable", "hatchback","sedan","wagon","hardtop"])
        # layout.addWidget(self.input7, 2, 1)
        #
        # self.input8 = QComboBox()
        # self.input8.addItems(["fwd", "rwd", "4wd"])
        # layout.addWidget(self.input8, 2, 3)
        #
        # self.input9 = QLineEdit()
        # layout.addWidget(self.input9, 2, 5)
        #
        # self.input10 = QLineEdit()
        # layout.addWidget(self.input10, 3, 1)
        #
        # self.input11 = QLineEdit()
        # layout.addWidget(self.input11, 3, 3)
        #
        # self.input12 = QLineEdit()
        # layout.addWidget(self.input12, 3, 5)
        #
        # self.input13 = QLineEdit()
        # layout.addWidget(self.input13, 4, 1)
        #
        # self.input14 = QLineEdit()
        # layout.addWidget(self.input14, 4, 3)
        #
        # self.input15 = QComboBox()
        # self.input15.addItems(["ohc", "dohc", "I", "ohcv", "rotor", "ohcf"])
        # layout.addWidget(self.input15, 4, 5)
        #
        # self.input16 = QComboBox()
        # self.input16.addItems(["two","three","four","five","six","eight","twelve"])
        # layout.addWidget(self.input16, 5, 1)
        #
        # self.input17 = QLineEdit()
        # layout.addWidget(self.input17, 5, 3)
        #
        # self.input18 = QLineEdit()
        # layout.addWidget(self.input18, 5, 5)
        #
        # self.input19 = QLineEdit()
        # layout.addWidget(self.input19, 6, 1)
        #
        # self.input20 = QLineEdit()
        # layout.addWidget(self.input20, 6, 3)
        #
        # self.input21 = QLineEdit()
        # layout.addWidget(self.input21, 6, 5)
        #
        # self.input22 = QLineEdit()
        # layout.addWidget(self.input22, 7, 1)
        #
        # self.input23 = QLineEdit()
        # layout.addWidget(self.input23, 7, 3)
        #
        # self.input24 = QLineEdit()
        # layout.addWidget(self.input24, 7, 5)
        #
        # self.input25 = QLineEdit()
        # layout.addWidget(self.input25, 8, 1)
        #
        # self.input26 = QLineEdit()
        # layout.addWidget(self.input26, 8, 3)
        #
        # button=QPushButton("Submit")
        # button.setFixedWidth(120)
        # # button.clicked.connect(self.display)
        # layout.addWidget(button,10,3)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.CLIENTNUM = None
        self.setWindowTitle("Bank Churner Prediction")
        df = pd.read_csv('BankChurners.csv')

        # convert dataframe to a list of dictionaries
        customers = df.to_dict('records')

        # display the list of dictionaries
        # print(employees)
        self.window = None
        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(20)
        # self.table.setColumnWidth(0, 150)
        # self.table.setColumnWidth(1, 150)
        # self.table.setColumnWidth(2, 50)

        self.table.setHorizontalHeaderLabels(customers[0].keys())
        self.table.setRowCount(len(customers))
        column_names = []
        for i in customers[0].keys():
            column_names.append(i)
        row = 0

        for e in customers:
            # print(col)
            # print('"{0}"'.format(column_names[col]))
            self.table.setItem(row, 0, QTableWidgetItem(str(e['{0}'.format(column_names[0])])))
            self.table.setItem(row, 1, QTableWidgetItem(str(e['{0}'.format(column_names[1])])))
            self.table.setItem(row, 2, QTableWidgetItem(str(e['{0}'.format(column_names[2])])))
            self.table.setItem(row, 3, QTableWidgetItem(str(e['{0}'.format(column_names[3])])))
            self.table.setItem(row, 4, QTableWidgetItem(str(e['{0}'.format(column_names[4])])))
            self.table.setItem(row, 5, QTableWidgetItem(str(e['{0}'.format(column_names[5])])))
            self.table.setItem(row, 6, QTableWidgetItem(str(e['{0}'.format(column_names[6])])))
            self.table.setItem(row, 7, QTableWidgetItem(str(e['{0}'.format(column_names[7])])))
            self.table.setItem(row, 8, QTableWidgetItem(str(e['{0}'.format(column_names[8])])))
            self.table.setItem(row, 9, QTableWidgetItem(str(e['{0}'.format(column_names[9])])))
            self.table.setItem(row, 10, QTableWidgetItem(str(e['{0}'.format(column_names[10])])))
            self.table.setItem(row, 11, QTableWidgetItem(str(e['{0}'.format(column_names[11])])))
            self.table.setItem(row, 12, QTableWidgetItem(str(e['{0}'.format(column_names[12])])))
            self.table.setItem(row, 13, QTableWidgetItem(str(e['{0}'.format(column_names[13])])))
            self.table.setItem(row, 14, QTableWidgetItem(str(e['{0}'.format(column_names[14])])))
            self.table.setItem(row, 15, QTableWidgetItem(str(e['{0}'.format(column_names[15])])))
            self.table.setItem(row, 16, QTableWidgetItem(str(e['{0}'.format(column_names[16])])))
            self.table.setItem(row, 17, QTableWidgetItem(str(e['{0}'.format(column_names[17])])))
            self.table.setItem(row, 18, QTableWidgetItem(str(e['{0}'.format(column_names[18])])))
            self.table.setItem(row, 19, QTableWidgetItem(str(e['{0}'.format(column_names[19])])))
            # print((str(e['{0}'.format(column_names[0])])))
            # self.table.setItem(row, 1, QTableWidgetItem(str(e['Customer_Age'])))
            # self.table.setItem(row, 2, QTableWidgetItem(str(e['Gender'])))
            row +=1
        # print(row)
        dock = QDockWidget('New Customer')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        # create form
        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.first_name = QLineEdit(form)
        self.last_name = QLineEdit(form)
        self.age = QSpinBox(form, minimum=18, maximum=67)
        self.age.clear()

        layout.addRow('First Name:', self.first_name)
        layout.addRow('Last Name:', self.last_name)
        layout.addRow('Age:', self.age)

        btn_add = QPushButton('Add')
        btn_add.clicked.connect(self.add_employee)
        layout.addRow(btn_add)

        # add delete & edit button
        toolbar = QToolBar('main toolbar')
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        add_action = QAction(QIcon('./add.png'), '&Add', self)
        add_action.triggered.connect(self.form_window)
        toolbar.addAction(add_action)


        delete_action = QAction(QIcon('delete.png'), '&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)

        delete_button = QPushButton('Delete', form)
        delete_button.clicked.connect(self.delete)
        layout.addRow(delete_button)
        edit_action = QAction(QIcon('edit.png'), '&Edit', self)
        edit_action.triggered.connect(self.edit_employee)
        toolbar.addAction(edit_action)

        edit_button = QPushButton('Edit', form)
        edit_button.clicked.connect(self.edit_employee)
        layout.addRow(edit_button)

        search_action = QAction(QIcon('search.png'), '&Search', self)
        search_action.triggered.connect(self.search)
        toolbar.addAction(search_action)
        search_button = QPushButton('Search', form)
        search_button.clicked.connect(self.search)
        layout.addRow(search_button)
        dock.setWidget(form)

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

    def form_window(self):
        if self.window is None:
            self.window = FormWindow()
        self.window.show()

    def edit_employee(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            return QMessageBox.warning(self, 'Warning', 'Please select a record to edit')

        first_name = self.table.item(current_row, 0).text()
        last_name = self.table.item(current_row, 1).text()
        age = int(self.table.item(current_row, 2).text())

        form = QWidget()
        layout = QFormLayout(form)
        form.setLayout(layout)

        self.first_name_update = QLineEdit(first_name, form)
        self.last_name_update = QLineEdit(last_name, form)
        self.age_update = QSpinBox(form, minimum=18, maximum=67)
        self.age_update.setValue(age)

        layout.addRow('First Name:', self.first_name_update)
        layout.addRow('Last Name:', self.last_name_update)
        layout.addRow('Age:', self.age_update)

        btn_edit = QPushButton('Update')
        btn_edit.clicked.connect(lambda: self.update_employee(current_row))
        layout.addRow(btn_edit)

        dock = QDockWidget('Edit Employee')
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        dock.setWidget(form)

    def update_employee(self, row):
        # if not self.valid():
        #     return
        # print(self.first_name_update.text())
        self.table.setItem(row, 0, QTableWidgetItem(self.first_name_update.text()))
        self.table.setItem(row, 1, QTableWidgetItem(self.last_name_update.text()))
        self.table.setItem(row, 2, QTableWidgetItem(self.age_update.text()))
        self.save()

        # self.reset()
        # self.hide_dock_widgets()

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
        if button == QMessageBox.StandardButton.Yes:
            self.table.removeRow(current_row)
            self.save()

    def valid(self):
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()

        if not first_name:
            QMessageBox.critical(self, 'Error', 'Please enter the first name')
            self.first_name.setFocus()
            return False

        if not last_name:
            QMessageBox.critical(self, 'Error', 'Please enter the last name')
            self.last_name.setFocus()
            return False

        try:
            age = int(self.age.text().strip())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Please enter a valid age')
            self.age.setFocus()
            return False

        if age <= 0 or age >= 67:
            QMessageBox.critical(
                self, 'Error', 'The valid age is between 1 and 67')
            return False

        return True

    def reset(self):
        self.first_name.clear()
        self.last_name.clear()
        self.age.clear()

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

    def add_employee(self,a):
        # if not self.valid():
        #     return
        # var = FormWindow()
        # a = var.CLIENTNUM.text()
        # print(a)
        # print(var.CLIENTNUM.text())
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(
            a)
                           )
        self.table.setItem(
            row, 1, QTableWidgetItem(self.last_name.text())
        )
        self.table.setItem(
            row, 2, QTableWidgetItem(self.age.text())
        )

        self.reset()
        self.save()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    window.show()
    sys.exit(app.exec())
