import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnColorNumber = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnColorNumber.sizePolicy().hasHeightForWidth())
        self.btnColorNumber.setSizePolicy(sizePolicy)
        self.btnColorNumber.setIconSize(QtCore.QSize(20, 20))
        self.btnColorNumber.setAutoDefault(False)
        self.btnColorNumber.setObjectName("btnColorNumber")
        self.verticalLayout.addWidget(self.btnColorNumber)
        self.drawCanvas = QtWidgets.QWidget(self.centralwidget)
        self.drawCanvas.setObjectName("drawCanvas")
        self.verticalLayout.addWidget(self.drawCanvas)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генерация флага"))
        self.btnColorNumber.setText(_translate("MainWindow", "Ввести количество цветов флага"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.colors = ()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnColorNumber.clicked.connect(self.get_color_number)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def get_color_number(self):
        number, ok_pressed = QtWidgets.QInputDialog.getInt(self, "Введите количество цветов",
                                                           "Сколько цветов?", value=3, min=2, step=1)
        if ok_pressed:
            self.colors = tuple(self.get_random_colors(number))
            self.update()

    def draw(self, painter):
        elem_width, elem_height = 120, 30
        x, y = (self.drawCanvas.width() // 2 - elem_width // 2,
                (self.drawCanvas.y()
                 + self.drawCanvas.height() // 2
                 - (elem_height * len(self.colors)) // 2))
        for ind, color in enumerate(self.colors):
            painter.setBrush(QtGui.QColor(*color))
            painter.drawRect(x, y + elem_height * ind, elem_width, elem_height)

    @staticmethod
    def get_random_colors(num):
        for _ in range(num):
            yield tuple(random.randint(0, 255) for _ in range(3))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
