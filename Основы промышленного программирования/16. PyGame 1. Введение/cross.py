import pygame


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
    pygame.display.set_caption('Крест')
    white = pygame.Color((255, 255, 255))
    pygame.draw.line(screen, white, (0, 0), (width, height), 5)
    pygame.draw.line(screen, white, (0, height), (width, 0), 5)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
