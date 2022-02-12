import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setPageStep(1)
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Рост хорошего настроения"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.scale = self.verticalSlider.value() / 100

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.verticalSlider.valueChanged[int].connect(self.set_value)

    def set_value(self, value):
        self.scale = value / 100
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw(painter)
        painter.end()

    def draw(self, painter):
        x, y = self.widget.x(), self.widget.y()
        painter.setPen(QtGui.QColor(255, 0, 0))
        face_width, face_height = (self.widget.height(),
                                   self.widget.height())
        face_width, face_height = int(face_width * self.scale), int(face_height * self.scale)
        painter.drawEllipse(x, y, face_width, face_height)
        eye_width, eye_height = (int(face_width / 5), int(face_height / 5))
        painter.drawEllipse(x + eye_width, y + eye_height, eye_width, eye_height)
        painter.drawEllipse(x + eye_width * 3, y + eye_height, eye_width, eye_height)
        painter.drawArc(x - face_width / 10, y - face_height / 2.9, face_width * (6/5),
                        face_height * (6/5), 360 * (11/16) * 16, 360 * (2/16) * 16)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
