import sys
import sqlite3
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.lineEditTitle = QtWidgets.QLineEdit(Dialog)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.gridLayout.addWidget(self.lineEditTitle, 0, 1, 1, 1)
        self.comboBoxGenre = QtWidgets.QComboBox(Dialog)
        self.comboBoxGenre.setObjectName("comboBoxGenre")
        self.gridLayout.addWidget(self.comboBoxGenre, 2, 1, 1, 1)
        self.labelYear = QtWidgets.QLabel(Dialog)
        self.labelYear.setObjectName("labelYear")
        self.gridLayout.addWidget(self.labelYear, 1, 0, 1, 1)
        self.lineEditYear = QtWidgets.QLineEdit(Dialog)
        self.lineEditYear.setObjectName("lineEditYear")
        self.gridLayout.addWidget(self.lineEditYear, 1, 1, 1, 1)
        self.labelGenre = QtWidgets.QLabel(Dialog)
        self.labelGenre.setObjectName("labelGenre")
        self.gridLayout.addWidget(self.labelGenre, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditDuration = QtWidgets.QLineEdit(Dialog)
        self.lineEditDuration.setObjectName("lineEditDuration")
        self.gridLayout.addWidget(self.lineEditDuration, 3, 1, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(Dialog)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить элемент"))
        self.labelTitle.setText(_translate("Dialog", "Называние"))
        self.labelYear.setText(_translate("Dialog", "Год выпуска"))
        self.labelGenre.setText(_translate("Dialog", "Жанр"))
        self.label_4.setText(_translate("Dialog", "Длина"))
        self.btnAdd.setText(_translate("Dialog", "Добавить"))


class AddElementDialog(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self, parent, con):
        super(AddElementDialog, self).__init__(parent)
        self.con = con
        self.cur = self.con.cursor()
        self.setupUi(self)
    
    def setupUi(self, Dialog):
        super(AddElementDialog, self).setupUi(Dialog)
        genres = self.get_genres()
        self.comboBoxGenre.addItems(genres)
        self.btnAdd.clicked.connect(self.add_item)

    def get_genres(self):
        genres = self.cur.execute("""SELECT title FROM genres""").fetchall()
        return [i[0] for i in genres]

    def add_item(self):
        title = self.lineEditTitle.text()
        year = self.lineEditYear.text()
        genre = self.comboBoxGenre.currentText()
        duration = self.lineEditDuration.text()
        if '' in (title, year, duration):
            QtWidgets.QMessageBox.critical(self, 'Неверные данные', 'Введите данные')
            return
        try:
            int(year)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, 'Неверные данные', 'Введите год в виде числа')
            return
        if int(year) > datetime.now().year:
            QtWidgets.QMessageBox.critical(self, 'Неверные данные', 'Год не должен быть в будущем')
            return
        try:
            int(duration)
        except ValueError:
            QtWidgets.QMessageBox.critical(self, 'Неверные данные', 'Введите длину в виде числа')
            return
        if int(duration) < 1:
            QtWidgets.QMessageBox.critical(self, 'Неверные данные', 'Ввиде положительную длину')
            return
        genre = self.get_genre_id(genre)
        self.add_item_db(title, year, genre, duration)
        self.close()

    def get_genre_id(self, genre):
        identification = self.cur.execute("""SELECT id FROM genres WHERE title = ?""", (genre,))
        return identification.fetchone()[0]

    def add_item_db(self, title, year, genre, duration):
        self.cur.execute("""INSERT INTO films(title, year, genre, duration)
         VALUES(?, ?, ?, ?)""", (title, year, genre, duration))
        self.con.commit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фильмотека"))
        self.btnAdd.setText(_translate("MainWindow", "Добавить"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.con = sqlite3.connect('films_db.sqlite')
        self.cur = self.con.cursor()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnAdd.clicked.connect(self.add_item)
        self.display_table()

    def add_item(self):
        dialog = AddElementDialog(self, self.con)
        dialog.exec()
        self.display_table()

    def get_films_data(self):
        films_data = self.cur.execute("""SELECT films.id, films.title, year, genres.title, duration
         FROM films
         INNER JOIN genres ON films.genre = genres.id
         ORDER BY films.id DESC""").fetchall()
        return films_data

    def display_table(self):
        headers = ['ИД', 'Называние фильма', 'Год выпуска', 'Жанр', 'Продолжительность']
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setRowCount(0)
        data = self.get_films_data()
        for row_ind, i in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for col_ind, (_, j) in enumerate(zip(headers, i)):
                item = QtWidgets.QTableWidgetItem(str(j))
                self.tableWidget.setItem(row_ind, col_ind, item)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
