import pygame

TITLE = 'Белый кролик'


def draw(screen):
    pass


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    MY_EVENT_TYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MY_EVENT_TYPE, 100)
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, 'white', event.pos, 20)
                pygame.draw.ellipse(screen, 'white', (event.pos[0] - 15, event.pos[1] - 40, 10, 40))
                pygame.draw.ellipse(screen, 'white', (event.pos[0] + 5, event.pos[1] - 40, 10, 40))
            if event.type == MY_EVENT_TYPE:
                print("Moe sobytie srabotalo")
        # отрисовка и изменения св-в объекта
        pygame.display.flip()  # обновление экрана
        clock.tick(27)
    pygame.quit()


if __name__ == '__main__':
    main()
