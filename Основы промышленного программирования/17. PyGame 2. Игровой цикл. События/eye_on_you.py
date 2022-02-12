import pygame

TITLE = 'Слежка'


def main():
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    fps = 60
    reset_color = pygame.Color('black')
    count = 0
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWMINIMIZED:
                count += 1
        screen.fill(reset_color)
        # отрисовка и изменения св-в объекта
        font = pygame.font.Font(None, 100)
        text = font.render(str(count), True, 'red')
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        clock.tick(fps)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
