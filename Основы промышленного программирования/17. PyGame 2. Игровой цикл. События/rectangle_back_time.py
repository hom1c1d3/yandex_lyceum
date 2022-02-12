import pygame


def draw(screen, rhombus_diagonal):
    width, height = screen.get_size()
    color = pygame.Color('orange')
    for i in range(0, width - rhombus_diagonal, rhombus_diagonal):
        for j in range(0, height - rhombus_diagonal, rhombus_diagonal):
            center = i + rhombus_diagonal / 2, j + rhombus_diagonal / 2
            coords = ((center[0], j),
                      (i + rhombus_diagonal, center[1]),
                      (center[0], j + rhombus_diagonal),
                      (i, center[1]))
            pygame.draw.polygon(screen, color, coords)


def main():
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    canvas = pygame.Surface(screen.get_size())
    x1, y1, w, h = 0, 0, 0, 0
    drawing = False  # режим рисования выключен
    running = True
    figures = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True  # включаем режим рисования
                figures.append(None)
                # запоминаем координаты одного угла
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                # сохраняем нарисованное (на втором холсте)
                canvas.blit(screen, (0, 0))
                drawing = False
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                # запоминаем текущие размеры
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
                    figures.pop()
                    figures.append(pygame.Rect(x1, y1, w, h))
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_z
                    and event.mod & pygame.KMOD_CTRL):
                try:
                    figures.pop()
                except IndexError:
                    pass
        canvas.fill(pygame.Color('black'))
        for rect in list(filter(lambda x: x is not None, figures)):
            pygame.draw.rect(canvas, (0, 0, 255), rect, 5)
        # рисуем на экране сохранённое на втором холсте
        screen.fill(pygame.Color('black'))
        screen.blit(canvas, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
