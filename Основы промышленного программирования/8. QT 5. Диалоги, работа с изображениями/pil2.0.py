import sys
from tempfile import TemporaryFile
from os import remove
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnAll = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btnAll.sizePolicy().hasHeightForWidth())
        self.btnAll.setSizePolicy(sizePolicy)
        self.btnAll.setObjectName("btnAll")
        self.gridLayout.addWidget(self.btnAll, 3, 0, 1, 1)
        self.btnB = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btnB.sizePolicy().hasHeightForWidth())
        self.btnB.setSizePolicy(sizePolicy)
        self.btnB.setObjectName("btnB")
        self.gridLayout.addWidget(self.btnB, 2, 0, 1, 1)
        self.btnG = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btnG.sizePolicy().hasHeightForWidth())
        self.btnG.setSizePolicy(sizePolicy)
        self.btnG.setObjectName("btnG")
        self.gridLayout.addWidget(self.btnG, 1, 0, 1, 1)
        self.btnR = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btnR.sizePolicy().hasHeightForWidth())
        self.btnR.setSizePolicy(sizePolicy)
        self.btnR.setObjectName("btnR")
        self.gridLayout.addWidget(self.btnR, 0, 0, 1, 1)
        self.image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 1, 4, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCouterclockwise = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btnCouterclockwise.sizePolicy().hasHeightForWidth())
        self.btnCouterclockwise.setSizePolicy(sizePolicy)
        self.btnCouterclockwise.setObjectName("btnCouterclockwise")
        self.horizontalLayout.addWidget(self.btnCouterclockwise)
        self.btnClockwise = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.btnClockwise.sizePolicy().hasHeightForWidth())
        self.btnClockwise.setSizePolicy(sizePolicy)
        self.btnClockwise.setObjectName("btnClockwise")
        self.horizontalLayout.addWidget(self.btnClockwise)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIL 2.0"))
        self.btnAll.setText(_translate("MainWindow", "ALL"))
        self.btnB.setText(_translate("MainWindow", "B"))
        self.btnG.setText(_translate("MainWindow", "G"))
        self.btnR.setText(_translate("MainWindow", "R"))
        self.image.setText(_translate("MainWindow", "TextLabel"))
        self.btnCouterclockwise.setText(_translate("MainWindow", "Против часовой стрелке"))
        self.btnClockwise.setText(_translate("MainWindow", "По часовой стрелке"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.origin_im = QtGui.QImage(self.get_image_filename())
        self.angle = 0
        self.im = self.origin_im.copy()
        self.save_temp_path = TemporaryFile(suffix='.png').name
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.set_current_im()
        for i in (self.btnR, self.btnG, self.btnB):
            i.clicked.connect(self.set_channel)
        self.btnAll.clicked.connect(self.set_all_channels)
        for i in (self.btnClockwise, self.btnCouterclockwise):
            i.clicked.connect(self.rotate_image)

    def set_all_channels(self):
        pil_im = Image.fromqimage(self.origin_im.copy())
        pil_im = pil_im.rotate(self.angle, expand=True)
        pil_im.save(self.save_temp_path)
        self.im = QtGui.QPixmap(self.save_temp_path).toImage()
        self.set_current_im()

    def set_channel(self):
        r, g, b = {'R': (1, 0, 0), 'G': (0, 1, 0), 'B': (0, 0, 1)}[self.sender().text()]
        pil_im: Image.Image = Image.fromqimage(self.origin_im)
        pil_im_dropped_channel = pil_im.copy().convert("RGB", matrix=(r, 0, 0, 0,
                                                                      0, g, 0, 0,
                                                                      0, 0, b, 0)
                                                       )

        pil_im_dropped_channel = pil_im_dropped_channel.rotate(self.angle, expand=True)
        pil_im_dropped_channel.save(self.save_temp_path)
        self.im = QtGui.QPixmap(self.save_temp_path).toImage()
        self.set_current_im()

    def set_current_im(self):
        self.image.setPixmap(QtGui.QPixmap.fromImage(self.im))

    def get_image_filename(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

    def rotate_image(self):
        if self.sender().objectName().endswith('Clockwise'):
            angle = -90
        else:
            angle = 90
        self.angle += angle
        pil_im: Image.Image = Image.fromqimage(self.im)
        pil_im_rotated = pil_im.copy().rotate(angle, expand=True)
        pil_im_rotated.save(self.save_temp_path)
        self.im = QtGui.QPixmap(self.save_temp_path).toImage()
        self.set_current_im()

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
