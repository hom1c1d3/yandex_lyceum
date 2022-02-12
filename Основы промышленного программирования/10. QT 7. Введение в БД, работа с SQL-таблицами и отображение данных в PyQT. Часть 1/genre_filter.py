import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 522)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxGenres = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.comboBoxGenres.sizePolicy().hasHeightForWidth())
        self.comboBoxGenres.setSizePolicy(sizePolicy)
        self.comboBoxGenres.setObjectName("comboBoxGenres")
        self.verticalLayout.addWidget(self.comboBoxGenres)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фильтрация по жанрам"))
        self.pushButton.setText(_translate("MainWindow", "Пуск"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.cur = self.create_cursor('films_db.sqlite')
        self.genres = {title: id_ for id_, title in
                       self.cur.execute('SELECT id, title from genres')}
        self.setupUi(self)

    @staticmethod
    def create_cursor(db_name):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        return cur

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.comboBoxGenres.addItems(self.genres.keys())
        data = self.cur.execute(f'SELECT title, genre, year FROM films').fetchall()
        self.set_table_data(data)
        self.pushButton.clicked.connect(self.set_table)

    def set_table_data(self, data):
        headers = ['Название', 'Жанр', 'Год']
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setRowCount(0)
        for row_ind, i in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for col_ind, (_, j) in enumerate(zip(headers, i)):
                item = QtWidgets.QTableWidgetItem(str(j))
                self.tableWidget.setItem(row_ind, col_ind, item)
        self.tableWidget.setHorizontalHeaderLabels(headers)

    def set_table(self):
        genre_id = self.genres[self.comboBoxGenres.currentText()]
        data = self.cur.execute(f'SELECT title, genre, year FROM films WHERE genre = {genre_id}')
        self.set_table_data(data)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
