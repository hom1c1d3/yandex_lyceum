import pygame


def draw(screen, cell_num):
    size, size = screen.get_size()
    cell_w = cell_h = size // cell_num
    color = 1 if cell_num % 2 else 0
    for row in range(cell_num):
        for col in range(cell_num):
            clr = 'black' if color else 'white'
            pygame.draw.rect(screen, pygame.Color(clr), (col * cell_w, row * cell_h, cell_w, cell_h), 0)
            color = not color
        if col % 2 != 0:
            color = not color


def main():
    standard_err = 'Неправильный формат ввода'
    try:
        size, cell_num = map(int, input('Размер и количество клеток: ').split())
    except ValueError:
        print(standard_err)
        return
    if size % cell_num != 0:
        print(standard_err)
        return
    pygame.init()
    screen = pygame.display.set_mode((size, size))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Шахматная клетка')
    draw(screen, cell_num)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
