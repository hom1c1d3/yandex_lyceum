import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')

        # self.pixmap = QPixmap('yandex.jpg')
        self.pixmap = QPixmap(QFileDialog.getOpenFileName(self, 'Выбери картинку', '', )[0])

        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(self.pixmap.size())

        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
