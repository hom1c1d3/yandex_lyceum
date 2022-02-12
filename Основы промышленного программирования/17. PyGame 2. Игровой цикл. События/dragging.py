import pygame

TITLE = 'Перетаскивание'


def main():
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    fps = 120
    reset_color = pygame.Color('black')
    is_dragging = False
    rect = pygame.Rect(0, 0, 100, 100)
    drag_offset = 0, 0
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # не левая
                    if rect.collidepoint(*event.pos):
                        is_dragging = True
                        drag_offset = rect.x - event.pos[0], rect.y - event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    is_dragging = False
            if event.type == pygame.MOUSEMOTION:
                if not is_dragging:
                    continue
                rect.x, rect.y = event.pos[0] + drag_offset[0], event.pos[1] + drag_offset[1]
        screen.fill(reset_color)
        # отрисовка и изменения св-в объекта
        pygame.draw.rect(screen, 'green', rect)
        clock.tick(fps)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
