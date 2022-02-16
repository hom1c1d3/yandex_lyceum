import pygame


TITLE = 'К щелчку'


def main():
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    speed = 1
    pos = width // 2, height // 2
    prev_pos = pos
    radius = 20
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                prev_pos = pos
                pos = event.pos
        screen.fill((0, 0, 0))
        # отрисовка и изменения св-в объекта
        if prev_pos[0] < pos[0]:
            dx = speed
        elif prev_pos[0] > pos[0]:
            dx = -speed
        else:
            dx = 0
        if prev_pos[1] < pos[1]:
            dy = speed
        elif prev_pos[1] > pos[1]:
            dy = -speed
        else:
            dy = 0
        prev_pos = prev_pos[0] + dx, prev_pos[1] + dy
        pygame.draw.circle(screen, 'red', prev_pos, radius)
        pygame.display.flip()  # обновление экрана
        clock.tick(100)
    pygame.quit()


if __name__ == '__main__':
    main()