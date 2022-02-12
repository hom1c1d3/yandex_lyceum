import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Супрематизм"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.key_pressed = None
        self.key_pos = 0, 0
        self.shape_size = 1, 1
        self.color = 0, 0, 0
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.resize(random.randint(128, 1920), random.randint(128, 1080))

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        if self.key_pressed is None:
            return
        painter.setBrush(QtGui.QColor(*self.color))
        if self.key_pressed == QtCore.Qt.LeftButton:
            self.draw_circle(painter)
        elif self.key_pressed == QtCore.Qt.RightButton:
            self.draw_square(painter)
        elif self.key_pressed == QtCore.Qt.Key_Space:
            self.draw_triangle(painter)

    def draw_triangle(self, painter):
        x, y = self.key_pos
        r, _ = self.shape_size
        r = int(r)
        a = QtCore.QPoint(x, y - r)
        half_side = int((r**2 - (.5*r)**2)**.5)
        h = int(y + .5*r)
        b = QtCore.QPoint(x - half_side, h)
        c = QtCore.QPoint(x + half_side, h)
        painter.drawPolygon(a, b, c)

    def draw_square(self, painter):
        painter.drawRect(*self.key_pos, *self.shape_size)

    def draw_circle(self, painter):
        painter.drawEllipse(QtCore.QPoint(*self.key_pos), *self.shape_size)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == QtCore.Qt.Key_Space:
            self.update_pos()
            self.color = [random.randint(0, 255) for _ in range(3)]
            self.key_pressed = a0.key()
            self.update()

    def update_pos(self):
        p = self.mapFromGlobal(self.cursor().pos())
        self.key_pos = p.x(), p.y()
        x, y = self.key_pos
        x, y = min(max(x, 0), self.width()), min(max(y, 0), self.height())
        x, y = (x if x < self.width() // 2 else self.width() - x,
                y if y < self.height() // 2 else self.height() - y)
        radius = max(min(x, y), 1)
        radius = random.randint(1, radius)
        self.shape_size = radius, radius

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.key_pressed = a0.button()
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.update_pos()
        radius = self.shape_size[0]
        if self.key_pressed == QtCore.Qt.RightButton:
            self.key_pos = a0.x() - radius, a0.y() - radius
            radius = radius * 2
        self.shape_size = radius, radius
        self.update()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
