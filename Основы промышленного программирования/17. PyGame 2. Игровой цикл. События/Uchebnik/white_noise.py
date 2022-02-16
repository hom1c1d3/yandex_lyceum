import random
import pygame


def draw(screen):
    width, height = screen.get_size()
    for i in range(100000):
        screen.fill(pygame.Color((255, 255, 255)), (random.random() * width, random.random() * height, 2, 2))


def main():
    pygame.init()
    size = 800, 600
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        # отрисовка и изменения св-в объекта
        draw(screen)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()