import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 290, 40)
        self.setWindowTitle('Арифмометр')

        buffer = 5

        self.first_num_inline = QLineEdit(self)
        self.first_num_inline.resize(60, 30)
        self.first_num_inline.move(buffer, buffer)
        # self.first_num_inline.setReadOnly(True)

        for ind, i in enumerate(('+', '-', '*')):
            button = QPushButton(i, self)
            button.resize(self.first_num_inline.width() // 2, self.first_num_inline.height())
            first_inline_offset = (self.first_num_inline.x() +
                                   self.first_num_inline.width() + buffer // 3)
            button.move(first_inline_offset + button.width() * ind, self.first_num_inline.y())
            button.clicked.connect(self.solve_expression)

        self.second_num_inline = QLineEdit(self)
        self.second_num_inline.resize(self.first_num_inline.size())
        self.second_num_inline.move(button.x() + button.width() + buffer // 3,
                                    self.first_num_inline.y())

        equal_sign = QLabel('=', self)
        equal_sign.resize(equal_sign.sizeHint())
        equal_sign.move(self.second_num_inline.x() + self.second_num_inline.width(),
                        self.second_num_inline.y() + self.second_num_inline.height() // 4)

        self.result_inline = QLineEdit(self)
        self.result_inline.resize(self.second_num_inline.size())
        self.result_inline.move(equal_sign.x() + equal_sign.width(), self.second_num_inline.y())
        self.result_inline.setDisabled(True)

    def solve_expression(self):
        sign = self.sender().text()
        expression = f'{self.first_num_inline.text()}{sign}{self.second_num_inline.text()}'
        try:
            res = eval(expression)
        except Exception:
            res = ''
        self.result_inline.setText(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
