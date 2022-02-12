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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEditM = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditM.setObjectName("lineEditM")
        self.horizontalLayout.addWidget(self.lineEditM)
        self.btnDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnDraw.setObjectName("btnDraw")
        self.horizontalLayout.addWidget(self.btnDraw)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.drawCanvas = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Не квадрат-объектив"))
        self.label.setText(_translate("MainWindow", "K="))
        self.label_2.setText(_translate("MainWindow", "N="))
        self.label_3.setText(_translate("MainWindow", "M="))
        self.btnDraw.setText(_translate("MainWindow", "Рисовать"))


def get_third_side(a, b, angle_degrees):
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle_degrees)))
    return c


def get_second_angle(a, c, alpha):
    sin_beta = (a * math.sin(math.radians(alpha))) / c
    beta = math.asin(sin_beta)
    return math.degrees(beta)


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
            m = int(self.lineEditM.text())
            color = self.get_color()
        except ValueError:
            self.opts = None
            return
        self.opts = k, n, m, color
        self.update()  # иначе не отрисовывается

    def get_color(self):
        color = QtWidgets.QColorDialog.getColor(QtGui.QColor('red'), self)
        if color.isValid():
            return color
        raise ValueError

    def draw(self, event, painter):
        opts = self.opts
        if opts is None:
            return
        k, n, m, color = opts
        painter.setPen(QtGui.QPen(color, 2))
        circle_diameter = min(self.drawCanvas.width(), self.drawCanvas.height())
        sides = m
        deg = 360 / sides
        painter.translate(self.drawCanvas.x(), self.drawCanvas.y())
        painter.translate((self.drawCanvas.width() // 2) - (circle_diameter // 2), 0)
        painter.translate(circle_diameter, circle_diameter / 2)
        painter.rotate(deg / 2)
        for i in range(n):
            side = get_third_side(circle_diameter / 2, circle_diameter / 2, deg)
            for j in range(sides):
                painter.rotate(-deg)
                painter.drawLine(0, 0, 0, int(-side))
                painter.translate(0, -side)
            painter.translate(0, side - side * k)
            less_ratio_side, larger_ratio_side = side - (side * k), side * k
            next_side = get_third_side(less_ratio_side, larger_ratio_side, 180 - deg)
            rotate_angle = get_second_angle(less_ratio_side, next_side, 180 - deg)
            painter.rotate(rotate_angle)
            painter.scale(next_side / side, next_side / side)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
