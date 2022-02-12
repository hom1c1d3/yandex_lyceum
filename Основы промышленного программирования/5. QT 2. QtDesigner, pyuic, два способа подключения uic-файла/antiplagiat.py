import sys
import difflib
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTriggerPoint = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTriggerPoint.sizePolicy().hasHeightForWidth())
        self.labelTriggerPoint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelTriggerPoint.setFont(font)
        self.labelTriggerPoint.setObjectName("labelTriggerPoint")
        self.horizontalLayout.addWidget(self.labelTriggerPoint)
        self.doubleSpinBoxTriggerPoint = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBoxTriggerPoint.sizePolicy().hasHeightForWidth())
        self.doubleSpinBoxTriggerPoint.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBoxTriggerPoint.setFont(font)
        self.doubleSpinBoxTriggerPoint.setProperty("value", 85.0)
        self.doubleSpinBoxTriggerPoint.setObjectName("doubleSpinBoxTriggerPoint")
        self.horizontalLayout.addWidget(self.doubleSpinBoxTriggerPoint)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelText1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelText1.setFont(font)
        self.labelText1.setObjectName("labelText1")
        self.gridLayout.addWidget(self.labelText1, 0, 0, 1, 1)
        self.labelText2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelText2.setFont(font)
        self.labelText2.setObjectName("labelText2")
        self.gridLayout.addWidget(self.labelText2, 0, 1, 1, 1)
        self.plainTextEdit1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit1.setFont(font)
        self.plainTextEdit1.setPlaceholderText("")
        self.plainTextEdit1.setObjectName("plainTextEdit1")
        self.gridLayout.addWidget(self.plainTextEdit1, 1, 0, 1, 1)
        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit2.setFont(font)
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.gridLayout.addWidget(self.plainTextEdit2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btnCompare = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCompare.setFont(font)
        self.btnCompare.setObjectName("btnCompare")
        self.verticalLayout.addWidget(self.btnCompare)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Антиплагиат v0.0001"))
        self.labelTriggerPoint.setText(_translate("MainWindow", "Порог срабатывания (%)"))
        self.labelText1.setText(_translate("MainWindow", "Текст 1"))
        self.labelText2.setText(_translate("MainWindow", "Текст 2"))
        self.plainTextEdit1.setPlainText(_translate("MainWindow", "x = []\n"
"merila = {\"аршины\": 0.71, \"метры\": 1, \"футы\": 0.3}\n"
"for i in range(3):\n"
"    vel = input()\n"
"    val = float(input())\n"
"    x.append([vel, val, val * merila[vel]])\n"
"x.sort(key=lambda i: (i[2], [0]))\n"
"for i in x:\n"
"    print(i[1], \" (\", [0], \")\", sep=\"\")"))
        self.plainTextEdit2.setPlainText(_translate("MainWindow", "x = []\n"
"\n"
"merila1 = {\"аршины\": 0.71, \"метры\": 1, \"футы\": 0.3}\n"
"for i in range(3):\n"
"    vel1 = input()\n"
"    val1 = float(input())\n"
"    x1.append([vel, val, val * merila[vel]])\n"
"x1.sort(key=lambda i: (i[2], [0]))\n"
"for i in x:\n"
"    print(i[1], \" (\", [0], \")\", sep=\"\")"))
        self.btnCompare.setText(_translate("MainWindow", "Сравнить"))


def check_similarity(text1, text2):
    if not text1 or not text2:
        return 0.
    ratios = []
    for a, b in zip(filter(None, text1.splitlines()), filter(None, text2.splitlines())):
        ratio = difflib.SequenceMatcher(None, a, b).ratio()
        if not ratio:
            continue
        ratios.append(ratio)
    res = sum(ratios) / len(ratios)
    return res


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnCompare.clicked.connect(self.compare)

    def compare(self):
        text1, text2 = self.plainTextEdit1.toPlainText(), self.plainTextEdit2.toPlainText()
        similarity = check_similarity(text1, text2)
        self.display_similarity(similarity)

    def display_similarity(self, similarity):
        color = 'red' if similarity >= self.doubleSpinBoxTriggerPoint.value() / 100 else 'green'
        self.statusBar.setStyleSheet(f"background-color: {color};")
        self.statusBar.showMessage(f'Код похож на {similarity:.2%}')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
