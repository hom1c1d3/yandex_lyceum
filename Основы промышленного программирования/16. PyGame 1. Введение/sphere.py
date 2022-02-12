import pygame


def draw(screen, ellipse_num):
    width, height = screen.get_size()
    step_x = width / ellipse_num
    step_y = height / ellipse_num
    el_x, el_y, el_width, el_height = 0, 0, width, height
    draw_ellipse = (lambda x, y, w, h: pygame.draw.ellipse(screen, 'white', (x, y, w, h), 1))
    draw_ellipse(el_x, el_y, el_width, el_height)
    for i in range(ellipse_num - 1):
        el_y += step_y / 2
        el_height -= step_y
        draw_ellipse(el_x, el_y, el_width, el_height)
    el_x, el_y, el_width, el_height = 0, 0, width, height
    for i in range(ellipse_num - 1):
        el_x += step_x / 2
        el_width -= step_x
        draw_ellipse(el_x, el_y, el_width, el_height)


def main():
    standard_err = 'Неправильный формат ввода'
    try:
        ellipse_num = int(input('Количество эллипсов: '))
    except ValueError:
        print(standard_err)
        return
    if ellipse_num < 1:
        print(standard_err)
        return
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Сфера')
    draw(screen, ellipse_num)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


if __name__ == '__main__':
    main()
