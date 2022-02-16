import pygame


TITLE = 'Жёлтый круг'


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    center = None
    start_radius = 10
    radius = 1
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                center = event.pos
                radius = 10
                screen.fill(pygame.Color('blue'))
        screen.fill(pygame.Color('blue'))
        # отрисовка и изменения св-в объекта
        if center is not None:
            radius += start_radius * clock.tick() / 1000
            pygame.draw.circle(screen, pygame.Color('yellow'), center, radius)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()