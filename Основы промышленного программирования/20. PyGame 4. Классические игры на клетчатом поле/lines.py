import heapq

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

    @staticmethod
    def on_click(cell_pos):
        if cell_pos is None:
            return

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Lines(Board):

    def __init__(self, width, height):
        super(Lines, self).__init__(width, height)
        self.red_coord = None
        self.path = None

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
                if col_v == 1:
                    clr = 'blue'
                elif col_v == 2:
                    clr = 'red'
                else:
                    clr = 'black'
                rect_width = 0
                pygame.draw.ellipse(screen, pygame.Color(clr),
                                    (self.left + col * self.cell_size + 2,
                                     self.top + row * self.cell_size + 2,
                                     self.cell_size - 4,
                                     self.cell_size - 4),
                                    rect_width)

    def on_click(self, cell_pos):
        if cell_pos is None:
            return
        cell_pos = cell_pos[::-1]
        row, col = cell_pos
        # print(f'({row}, {col})')
        old_value = self.board[row][col]
        if old_value == 0:
            new_value = 1
            if self.red_coord is not None:
                if self.has_path(*self.red_coord, *cell_pos):
                    self.board[self.red_coord[0]][self.red_coord[1]] = 0
                    self.red_coord = None
                else:
                    new_value = 0
        elif old_value == 1:
            if self.red_coord is not None:
                self.board[self.red_coord[0]][self.red_coord[1]] = 1
            self.red_coord = row, col
            new_value = 2
        else:
            new_value = 1
        self.board[row][col] = new_value

    def next_animation(self):
        path = self.path
        if self.path is None:
            return
        if len(path) == 1:
            prev_row, prev_col = path[0]
            self.board[prev_row][prev_col] = 1
            self.path = None
            self.red_coord = None
            return
        prev_row, prev_col = path[0]
        nxt_row, nxt_col = path[1]
        self.board[prev_row][prev_col] = 0
        self.board[nxt_row][nxt_col] = 2
        self.red_coord = path[1]
        self.path = self.path[1:]

    def search_path(self, start, destination):
        frontier = PriorityQueue()
        frontier.put(start, False)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == destination:
                break

            for neighbour_edge in self.get_neighbours(current):
                nxt = neighbour_edge
                cost = self.get_cost(current, nxt)
                if cost is None:
                    continue
                new_cost = cost_so_far[current] + cost
                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                    cost_so_far[nxt] = new_cost
                    heuristic = self.heuristic(destination, nxt)
                    priority = new_cost + heuristic
                    frontier.put(nxt, priority)
                    came_from[nxt] = current

        return came_from, cost_so_far

    @staticmethod
    def heuristic(p1, p2):
        (x1, y1) = p1
        (x2, y2) = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def get_cost(self, frm, to):
        if self.board[to[0]][to[1]] == 1:
            return None
        return 1

    def get_path(self, start, destination):
        came_from, cost_so_far = self.search_path(start, destination)

        path = []
        current = destination
        if destination not in came_from:
            return None
        while came_from[current] is not None:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path = path[::-1]
        return path

    def has_path(self, x1, y1, x2, y2):
        path = self.get_path((x1, y1), (x2, y2))
        return path is not None

    def get_neighbours(self, cell):
        row, col = cell
        neighbour_cells_raw = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
        neighbour_cells = []
        for row_ind, col_ind in neighbour_cells_raw:
            if 0 <= row_ind < self.height and 0 <= col_ind < self.width:
                neighbour_cells.append((row_ind, col_ind))
        return neighbour_cells


def main():
    pygame.init()
    size = width, height = 430, 430
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Линеечки')
    left, top, cell_size = 15, 15, 40
    board = Lines((width - left * 2) // cell_size, (height - top * 2) // cell_size)
    board.set_view(left, top, cell_size)
    running = True
    clock = pygame.time.Clock()
    timer = 0
    update_time = 100
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
        clock.tick(60)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
