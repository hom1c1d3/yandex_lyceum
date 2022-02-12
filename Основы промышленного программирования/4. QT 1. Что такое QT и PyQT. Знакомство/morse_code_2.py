import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


EN = {('m', '−−'), ('p', '.−−.'), ('g', '−−.'), ('i', '..'), ('l', '.−..'), ('x', '−..−'),
      ('w', '.−−'), ('q', '−−.−'), ('r', '.−.'), ('u', '..−'), ('a', '.−'), ('y', '−.−−'),
      ('n', '−.'), ('v', '...−'), ('z', '−−..'), ('j', '.−−−'), ('o', '−−−'), ('k', '−.−'),
      ('h', '....'), ('e', '.'), ('b', '−...'), ('c', '−.−.'), ('d', '−..'), ('f', '..−.'),
      ('s', '...'), ('t', '−')}


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 120)
        self.setWindowTitle('Азбука Морзе 2')

        buffer = 5

        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        btn_size = QPushButton(alphabet[0]).size().__class__(30, 30)
        row_len = (buffer + btn_size.width() * len(alphabet) + buffer)
        alphabet_iter = iter(alphabet)
        for row_ind in range(row_len // self.width() + 1):
            for i in range(0, ((2 * buffer + self.width()) // btn_size.width()) - 1):
                try:
                    letter = next(alphabet_iter)
                except StopIteration:
                    break
                button = QPushButton(letter, self)
                button.resize(btn_size)
                button.move(buffer + i * btn_size.width(), 2 * buffer + row_ind * btn_size.height())
                button.clicked.connect(self.morse_encode)

        self.morse_line = QLineEdit(self)
        self.morse_line.resize(self.width() - 2 * buffer, btn_size.height())
        self.morse_line.move(buffer, button.y() + button.height() + 2 * buffer)

    def morse_encode(self):
        btn = self.sender()
        morse_code = dict(EN)[btn.text()]
        self.morse_line.setText(self.morse_line.text() + morse_code)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
