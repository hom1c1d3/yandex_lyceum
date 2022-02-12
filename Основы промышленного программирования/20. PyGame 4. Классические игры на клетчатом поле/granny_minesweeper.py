import random

import pygame


class Board:

    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # дефолтные значения
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for row, row_v in enumerate(self.board):
            for col, col_v in enumerate(row_v):
                clr = 'white'
                rect_width = 1
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size,
                                  self.top + row * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 rect_width)
                clr = 'black'
                rect_width = 0
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size + 1,
                                  self.top + row * self.cell_size + 1,
                                  self.cell_size - 2,
                                  self.cell_size - 2),
                                 rect_width)

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
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):

    def __init__(self, width, height, bombs_count):
        super().__init__(width, height)
        self.place_bombs(bombs_count)

    def place_bombs(self, bombs_count):
        count = 0
        while count < bombs_count:
            row, col = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.board[row][col] == -1:
                count += 1
                self.board[row][col] = 10

    def render(self, screen):
        for row, row_v in enumerate(self.board):
            for col, col_v in enumerate(row_v):
                clr = 'white'
                rect_width = 1
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size,
                                  self.top + row * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 rect_width)
                clr = 'black'
                if col_v == 10:
                    clr = 'red'
                elif -1 < col_v < 10:
                    self.draw_number(screen, col_v, (row, col))
                    continue
                rect_width = 0
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size + 1,
                                  self.top + row * self.cell_size + 1,
                                  self.cell_size - 2,
                                  self.cell_size - 2),
                                 rect_width)

    def on_click(self, cell_pos):
        if cell_pos is None:
            return
        row, col = cell_pos[::-1]
        self.open_cell(row, col)

    def open_cell(self, row, col):
        if self.board[row][col] == 10:
            return
        self.board[row][col] = self.get_mines_count_around(row, col)

    def get_neighbour_cells(self, row, col):
        neighbour_cells = []
        for row_ind in range(row - 1, row + 2):
            for col_ind in range(col - 1, col + 2):
                if not row_ind - row and not col_ind - col:  # сама клетка
                    continue
                cell = self.get_cell_by_coord(row_ind, col_ind)
                neighbour_cells.append(cell)
        return neighbour_cells

    def get_cell_by_coord(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.board[row][col]
        else:
            return 0

    def get_mines_count_around(self, row, col):
        neighbour_cells = self.get_neighbour_cells(row, col)
        return sum(1 for i in neighbour_cells if i == 10)

    def draw_number(self, screen, number, cell_pos):
        row, col = cell_pos
        x, y = self.left + col * self.cell_size + 1, self.top + row * self.cell_size + 1
        font_size = self.cell_size
        font = pygame.font.Font(None, font_size)
        text = font.render(str(number), True, 'green')
        width, height = text.get_size()
        x += (self.cell_size - width) / 2
        y += (self.cell_size - height) / 2
        screen.blit(text, (x, y))


def main():
    pygame.init()
    size = width, height = 430, 630
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Дедушка сапёра')
    left, top, cell_size = 15, 15, 40
    board = Minesweeper((width - left * 2) // cell_size, (height - top * 2) // cell_size, 10)
    board.set_view(left, top, cell_size)
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