import pygame


def draw(screen):
    width, height = screen.get_size()
    pygame.draw.rect(screen, pygame.Color('red'), (1, 1, width - 1, height - 1), 0)


def main():
    try:
        width, height = map(int, input('Размеры: ').split())
        size = width, height
    except ValueError:
        print('Неправильный формат ввода')
        return
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Прямоугольник')
    draw(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
