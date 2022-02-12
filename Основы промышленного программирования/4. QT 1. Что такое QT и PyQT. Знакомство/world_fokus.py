import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 35)
        self.setWindowTitle('Фокус со словами')

        buffer = 5
        self.first_inline = QLineEdit(self)
        self.first_inline.resize(175, 30)
        self.first_inline.move(5, 0)

        self.btn = QPushButton('->', self)
        self.btn.resize(self.first_inline.height(), self.first_inline.height())
        self.btn.move(self.first_inline.x() + self.first_inline.width() + buffer,
                      self.first_inline.y())
        self.btn.clicked.connect(self.change_word_position)

        self.second_inline = QLineEdit(self)
        self.second_inline.resize(self.first_inline.size())
        self.second_inline.move(self.btn.x() + self.btn.width() + buffer, self.btn.y())

    def change_word_position(self):
        self.second_inline.setText(self.first_inline.text())
        self.first_inline.setText('')
        self.btn.setText('<-' if self.btn.text() == '->' else '->')
        self.first_inline, self.second_inline = self.second_inline, self.first_inline


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())