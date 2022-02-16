import pygame


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Движущийся шар")
    running = True
    x_pos = 0
    delta_x = 1
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        # отрисовка и изменения св-в объекта
        pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
        x_pos += delta_x
        if x_pos >= width:
            x_pos = delta_x
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()