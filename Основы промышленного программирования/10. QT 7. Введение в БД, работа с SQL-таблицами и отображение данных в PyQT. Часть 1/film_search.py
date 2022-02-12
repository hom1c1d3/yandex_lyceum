import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditParameter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditParameter.setObjectName("lineEditParameter")
        self.gridLayout.addWidget(self.lineEditParameter, 0, 1, 1, 2)
        self.comboBoxParameter = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxParameter.setObjectName("comboBoxParameter")
        self.gridLayout.addWidget(self.comboBoxParameter, 0, 0, 1, 1)
        self.labelYear = QtWidgets.QLabel(self.centralwidget)
        self.labelYear.setObjectName("labelYear")
        self.gridLayout.addWidget(self.labelYear, 3, 0, 1, 1)
        self.lineEditYear = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditYear.setObjectName("lineEditYear")
        self.gridLayout.addWidget(self.lineEditYear, 3, 1, 1, 3)
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 2, 0, 1, 1)
        self.labelID = QtWidgets.QLabel(self.centralwidget)
        self.labelID.setObjectName("labelID")
        self.gridLayout.addWidget(self.labelID, 1, 0, 1, 1)
        self.labelDuration = QtWidgets.QLabel(self.centralwidget)
        self.labelDuration.setObjectName("labelDuration")
        self.gridLayout.addWidget(self.labelDuration, 5, 0, 1, 1)
        self.lineEditTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.gridLayout.addWidget(self.lineEditTitle, 2, 1, 1, 3)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setObjectName("btnSearch")
        self.gridLayout.addWidget(self.btnSearch, 0, 3, 1, 1)
        self.lineEditGenre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditGenre.setObjectName("lineEditGenre")
        self.gridLayout.addWidget(self.lineEditGenre, 4, 1, 1, 3)
        self.labelGenre = QtWidgets.QLabel(self.centralwidget)
        self.labelGenre.setObjectName("labelGenre")
        self.gridLayout.addWidget(self.labelGenre, 4, 0, 1, 1)
        self.lineEditID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditID.setObjectName("lineEditID")
        self.gridLayout.addWidget(self.lineEditID, 1, 1, 1, 3)
        self.lineEditDuration = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDuration.setObjectName("lineEditDuration")
        self.gridLayout.addWidget(self.lineEditDuration, 5, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск по фильмам"))
        self.labelYear.setText(_translate("MainWindow", "Год выпуска"))
        self.labelTitle.setText(_translate("MainWindow", "Название:"))
        self.labelID.setText(_translate("MainWindow", "ID:"))
        self.labelDuration.setText(_translate("MainWindow", "Продолжительность:"))
        self.btnSearch.setText(_translate("MainWindow", "Поиск"))
        self.labelGenre.setText(_translate("MainWindow", "Жанр:"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.parameters = {'Название': 'title',
                           'Год выпуска': 'year', 'Продолжительность фильма': 'duration'}
        self.cur = self.create_cursor('films_db.sqlite')
        self.setupUi(self)

    @staticmethod
    def create_cursor(db_name):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        return cur

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.comboBoxParameter.addItems(self.parameters.keys())
        self.btnSearch.clicked.connect(self.search)

    @staticmethod
    def form_query(search_key, parameter_value):
        query = f"""SELECT * FROM films WHERE {search_key} = {parameter_value} 
        ORDER BY id ASC LIMIT 1"""
        return query

    def search_db(self, search_key, parameter_value):
        if search_key == 'title':
            parameter_value = f'"{parameter_value}"' if parameter_value else parameter_value
        query = self.form_query(search_key, parameter_value)
        try:
            results = self.cur.execute(query).fetchone()
        except sqlite3.OperationalError as e:
            results = e
        return results

    def clear_all_results(self):
        for i in (self.lineEditID, self.lineEditTitle,
                  self.lineEditYear, self.lineEditGenre, self.lineEditDuration):
            i.clear()

    def set_results(self, results):
        if isinstance(results, sqlite3.OperationalError) or results is None:
            self.clear_all_results()
            if isinstance(results, sqlite3.OperationalError):
                self.statusBar.showMessage('Неправильный запрос')
            else:
                self.statusBar.showMessage('Ничего не найдено')
            return
        self.statusBar.clearMessage()
        id_, title, year, genre, duration = results
        for le, val in zip((self.lineEditID, self.lineEditTitle,
                            self.lineEditYear, self.lineEditGenre, self.lineEditDuration),
                           (id_, title, year, genre, duration)):
            le.setText(str(val))

    def search(self):
        search_key = self.parameters[self.comboBoxParameter.currentText()]
        parameter_value = self.lineEditParameter.text()
        results = self.search_db(search_key, parameter_value)
        self.set_results(results)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
