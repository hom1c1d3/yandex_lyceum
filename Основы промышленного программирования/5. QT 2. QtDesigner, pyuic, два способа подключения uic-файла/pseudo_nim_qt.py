import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 470)
        MainWindow.setMinimumSize(QtCore.QSize(670, 470))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetMoves = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.listWidgetMoves.sizePolicy().hasHeightForWidth())
        self.listWidgetMoves.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidgetMoves.setFont(font)
        self.listWidgetMoves.setObjectName("listWidgetMoves")
        self.gridLayout.addWidget(self.listWidgetMoves, 4, 0, 1, 3)
        self.btnTake = QtWidgets.QPushButton(self.centralwidget)
        self.btnTake.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.btnTake.sizePolicy().hasHeightForWidth())
        self.btnTake.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnTake.setFont(font)
        self.btnTake.setCheckable(False)
        self.btnTake.setObjectName("btnTake")
        self.gridLayout.addWidget(self.btnTake, 3, 0, 1, 3)
        self.labelWinner = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelWinner.setFont(font)
        self.labelWinner.setText("")
        self.labelWinner.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWinner.setObjectName("labelWinner")
        self.gridLayout.addWidget(self.labelWinner, 5, 0, 1, 3)
        self.spinBoxTakeRockNum = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.spinBoxTakeRockNum.sizePolicy().hasHeightForWidth())
        self.spinBoxTakeRockNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBoxTakeRockNum.setFont(font)
        self.spinBoxTakeRockNum.setMinimum(1)
        self.spinBoxTakeRockNum.setMaximum(3)
        self.spinBoxTakeRockNum.setObjectName("spinBoxTakeRockNum")
        self.gridLayout.addWidget(self.spinBoxTakeRockNum, 2, 1, 1, 2)
        self.labelTakeRockNum = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.labelTakeRockNum.sizePolicy().hasHeightForWidth())
        self.labelTakeRockNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTakeRockNum.setFont(font)
        self.labelTakeRockNum.setObjectName("labelTakeRockNum")
        self.gridLayout.addWidget(self.labelTakeRockNum, 2, 0, 1, 1)
        self.btnSet = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.btnSet.sizePolicy().hasHeightForWidth())
        self.btnSet.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSet.setFont(font)
        self.btnSet.setObjectName("btnSet")
        self.gridLayout.addWidget(self.btnSet, 0, 2, 1, 1)
        self.spibBoxRockNum = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.spibBoxRockNum.sizePolicy().hasHeightForWidth())
        self.spibBoxRockNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spibBoxRockNum.setFont(font)
        self.spibBoxRockNum.setMinimum(1)
        self.spibBoxRockNum.setMaximum(256)
        self.spibBoxRockNum.setObjectName("spibBoxRockNum")
        self.gridLayout.addWidget(self.spibBoxRockNum, 0, 1, 1, 1)
        self.labelRockNum = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.labelRockNum.sizePolicy().hasHeightForWidth())
        self.labelRockNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelRockNum.setFont(font)
        self.labelRockNum.setObjectName("labelRockNum")
        self.gridLayout.addWidget(self.labelRockNum, 0, 0, 1, 1)
        self.lcdNumberRockNum = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.lcdNumberRockNum.sizePolicy().hasHeightForWidth())
        self.lcdNumberRockNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lcdNumberRockNum.setFont(font)
        self.lcdNumberRockNum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumberRockNum.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumberRockNum.setSmallDecimalPoint(False)
        self.lcdNumberRockNum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberRockNum.setProperty("value", 0.0)
        self.lcdNumberRockNum.setProperty("intValue", 0)
        self.lcdNumberRockNum.setObjectName("lcdNumberRockNum")
        self.gridLayout.addWidget(self.lcdNumberRockNum, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Псевдоним. Возвращение"))
        self.btnTake.setText(_translate("MainWindow", "Взять"))
        self.labelTakeRockNum.setText(_translate("MainWindow", "Сколько камней взять?"))
        self.btnSet.setText(_translate("MainWindow", "Задать"))
        self.labelRockNum.setText(_translate("MainWindow", "Задать количество спичек"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.rock_num = 1

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnSet.clicked.connect(self.set_rock_num)
        self.btnTake.clicked.connect(self.take_rock_num)

    def set_rock_num(self):
        self.labelWinner.clear()
        self.btnTake.setDisabled(False)
        self.listWidgetMoves.clear()
        self.rock_num = int(self.spibBoxRockNum.text())
        self.lcdNumberRockNum.display(self.rock_num)

    def solve_winner(self, who):
        self.labelWinner.setText(f'Победил {who}!')
        self.btnTake.setDisabled(True)

    def take_rock_num(self):
        rock_num = int(self.spinBoxTakeRockNum.text())
        self.rock_num -= rock_num
        self.rock_num = 0 if self.rock_num < 0 else self.rock_num
        self.lcdNumberRockNum.display(self.rock_num)
        self.listWidgetMoves.addItem(f'Игрок взял - {rock_num}')
        if not self.rock_num:
            self.solve_winner('пользователь')
            return
        self.computer_move()

    def computer_move(self):
        if self.rock_num % (3 + 1) == 0:
            rock_num = 3
        else:
            rock_num = self.rock_num % (3 + 1)
        self.rock_num -= rock_num
        self.lcdNumberRockNum.display(self.rock_num)
        self.listWidgetMoves.addItem(f'Компьтер взял - {rock_num}')
        if not self.rock_num:
            self.solve_winner('компьтер')
            return


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
