import pygame


TITLE = 'TEMPLATE'


def draw(screen):
    pass


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    # Создаем новый холст
    canvas = pygame.Surface(screen.get_size())
    x1, y1 = 0, 0
    w, h = 0, 0
    drawing = False
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                canvas.blit(screen, (0, 0))
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
                else:
                    w, h = 0, 0
        screen.fill(pygame.Color('black'))
        screen.blit(canvas, (0, 0))
        if drawing and (w, h) != (0, 0):
            pygame.draw.rect(screen, (0, 0, 255), (x1, y1, w, h), 5)
        # отрисовка и изменения св-в объекта
        draw(screen)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()