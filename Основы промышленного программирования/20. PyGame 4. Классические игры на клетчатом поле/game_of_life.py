import pygame


class Board:

    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
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
        if cell_pos is None:
            return
        row, col = cell_pos[::-1]
        # print(f'({row}, {col})')
        self.board[row][col] = int(not self.board[row][col])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Life(Board):

    def render(self, screen):
        # color = 0 if self.width % 2 else 1
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
                if col_v == 1:
                    clr = 'green'
                elif col_v == 0:
                    continue  # leave cell black
                rect_width = 0
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size + 1,
                                  self.top + row * self.cell_size + 1,
                                  self.cell_size - 2,
                                  self.cell_size - 2),
                                 rect_width)

    def get_cell_by_coord(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            return self.board[row][col]
        else:
            return 0

    def get_neighbour_cells(self, row, col):
        neighbour_cells = []
        for row_ind in range(row - 1, row + 2):
            for col_ind in range(col - 1, col + 2):
                if not row_ind - row and not col_ind - col:  # сама клетка
                    continue
                cell = self.get_cell_by_coord(row_ind, col_ind)
                neighbour_cells.append(cell)
        return neighbour_cells

    def solve_cell(self, row, col):
        cell = self.board[row][col]
        neighbour_cells = self.get_neighbour_cells(row, col)
        living_cells = [i for i in neighbour_cells if i]
        living_cells_count = len(living_cells)
        if not cell:
            if living_cells_count == 3:  # если рядом с мертвой три живых
                cell_state = 1
            else:
                cell_state = 0
        else:
            if not (living_cells_count == 2 or living_cells_count == 3):
                # рядом с живой слишком мало или слишком много клеток то умирает
                cell_state = 0
            else:
                cell_state = 1

        return cell_state

    def next_move(self):
        next_cells = []
        for row_ind, row in enumerate(self.board):
            for col_ind, col in enumerate(row):
                cell_state = self.solve_cell(row_ind, col_ind)
                next_cells.append(((row_ind, col_ind), cell_state))
        for (row, col), cell_state in next_cells:
            self.board[row][col] = cell_state


def main():
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Игра «Жизнь»')
    left, top, cell_size = 0, 0, 15
    board = Life((width - left * 2) // cell_size, (height - top * 2) // cell_size)
    board.set_view(left, top, cell_size)
    running = True
    clock = pygame.time.Clock()
    game_state = False
    timer = 0
    fps = 60
    update_time = 20
    update_delta = 100
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    game_state = not game_state
                elif event.button == 1:
                    board.get_click(event.pos)
                elif event.button == 4:
                    update_time -= update_delta
                elif event.button == 5:
                    update_time += update_delta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = not game_state
        screen.fill((0, 0, 0))
        # отрисовка и изменения св-в объекта
        if game_state and pygame.time.get_ticks() - timer > update_time:
            timer = pygame.time.get_ticks()
            board.next_move()
        board.render(screen)
        clock.tick(fps)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()