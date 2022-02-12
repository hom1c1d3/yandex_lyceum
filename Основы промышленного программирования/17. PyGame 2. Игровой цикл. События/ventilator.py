import math
import pygame

TITLE = 'Вентилятор'


def draw(screen, start_angle):
    width, height = screen.get_size()
    center = width // 2, height // 2
    cx, cy = center
    blade_len = 70
    radius = 10
    color = pygame.Color('white')
    pygame.draw.circle(screen, color, center, radius)
    blade_angle = 30
    blade_between_angle = 120
    blade_between_angle = blade_between_angle - 2 * (blade_angle / 2)
    angle = start_angle
    pygame_angle = angle - 90
    for _ in range(3):
        pygame.draw.polygon(screen, color,
                            (center,
                             (math.cos(math.radians(pygame_angle)) * blade_len + cx,
                              math.sin(math.radians(pygame_angle)) * blade_len + cy),
                             (math.cos(math.radians(pygame_angle + blade_angle)) * blade_len + cx,
                              math.sin(math.radians(pygame_angle + blade_angle)) * blade_len + cy)))
        angle = angle + blade_angle + blade_between_angle
        pygame_angle = angle - 90


def main():
    pygame.init()
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    speed = 1
    fps = 50
    speed = speed / fps
    angle = 345
    reset_color = pygame.Color('black')
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка мыши
                    speed -= 1  # крутит в левую сторону
                else:
                    speed += 1
        screen.fill(reset_color)
        # отрисовка и изменения св-в объекта
        draw(screen, angle)
        angle += speed
        clock.tick(fps)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
