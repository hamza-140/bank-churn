import csv
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtChart import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QPieSeries, QPieSlice


def create_bar_chart(csv_file, column_name):
    # Read the CSV file
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row[column_name] for row in reader]

    # Count the number of males and females
    counts = {'Male': 0, 'Female': 0}
    for gender in data:
        if gender == 'M':
            counts['Male'] += 1
        elif gender == 'F':
            counts['Female'] += 1


    app = QApplication([])
    # Create a bar chart
    series = QPieSeries()
    series.append("Male", counts['Male'])
    series.append("Female", counts['Female'])

    # adding slice
    slice = QPieSlice()
    slice = series.slices()[1]
    slice.setExploded(True)
    slice.setLabelVisible(True)
    slice.setPen(QPen(Qt.darkGreen, 2))
    slice.setBrush(Qt.green)

    chart = QChart()
    chart.legend().hide()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.setTitle("Gender Comparison")

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    chartview = QChartView(chart)
    chartview.setRenderHint(QPainter.Antialiasing)

    # Set up the main window and add the chart view to it
    mainWindow = QMainWindow()
    mainWindow.setCentralWidget(chartview)
    mainWindow.resize(800, 600)
    mainWindow.show()

    app.exec_()

# Example usage
create_bar_chart('BankChurners1.csv', 'Gender')
