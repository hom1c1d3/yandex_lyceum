import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.gridLayout.addWidget(self.lineEditFileName, 0, 1, 1, 1)
        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoad.setObjectName("btnLoad")
        self.gridLayout.addWidget(self.btnLoad, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перемешивание"))
        self.btnLoad.setText(_translate("MainWindow", "Загрузить строки"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnLoad.clicked.connect(self.shuffle_lines)

    def get_file_data(self, file_name):
        try:
            with open(file_name, 'r', encoding='utf8') as f:
                data = f.read()
        except FileNotFoundError:
            self.statusbar.showMessage(f'Файл {repr(file_name)} не найден')
            return
        return data

    def set_lines(self, data):
        data = data.splitlines()
        res = data[1::2] + data[0::2]
        res = '\n'.join(res)
        self.plainTextEdit.setPlainText(res)

    def shuffle_lines(self):
        filename = self.lineEditFileName.text()
        data = self.get_file_data(filename)
        if data is None:
            return
        self.set_lines(data)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
