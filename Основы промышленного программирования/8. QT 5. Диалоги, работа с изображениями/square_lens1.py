import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEditSide = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.lineEditSide.sizePolicy().hasHeightForWidth())
        self.lineEditSide.setSizePolicy(sizePolicy)
        self.lineEditSide.setObjectName("lineEditSide")
        self.gridLayout.addWidget(self.lineEditSide, 0, 2, 1, 1)
        self.lineEditCoeff = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.lineEditCoeff.sizePolicy().hasHeightForWidth())
        self.lineEditCoeff.setSizePolicy(sizePolicy)
        self.lineEditCoeff.setObjectName("lineEditCoeff")
        self.gridLayout.addWidget(self.lineEditCoeff, 1, 2, 1, 1)
        self.lineEditN = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.lineEditN.sizePolicy().hasHeightForWidth())
        self.lineEditN.setSizePolicy(sizePolicy)
        self.lineEditN.setObjectName("lineEditN")
        self.gridLayout.addWidget(self.lineEditN, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.drawCanvas = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.drawCanvas.sizePolicy().hasHeightForWidth())
        self.drawCanvas.setSizePolicy(sizePolicy)
        self.drawCanvas.setObjectName("drawCanvas")
        self.verticalLayout.addWidget(self.drawCanvas)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Квадрат объектив 1"))
        self.pushButton.setText(_translate("MainWindow", "Показать"))
        self.label.setText(_translate("MainWindow", "side"))
        self.label_3.setText(_translate("MainWindow", "n"))
        self.label_2.setText(_translate("MainWindow", "coeff"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.opts = None
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.pushButton.clicked.connect(self.apply_opts)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw(event, painter)
        painter.end()

    def apply_opts(self):
        try:
            side = int(self.lineEditSide.text())
            coeff = float(self.lineEditCoeff.text())
            n = int(self.lineEditN.text())
        except ValueError:
            self.opts = None
            return
        self.opts = side, coeff, n
        self.update()  # иначе не отрисовывается

    def draw(self, event, painter):
        if self.opts is None:
            return
        side, coeff, n = self.opts
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 2))
        side //= coeff
        for i in range(n):
            side = int(side * coeff)
            left_right_corner = (self.drawCanvas.width() // 2 - side // 2,
                                 self.drawCanvas.y() + self.drawCanvas.height() // 2 - side // 2)
            painter.drawRect(*left_right_corner, side, side)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
