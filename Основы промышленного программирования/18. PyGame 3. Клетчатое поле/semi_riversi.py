import random
import pygame


class Board:

    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
        # дефолтные значения
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = {0: pygame.Color('blue'), 1: pygame.Color('red')}

    def render(self, screen):
        # color = 0 if self.width % 2 else 1
        color = 1
        for row, row_v in enumerate(self.board):
            col = 0
            for col, col_v in enumerate(row_v):
                clr = 'white'
                rect_width = 1
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size,
                                  self.top + row * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 rect_width)
                clr = self.colors[col_v]
                rect_width = 0
                pygame.draw.ellipse(screen, pygame.Color(clr),
                                    (self.left + col * self.cell_size + 2,
                                     self.top + row * self.cell_size + 2,
                                     self.cell_size - 4,
                                     self.cell_size - 4),
                                    rect_width)
                # color = not color
                color = color
            if col % 2 != 0:
                # color = not color
                color = color

    def set_view(self, left, top, cell_size):
        self.left, self.top, self.cell_size = left, top, cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.left < x < self.left + (self.width * self.cell_size):
            cell_x = (x - self.left) // self.cell_size
        else:
            return
        if self.top < y < self.top + (self.height * self.cell_size):
            cell_y = (y - self.top) // self.cell_size
        else:
            return
        return cell_x, cell_y

    def on_click(self, cell_pos):
        if cell_pos is None:
            return
        row, col = cell_pos[::-1]
        self.color_row_col(row, col)

    def color_row_col(self, row, col):
        color = self.board[row][col]
        for i in range(self.width):
            if i == col:
                continue
            self.board[row][i] = color
        for i in range(self.height):
            self.board[i][col] = color

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def main():
    pygame.init()
    standard_err = 'Неправильный формат ввода'
    try:
        board_size = int(input('Размер поля: '))
    except ValueError:
        print(standard_err)
        return
    if board_size < 3:
        print(standard_err)
        return
    board = Board(board_size, board_size)
    board.set_view(20, 20, 50)
    size = width, height = (board.left * 2 + board.width * board.cell_size,
                            board.top * 2 + board.height * board.cell_size)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Недореверси')
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        # отрисовка и изменения св-в объекта
        board.render(screen)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
