import re
import pygame

TITLE = 'Zoom'


def get_points(file_path):
    with open(file_path, encoding='utf8') as fd:
        points_str = fd.read()
    if not points_str:
        return
    res = []
    points = re.split(r'\), \(', points_str[1:-1])
    for point in points:
        x, y = map(float, point.replace(',', '.').split(';'))
        res.append((x, y))
    return res


def pygamify_points(screen_size, points):
    width, height = screen_size
    cx, cy = width / 2, height / 2
    res = [(cx + x, cy - y) for x, y in points]
    return res


def get_scaled_points(scale, points):
    return [(x * scale, y * scale) for x, y in points]


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    fps = 60
    reset_color = pygame.Color('black')
    color = pygame.Color('white')
    points = get_points('points.txt')
    if points is None:
        print('неверный формат точек')
        return
    scale = 10
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # колесико вверх
                    scale += 1
                elif event.button == 5:
                    scale -= 1
                scale = max(2, scale)
        screen.fill(reset_color)
        # отрисовка и изменения св-в объекта
        draw_points = pygamify_points(size, get_scaled_points(scale, points))
        pygame.draw.polygon(screen, color, draw_points, 1)
        clock.tick(fps)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()