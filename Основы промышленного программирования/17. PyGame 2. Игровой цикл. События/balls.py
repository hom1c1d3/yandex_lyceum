import math
import pygame

TITLE = 'Шарики'


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    running = True
    clock = pygame.time.Clock()
    radius = 10
    degree = 45
    speed = 100
    fps = 100
    speed = speed / fps
    balls = []
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball = [event.pos, 180 + degree]
                balls.append(ball)
        screen.fill(pygame.Color('black'))
        # отрисовка и изменения св-в объекта
        for b in balls:
            center, deg = b
            x, y = center
            x += speed * math.cos(math.radians(deg))
            y += speed * math.sin(math.radians(deg))
            if not (0 + radius < y < height - radius):
                deg = -deg % 360
                y = radius if y - radius < 0 else y
                y = height - radius if y + radius > height else y
            elif not (0 + radius < x < width - radius):
                deg = 180 - deg
                x = radius + 1 if x - radius < 0 else x
                x = width - (radius + 1) if x + radius > width else x
            center = x, y
            b[0] = center
            b[1] = deg
            pygame.draw.circle(screen, 'white', center, radius)
        clock.tick(fps)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
