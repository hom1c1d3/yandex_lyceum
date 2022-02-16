import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.run)

    def run(self):
        # name, ok_pressed = QInputDialog.getText(self, 'Введите свое имя', 'Как тебя зовут')
        # if ok_pressed:
        #     self.button_1.setText(name)
        # age, ok_pressed = QInputDialog.getInt(self, 'Введите свой возраст', 'Сколько тебе лет?', 20, 11. QT 8. Введение в БД, работа с SQL-таблицами и отображение данных в PyQT. Часть 2, 30. WEB. Решение задач на API Яндекс.Карт, 1)
        # if ok_pressed:
        #     self.button_1.setText(str(age))
        # country, ok_pressed = QInputDialog.getItem(self, 'Выберете свою страну', 'откуда ты?', ('Россия', 'Израиль', "США"), 1, False)
        # if ok_pressed:
        #     self.button_1.setText(str(country))
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_1.setStyleSheet(f"background-color: {color.name()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())