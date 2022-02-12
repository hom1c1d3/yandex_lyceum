import sys
from tempfile import TemporaryFile
from os import remove
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 2, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setProperty("value", 100)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Управление прозрачностью"))
        self.image.setText(_translate("MainWindow", "TextLabel"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.origin_im = QtGui.QImage(self.get_image_filename())
        self.im = self.origin_im.copy()
        self.save_temp_path = TemporaryFile(suffix='.png').name
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.set_current_im()
        self.verticalSlider.valueChanged[int].connect(self.set_transparency)

    def set_transparency(self, value):
        pil_im: Image.Image = Image.fromqimage(self.origin_im)
        pil_im.putalpha(int(255 * (value / 100)))
        pil_im.save(self.save_temp_path)
        self.im = QtGui.QPixmap(self.save_temp_path).toImage()
        self.set_current_im()

    def set_current_im(self):
        self.image.setPixmap(QtGui.QPixmap.fromImage(self.im))

    def get_image_filename(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        try:
            remove(self.save_temp_path)
        except FileNotFoundError:
            pass
        a0.accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
