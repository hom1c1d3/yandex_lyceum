import sys

from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 120)
        self.setWindowTitle('Прятки для виджетов')

        buffer = 5

        for i in range(1, 5):
            check_box = QCheckBox(f'edit{i}', self)
            inline = QLineEdit(f'Поле edit{i}', self)
            inline.hide()
            check_box.inline = inline
            check_box.move(buffer, buffer + check_box.height() * (i - 1))
            inline.move(check_box.x() + check_box.width() + buffer, check_box.y())
            check_box.stateChanged.connect(self.check_box_checked)

    def check_box_checked(self):
        if self.sender().isChecked():
            self.sender().inline.show()
        else:
            self.sender().inline.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
