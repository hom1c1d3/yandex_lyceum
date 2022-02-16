import pygame


def draw(screen, circle_num):
    size, size = screen.get_size()
    centre = size // 2
    circle_w = size // circle_num // 2
    colors = [pygame.Color(clr) for clr in ('red', 'green', 'blue')]
    color_num = 0
    for i in range(circle_num):
        pygame.draw.circle(screen, colors[color_num], (centre, centre), circle_w * i + circle_w, circle_w)
        color_num += 1
        color_num %= len(colors)


def main():
    standard_err = 'Неправильный формат ввода'
    try:
        circle_w, circle_num = map(int, input('Размер и количество колец: ').split())
    except ValueError:
        print(standard_err)
        return
    size = circle_w * circle_num * 2
    pygame.init()
    screen = pygame.display.set_mode((size, size))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Мишень')
    draw(screen, circle_num)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
