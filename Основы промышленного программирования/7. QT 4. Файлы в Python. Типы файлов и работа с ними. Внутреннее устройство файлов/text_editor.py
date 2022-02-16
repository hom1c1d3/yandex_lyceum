import sys
from random import randrange
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class TextBrowserSample(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('TextBrowserSample.ui', self)
        self.loadButton.clicked.connect(self.load_file)
        self.processButton.clicked.connect(self.process_data)

    def load_file(self):
        try:
            with open('input.txt', 'r', encoding='utf8') as f:
                self.inputText.setText(f.read())
        except FileNotFoundError as e:
            self.statusBar().showMessage('Файл не найден')

    def process_data(self):
        # data = self.inputText.toPlainText()
        # self.outputText.setText(data[::-1])
        self.color_text()

    def color_text(self):
        data = self.inputText.toPlainText()
        HTML = ""
        for i in data:
            color = '#{:06x}'.format(randrange(0, 0xFFFFFF))
            HTML += "<font color='{}' size='{}'>{}</font>".format(
                color, randrange(1, 10), i
            )
        self.outputText.setText(HTML)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextBrowserSample()
    ex.show()
    sys.exit(app.exec())
