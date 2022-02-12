import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 150)
        self.setWindowTitle('Вычисление выражений')

        buffer = 7

        self.first_num_label = QLabel('Первое число (целое):', self)
        self.first_num_label.move(buffer, 10)

        self.first_num_inline = QLineEdit(self)
        self.first_num_inline.resize(125, 25)
        self.first_num_inline.move(buffer,
                                   (self.first_num_label.y() +
                                    self.first_num_label.height() - buffer * 2))

        self.second_num_label = QLabel('Второе число (целое): ', self)
        self.second_num_label.move(self.first_num_inline.x(),
                                   (self.first_num_inline.y() +
                                    self.first_num_inline.height() + buffer * 4))

        self.second_num_inline = QLineEdit(self)
        self.second_num_inline.resize(self.first_num_inline.size())
        self.second_num_inline.move(self.second_num_label.x(),
                                    (self.second_num_label.y() +
                                     self.second_num_label.height() - buffer * 2))

        self.btn = QPushButton('->', self)
        first_num_inline_bottom_y = (self.first_num_inline.y() + self.first_num_inline.height())
        second_num_inline_top_y = self.second_num_inline.y()
        self.btn.resize(self.first_num_inline.width() // 2, self.first_num_inline.height())
        self.btn.move(self.x() // 2 + self.btn.width() // 2, ((first_num_inline_bottom_y +
                                                               second_num_inline_top_y) // 2
                                                              - self.btn.height() // 2))
        self.btn.clicked.connect(self.solve_expressions)

        inline_btn_delta = self.btn.x() - (self.first_num_inline.x() + self.first_num_inline.width())

        expression_result_labels = []
        for ind, i in enumerate(('сумма', 'разность', "произведение", 'частное')):
            expression_result_label = QLabel(i.capitalize() + ':', self)
            expression_result_label.move(self.btn.x() + self.btn.width() + inline_btn_delta,
                                         self.first_num_label.y() + self.height() // 5 * ind)
            expression_result_labels.append(expression_result_label)

        self.expression_result_lcds = []
        for i in expression_result_labels:
            expression_result_lcd = QLCDNumber(self)
            expression_result_lcd.move(i.x() + i.width(), i.y())
            self.expression_result_lcds.append(expression_result_lcd)

        self.resize(self.expression_result_lcds[0].x() + self.expression_result_lcds[0].width(),
                    self.height())

    def solve_expressions(self):
        try:
            a, b = int(self.first_num_inline.text()), int(self.second_num_inline.text())
        except ValueError:
            return
        for sign, lcd in zip(('+', '-', '*', '/'), self.expression_result_lcds):
            expression = f'{a}{sign}{b}'
            try:
                res = eval(expression)
            except ZeroDivisionError:
                res = 'Error'
            lcd.display(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
