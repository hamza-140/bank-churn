import csv
import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDockWidget, QFormLayout, \
    QLineEdit, QWidget, QPushButton, QSpinBox, QMessageBox, QToolBar, QInputDialog
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Employees')
        self.setWindowIcon(QIcon('./assets/usergroup.png'))
        self.setGeometry(100, 100, 600, 400)

        # import pandas as pd

        # read csv file as a pandas dataframe
        df = pd.read_csv('test.csv')

        # convert dataframe to a list of dictionaries
        employees = df.to_dict('records')

        # display the list of dictionaries
        # print(employees)

        self.table = QTableWidget(self)
        self.setCentralWidget(self.table)

        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 50)

        self.table.setHorizontalHeaderLabels(employees[0].keys())
        self.table.setRowCount(len(employees))

        row = 0
        for e in employees:
            self.table.setItem(row, 0, QTableWidgetItem(e['First Name']))
            self.table.setItem(row, 1, QTableWidgetItem(e['Last Name']))
            self.table.setItem(row, 2, QTableWidgetItem(str(e['Age'])))
            row += 1

        dock = QDockWidget('New Employee')
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

        delete_action = QAction(QIcon('./assets/remove.png'), '&Delete', self)
        delete_action.triggered.connect(self.delete)
        toolbar.addAction(delete_action)

        delete_button = QPushButton('Delete', form)
        delete_button.clicked.connect(self.delete)
        layout.addRow(delete_button)
        edit_action = QAction(QIcon('./assets/edit.png'), '&Edit', self)
        edit_action.triggered.connect(self.edit_employee)
        toolbar.addAction(edit_action)

        edit_button = QPushButton('Edit', form)
        edit_button.clicked.connect(self.edit_employee)
        layout.addRow(edit_button)

        search_action = QAction(QIcon('./assets/search.png'), '&Search', self)
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
        with open('test.csv', 'w', newline='') as csvfile:
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

    def add_employee(self):
        if not self.valid():
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(
            self.first_name.text().strip())
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
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())