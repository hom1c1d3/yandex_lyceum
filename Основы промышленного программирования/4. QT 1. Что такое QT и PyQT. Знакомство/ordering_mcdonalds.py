import sys

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbCheesburger = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCheesburger.sizePolicy().hasHeightForWidth())
        self.cbCheesburger.setSizePolicy(sizePolicy)
        self.cbCheesburger.setObjectName("cbCheesburger")
        self.verticalLayout.addWidget(self.cbCheesburger)
        self.cbGamburger = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbGamburger.sizePolicy().hasHeightForWidth())
        self.cbGamburger.setSizePolicy(sizePolicy)
        self.cbGamburger.setObjectName("cbGamburger")
        self.verticalLayout.addWidget(self.cbGamburger)
        self.cbCocaCola = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCocaCola.sizePolicy().hasHeightForWidth())
        self.cbCocaCola.setSizePolicy(sizePolicy)
        self.cbCocaCola.setObjectName("cbCocaCola")
        self.verticalLayout.addWidget(self.cbCocaCola)
        self.cbNugget = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbNugget.sizePolicy().hasHeightForWidth())
        self.cbNugget.setSizePolicy(sizePolicy)
        self.cbNugget.setObjectName("cbNugget")
        self.verticalLayout.addWidget(self.cbNugget)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.btnOrder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOrder.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOrder.sizePolicy().hasHeightForWidth())
        self.btnOrder.setSizePolicy(sizePolicy)
        self.btnOrder.setObjectName("btnOrder")
        self.verticalLayout.addWidget(self.btnOrder)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заказ в Макдональдсе"))
        self.cbCheesburger.setText(_translate("MainWindow", "Чизбургер"))
        self.cbGamburger.setText(_translate("MainWindow", "Гамбургер"))
        self.cbCocaCola.setText(_translate("MainWindow", "Кока-кола"))
        self.cbNugget.setText(_translate("MainWindow", "Нагетсы"))
        self.btnOrder.setText(_translate("MainWindow", "Заказать"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnOrder.clicked.connect(self.create_order)

    def create_order(self):
        self.plainTextEdit.setPlainText('Ваш заказ:\n')
        for cb in (getattr(self, i) for i in self.__dict__ if i.startswith('cb')):
            if cb.isChecked():
                self.plainTextEdit.appendPlainText(cb.text())
        if self.plainTextEdit.toPlainText() == 'Ваш заказ:\n':
            self.plainTextEdit.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
