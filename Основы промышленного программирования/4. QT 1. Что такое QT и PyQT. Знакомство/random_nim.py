import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPlus.sizePolicy().hasHeightForWidth())
        self.btnPlus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnPlus.setFont(font)
        self.btnPlus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnPlus.setObjectName("btnPlus")
        self.gridLayout.addWidget(self.btnPlus, 2, 0, 1, 1)
        self.lcdCurrentNum = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdCurrentNum.sizePolicy().hasHeightForWidth())
        self.lcdCurrentNum.setSizePolicy(sizePolicy)
        self.lcdCurrentNum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdCurrentNum.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdCurrentNum.setObjectName("lcdCurrentNum")
        self.gridLayout.addWidget(self.lcdCurrentNum, 4, 1, 1, 1)
        self.lcdMovesLeft = QtWidgets.QLCDNumber(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMovesLeft.sizePolicy().hasHeightForWidth())
        self.lcdMovesLeft.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdMovesLeft.setFont(font)
        self.lcdMovesLeft.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdMovesLeft.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdMovesLeft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdMovesLeft.setObjectName("lcdMovesLeft")
        self.gridLayout.addWidget(self.lcdMovesLeft, 3, 1, 1, 1)
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMinus.sizePolicy().hasHeightForWidth())
        self.btnMinus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnMinus.setFont(font)
        self.btnMinus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnMinus.setObjectName("btnMinus")
        self.gridLayout.addWidget(self.btnMinus, 2, 1, 1, 1)
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResult.sizePolicy().hasHeightForWidth())
        self.labelResult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.gridLayout.addWidget(self.labelResult, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(375, 150, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.labelMovesLeft = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMovesLeft.sizePolicy().hasHeightForWidth())
        self.labelMovesLeft.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMovesLeft.setFont(font)
        self.labelMovesLeft.setObjectName("labelMovesLeft")
        self.gridLayout.addWidget(self.labelMovesLeft, 3, 0, 1, 1)
        self.labelCurrentNum = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCurrentNum.sizePolicy().hasHeightForWidth())
        self.labelCurrentNum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCurrentNum.setFont(font)
        self.labelCurrentNum.setObjectName("labelCurrentNum")
        self.gridLayout.addWidget(self.labelCurrentNum, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ним наносит ответный удар "))
        self.btnPlus.setText(_translate("MainWindow", "+"))
        self.btnMinus.setText(_translate("MainWindow", "-"))
        self.labelMovesLeft.setText(_translate("MainWindow", "Осталось ходов"))
        self.labelCurrentNum.setText(_translate("MainWindow", "Текущее число"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.current_number = 0
        self.moves_left = 0
        self.game_end = False
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.new_game()
        self.btnMinus.clicked.connect(self.change_current_num)
        self.btnPlus.clicked.connect(self.change_current_num)

    def new_game(self):
        self.moves_left = 10
        self.game_end = False
        self.labelResult.setText('')
        self.current_number = random.randint(3, 64)
        self.lcdCurrentNum.display(self.current_number)
        self.btnPlus.setText(f'+{random.SystemRandom().randint(2, 13)}')
        self.btnMinus.setText(f'-{random.SystemRandom().randint(2, 13)}')
        self.lcdMovesLeft.display(self.moves_left)

    def change_current_num(self):
        if self.game_end:
            return self.new_game()
        num = int(self.sender().text())
        self.current_number += num
        self.moves_left -= 1
        self.solve_current_position()

    def solve_current_position(self):
        res = ''
        if self.current_number == 0:
            res = 'выиграли'
            self.lcdCurrentNum.display(0)
            self.lcdMovesLeft.display(self.moves_left)
        elif self.moves_left == 0:
            res = 'проиграли'
            self.lcdMovesLeft.display(0)
        if res:
            self.labelResult.setText(f'Вы {res}, начинаем новую игру')
            self.game_end = True
        self.lcdMovesLeft.display(self.moves_left)
        self.lcdCurrentNum.display(self.current_number)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
