import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelID = QtWidgets.QLabel(self.centralwidget)
        self.labelID.setObjectName("labelID")
        self.gridLayout.addWidget(self.labelID, 0, 0, 1, 1)
        self.spinBoxID = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxID.setObjectName("spinBoxID")
        self.spinBoxID.setMaximum(2147483647)
        self.gridLayout.addWidget(self.spinBoxID, 0, 1, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 1)
        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.gridLayout.addWidget(self.pushButtonLoad, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelID.setText(_translate("MainWindow", "ID:"))
        self.pushButtonSave.setText(_translate("MainWindow", "Изменить"))
        self.pushButtonLoad.setText(_translate("MainWindow", "Загрузить"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.con = sqlite3.connect("films_db.sqlite")
        self.modified = {}
        self.titles = None
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.pushButtonLoad.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButtonSave.clicked.connect(self.save_results)

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT * FROM films WHERE id=?",
                             (item_id := self.spinBoxID.text(),)).fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        if not result:
            self.statusBar.showMessage('Ничего не нашлось')
            return
        else:
            self.statusBar.showMessage(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        reply = QtWidgets.QMessageBox.question(self, 'python',
                                               f'Действительно заменить элементы'
                                               f' с id {self.spinBoxID.text()}')
        if reply == QtWidgets.QMessageBox.No:
            return
        cur = self.con.cursor()
        que = "UPDATE films SET\n"
        que += ", ".join([f"{key}='{self.modified.get(key)}'"
                          for key in self.modified.keys()])
        title = self.tableWidget.item(0, 1).text()
        year = int(self.tableWidget.item(0, 2).text())
        duration = int(self.tableWidget.item(0, 4).text())
        self.modified = {'title': title[::-1], 'year': year + 1000, 'duration': duration * 2}
        que += ", ".join([f"{key}='{self.modified.get(key)}'"
                          for key in self.modified.keys()])
        que += "WHERE id = ?"
        cur.execute(que, (self.spinBoxID.text(),))
        self.con.commit()
        self.modified.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
