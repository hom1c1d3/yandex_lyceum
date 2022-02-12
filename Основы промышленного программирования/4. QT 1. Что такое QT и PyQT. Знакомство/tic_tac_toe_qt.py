import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QLabel


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.current_move = 'X'
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('Крестики-нолики')

        buffer = 5

        btn_size = QPushButton().size().__class__(80, 80)

        left_button_x, left_button_y = (
            self.width() // 2 - btn_size.width() // 2 - buffer - btn_size.width(),
            self.height() // 2 - btn_size.height() - buffer - btn_size.height())

        self.button_field = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton(self)
                button.resize(btn_size)
                button.move(left_button_x + (btn_size.width() + buffer) * j,
                            left_button_y + (btn_size.height() + buffer) * i)
                button.clicked.connect(self.set_move_to_button)
                row.append(button)
            self.button_field.append(row)

        self.x_radio_button = QRadioButton('X', self)
        self.x_radio_button.resize(self.x_radio_button.sizeHint())
        self.x_radio_button.move((self.button_field[0][1].x()
                                  + btn_size.width() // 2 - self.x_radio_button.width()),
                                 ((self.button_field[0][1].y() - buffer) // 2
                                  - self.x_radio_button.height() // 2))
        self.x_radio_button.setChecked(True)
        self.o_radio_button = QRadioButton('O', self)
        self.o_radio_button.move(self.x_radio_button.x() + self.x_radio_button.width(),
                                 self.x_radio_button.y())
        self.x_radio_button.clicked.connect(self.choose_current_move)
        self.o_radio_button.clicked.connect(self.choose_current_move)

        new_game_button = QPushButton('Новая игра', self)
        new_game_button.resize(new_game_button.sizeHint())
        field_bottom_buffered_y = (self.button_field[2][1].y() + btn_size.height() + buffer)
        new_game_button.move((self.button_field[2][1].x() +
                              btn_size.width() // 2 - new_game_button.width() // 2),
                             (field_bottom_buffered_y + (self.height() - field_bottom_buffered_y)
                              // 2 - (new_game_button.height() // 2)))
        new_game_button.clicked.connect(self.new_game)

        self.game_res_label = QLabel('Выиграл O!', self)
        self.game_res_label.resize(self.game_res_label.sizeHint())
        self.game_res_label.move((self.button_field[2][1].x() +
                                  btn_size.width() // 2 - self.game_res_label.width() // 2),
                                 ((field_bottom_buffered_y
                                   + (new_game_button.y() - field_bottom_buffered_y) // 2)
                                  - self.game_res_label.height() // 2))
        self.game_res_label.hide()

    def new_game(self):
        for i in self.button_field:
            for j in i:
                j.setText('')
                j.setDisabled(False)
        self.current_move = (self.x_radio_button.text()
                             if self.x_radio_button.isChecked()
                             else self.o_radio_button.text())
        self.game_res_label.hide()

    def choose_current_move(self):
        if self.is_not_game_running():
            self.current_move = self.sender().text()
            self.new_game()

    def check_field(self, field):
        for row in field:
            row = list(set(row))
            if len(row) == 1 and row[0] != '':
                return row[0]
        for col in zip(*field):
            col = list(set(col))
            if len(col) == 1 and col[0] != '':
                return col[0]
        diagonal1 = {field[i][i] for i in range(3)}
        diagonal2 = {field[i][-(i + 1)] for i in range(3)}
        for i in (diagonal1, diagonal2):
            if len(i) == 1 and i != {'', }:
                return list(i)[0]
        tie_field = [i for i in field for j in i if j != '']
        return 'D' if len(tie_field) == 3 ** 2 else None

    def disable_field(self):
        for i in self.button_field:
            for j in i:
                j.setDisabled(True)

    def solve_current_position(self):
        game_field_text = [[j.text() for j in i] for i in self.button_field]
        check = self.check_field(game_field_text)
        if check is None:
            return
        if check != 'D':
            self.game_res_label.setText(f'Выиграл {check}!')
        else:
            self.game_res_label.setText('Ничья!')
        self.game_res_label.show()
        self.disable_field()

    def set_move_to_button(self):
        if not self.sender().text():
            self.sender().setText(self.current_move)
            self.current_move = 'O' if self.current_move == 'X' else 'X'
        self.solve_current_position()

    def is_not_game_running(self):
        return all(not j.isEnabled() or not j.text() for i in self.button_field for j in i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
