import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 50)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGet = QtWidgets.QPushButton(self.centralwidget)
        self.btnGet.setObjectName("btnGet")
        self.horizontalLayout.addWidget(self.btnGet)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Случайная строка"))
        self.btnGet.setText(_translate("MainWindow", "Получить"))


def rand_line(file):
    try:
        line = next(file)
    except StopIteration:
        return

    for ind, iline in enumerate(file, 2):
        if random.randrange(ind):
            continue
        line = iline

    return line


def random_line():
    with open('lines.txt', 'r', encoding='utf8') as f:
        res = rand_line(f)
        return res


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnGet.clicked.connect(self.solve_random_line)

    def solve_random_line(self):
        try:
            res = random_line()
        except FileNotFoundError:
            res = 'Файл не найден'
        self.lineEdit.setText(res)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
