import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 65)
        self.setWindowTitle('Вычисление выражений')

        buffer = 5

        self.expression_label = QLabel('Выражение:', self)
        self.expression_label.move(buffer, 10)

        self.first_inline = QLineEdit(self)
        self.first_inline.resize(175, 30)
        self.first_inline.move(buffer, self.expression_label.height())

        self.btn = QPushButton('->', self)
        self.btn.resize(self.first_inline.height(), self.first_inline.height())
        self.btn.move(self.first_inline.x() + self.first_inline.width() + buffer,
                      self.first_inline.y())
        self.btn.clicked.connect(self.solve_expression)

        self.second_inline = QLineEdit(self)
        self.second_inline.resize(self.first_inline.size())
        self.second_inline.move(self.btn.x() + self.btn.width() + buffer, self.btn.y())

        self.result_label = QLabel('Результат: ', self)
        self.result_label.move(self.second_inline.x(), self.expression_label.y())

    def solve_expression(self):
        expression = self.first_inline.text()
        result = eval(expression)
        self.second_inline.setText(str(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())