import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 620)
        MainWindow.setMinimumSize(QtCore.QSize(420, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 3, 2, 1, 1)
        self.btnMultiplying = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnMultiplying.sizePolicy().hasHeightForWidth())
        self.btnMultiplying.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnMultiplying.setFont(font)
        self.btnMultiplying.setObjectName("btnMultiplying")
        self.gridLayout.addWidget(self.btnMultiplying, 3, 3, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 3, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 4, 2, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 4, 0, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet("")
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btnDivision = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnDivision.sizePolicy().hasHeightForWidth())
        self.btnDivision.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnDivision.setFont(font)
        self.btnDivision.setObjectName("btnDivision")
        self.gridLayout.addWidget(self.btnDivision, 2, 3, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btnClearEntry = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnClearEntry.sizePolicy().hasHeightForWidth())
        self.btnClearEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnClearEntry.setFont(font)
        self.btnClearEntry.setObjectName("btnClearEntry")
        self.gridLayout.addWidget(self.btnClearEntry, 5, 2, 1, 1)
        self.btnSubtraction = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnSubtraction.sizePolicy().hasHeightForWidth())
        self.btnSubtraction.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnSubtraction.setFont(font)
        self.btnSubtraction.setObjectName("btnSubtraction")
        self.gridLayout.addWidget(self.btnSubtraction, 4, 3, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 3, 1, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 5, 1, 1, 1)
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.gridLayout.addWidget(self.btnClear, 5, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 4, 1, 1, 1)
        self.btnEqual = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnEqual.sizePolicy().hasHeightForWidth())
        self.btnEqual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnEqual.setFont(font)
        self.btnEqual.setObjectName("btnEqual")
        self.gridLayout.addWidget(self.btnEqual, 6, 2, 1, 2)
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnDot.sizePolicy().hasHeightForWidth())
        self.btnDot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnDot.setFont(font)
        self.btnDot.setObjectName("btnDot")
        self.gridLayout.addWidget(self.btnDot, 6, 0, 1, 1)
        self.btnNegative = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnNegative.sizePolicy().hasHeightForWidth())
        self.btnNegative.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnNegative.setFont(font)
        self.btnNegative.setObjectName("btnNegative")
        self.gridLayout.addWidget(self.btnNegative, 6, 1, 1, 1)
        self.labelResultExpression = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.labelResultExpression.sizePolicy().hasHeightForWidth())
        self.labelResultExpression.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelResultExpression.setFont(font)
        self.labelResultExpression.setStyleSheet("")
        self.labelResultExpression.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelResultExpression.setWordWrap(False)
        self.labelResultExpression.setObjectName("labelResultExpression")
        self.gridLayout.addWidget(self.labelResultExpression, 1, 0, 1, 4)
        self.btnAddition = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btnAddition.sizePolicy().hasHeightForWidth())
        self.btnAddition.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnAddition.setFont(font)
        self.btnAddition.setObjectName("btnAddition")
        self.gridLayout.addWidget(self.btnAddition, 5, 3, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.labelHistory = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.labelHistory.sizePolicy().hasHeightForWidth())
        self.labelHistory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelHistory.setFont(font)
        self.labelHistory.setText("")
        self.labelHistory.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.labelHistory.setObjectName("labelHistory")
        self.gridLayout.addWidget(self.labelHistory, 0, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btnMultiplying.setText(_translate("MainWindow", "×"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btnDivision.setText(_translate("MainWindow", "÷"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnClearEntry.setText(_translate("MainWindow", "CE"))
        self.btnSubtraction.setText(_translate("MainWindow", "-"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnClear.setText(_translate("MainWindow", "C"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btnEqual.setText(_translate("MainWindow", "="))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnNegative.setText(_translate("MainWindow", "±"))
        self.labelResultExpression.setText(_translate("MainWindow", "0"))
        self.btnAddition.setText(_translate("MainWindow", "+"))
        self.btn7.setText(_translate("MainWindow", "7"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.expression = []
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.expression = [self.labelResultExpression.text()]
        for num_btn in (getattr(self, i) for i in self.__dict__ if i[-1].isdecimal()):
            num_btn: QtWidgets.QPushButton
            num_btn.clicked.connect(self.append_num)

        for sign in ('÷', '×', '-', '+'):
            for btn in (getattr(self, j) for j in self.__dict__ if j.startswith('btn')):
                if btn.text() == sign:
                    btn.clicked.connect(self.add_sign)

        self.btnEqual.clicked.connect(self.solve)
        self.btnDot.clicked.connect(self.append_num)
        self.btnNegative.clicked.connect(self.negative)
        self.btnClearEntry.clicked.connect(self.clear_entry)
        self.btnClear.clicked.connect(self.clear_global)

    def clear_global(self):
        self.labelHistory.clear()
        self.expression = ['0']
        self.labelResultExpression.setText(self.expression[-1])

    def clear_entry(self):
        if self.is_num(self.expression[-1]):
            self.expression[-1] = '0'
        elif self.expression[-1] != '':
            self.expression.append('0')
        if self.labelHistory.text().endswith('='):
            self.labelHistory.clear()
        self.labelResultExpression.setText(self.expression[-1])

    def negative(self):
        try:
            res = eval(f'-{self.expression[-1]}')
            self.expression[-1] = str(res)
        except SyntaxError:
            self.expression.append('0')
        self.labelResultExpression.setText(self.expression[-1])

    def solve_previous_text(self):
        if self.expression[-1] == '0':
            self.expression[-1] = ''
        if self.is_num(self.expression[-1]):
            prev_text = self.expression[-1]
        else:
            prev_text = ''
            if self.expression[-1] != '':
                self.expression.append('')
        return prev_text

    def clear_previous(self):
        if self.labelHistory.text().endswith('='):
            self.labelHistory.clear()
            self.labelResultExpression.clear()
            self.expression = ['']

    def append_num(self):
        self.clear_previous()
        prev_text = self.solve_previous_text()
        if self.sender().text() == '.':
            if self.expression[-1].endswith('.'):
                return
            if self.expression[-1] == '':
                self.expression[-1] = '0'
                prev_text = '0'
        num = self.sender().text()
        self.expression[-1] += num
        self.labelResultExpression.setText(prev_text + num)

    def display_history(self):
        self.solve_history()
        self.labelHistory.clear()
        self.labelHistory.setText(' '.join(self.expression))

    @staticmethod
    def get_python_expression(expression):
        trans_table = str.maketrans({'÷': '/', '×': '*'})
        expression = expression.translate(trans_table)
        return expression

    def solve_history(self):
        history_result = self.solve_expression((''.join(self.expression[:-1])))
        if history_result == 'Error':
            self.expression = ['']
            self.labelResultExpression.setText(history_result)
        else:
            self.expression = [str(history_result), self.expression[-1]]

    def add_sign(self):
        sign = self.sender().text()
        if self.expression[-1] in ('÷', '×', '-', '+'):
            self.expression.pop()
        self.expression.append(sign)
        self.display_history()

    def solve_expression(self, expression):
        try:
            res = eval(self.get_python_expression(expression))
            res = round(res, 15)
            res = eval(f'{res:e}')
            if len(str(res)) > 14:
                res = f'{res:e}'
            else:
                res = str(res)
            return res
        except (NameError, SyntaxError, ZeroDivisionError):
            return 'Error'

    @staticmethod
    def is_num(string):
        try:
            if type(eval(string)) not in (int, float):
                return SyntaxError
        except SyntaxError:
            return False
        return True

    def solve(self):
        if not self.is_num(self.expression[-1]):
            self.expression = self.expression[:-1]
        expression = ' '.join(self.expression)
        result = self.solve_expression(expression)
        if result.endswith('.0'):
            result = int(float(result))
        result = str(result)
        self.expression = [result]
        self.labelHistory.setText(expression + ' =')
        self.labelResultExpression.setText(result)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
