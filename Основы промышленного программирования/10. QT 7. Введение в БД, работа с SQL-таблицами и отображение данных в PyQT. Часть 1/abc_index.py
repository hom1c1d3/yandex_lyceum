import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алфавитный указатель"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        self.header = ['ID', 'Название', 'Жанр', 'Год', 'Продолжительность']
        self.cur = self.get_cursor('films_db.sqlite')
        self.setupUi(self)

    @staticmethod
    def get_cursor(name):
        con = sqlite3.connect(name)
        cur = con.cursor()
        return cur

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        for letter in self.alphabet:
            btn = QtWidgets.QPushButton(letter.upper(), self)
            btn.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                                    QtWidgets.QSizePolicy.Fixed))
            btn.clicked.connect(self.display_db_by_letter)
            self.horizontalLayout.addWidget(btn)

        self.display_db()
        self.showMaximized()

    def get_data_by_letter(self, letter=None):
        res = self.cur.execute(f"""SELECT * FROM films WHERE title LIKE 
        "{letter.upper() if letter is not None else ''}%" """).fetchall()
        return res

    def display_db_by_letter(self):
        letter = self.sender().text()
        self.display_db(letter)

    def display_db(self, letter=None):
        self.tableWidget.setColumnCount(len(self.header))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(self.header)
        data = self.get_data_by_letter(letter)
        data_length = len(data)
        for row_ind, row in enumerate(data):
            self.tableWidget.setRowCount(row_ind + 1)
            for item_ind, item in enumerate(row):
                self.tableWidget.setItem(row_ind, item_ind, QtWidgets.QTableWidgetItem(str(item)))
        self.tableWidget.resizeColumnsToContents()
        if not data_length:
            self.statusBar.showMessage(f"К сожалению, ничего не нашлось")
        else:
            self.statusBar.showMessage(f"Нашлось {data_length} записей")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
