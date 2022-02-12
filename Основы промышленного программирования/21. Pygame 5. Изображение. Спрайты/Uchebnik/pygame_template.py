import pygame


def main():
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шаблон")
    screen.fill('white')
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        # отрисовка и изменение св-в объектов
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
