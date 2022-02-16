import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditK = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditK.setObjectName("lineEditK")
        self.horizontalLayout.addWidget(self.lineEditK)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditN = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditN.setObjectName("lineEditN")
        self.horizontalLayout.addWidget(self.lineEditN)
        self.btnDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnDraw.setObjectName("btnDraw")
        self.horizontalLayout.addWidget(self.btnDraw)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.drawCanvas = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.drawCanvas.sizePolicy().hasHeightForWidth())
        self.drawCanvas.setSizePolicy(sizePolicy)
        self.drawCanvas.setObjectName("drawCanvas")
        self.verticalLayout.addWidget(self.drawCanvas)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Квадрат-объектив"))
        self.label.setText(_translate("MainWindow", "K="))
        self.label_2.setText(_translate("MainWindow", "N="))
        self.btnDraw.setText(_translate("MainWindow", "Рисовать"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.opts = None
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnDraw.clicked.connect(self.apply_opts)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw(event, painter)
        painter.end()

    def apply_opts(self):
        try:
            k = float(self.lineEditK.text())
            n = int(self.lineEditN.text())
        except ValueError:
            self.opts = None
            return
        self.opts = k, n
        self.update()  # иначе не отрисовывается

    def draw(self, event, painter):
        if self.opts is None:
            return
        k, n = self.opts
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 2))
        side = int(self.drawCanvas.width() / 3)
        painter.translate(self.drawCanvas.width() // 2 - side // 2,
                          self.drawCanvas.y() + self.drawCanvas.height() // 2 - side // 2)
        painter.drawRect(0, 0, side, side)
        pen_width = 2
        for i in range(n):
            painter.translate(side - (side * k), 0)
            painter.rotate(math.degrees(math.atan((side - side * k) / (side * k))))
            scale_k = math.sqrt((side - (side * k)) ** 2 + (side * k) ** 2) / side
            painter.scale(scale_k, scale_k)
            painter.drawRect(0, 0, side, side)
            pen_width = pen_width / scale_k
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), pen_width))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
