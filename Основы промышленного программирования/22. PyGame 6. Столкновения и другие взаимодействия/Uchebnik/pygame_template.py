import os
import random
import sys

import pygame

pygame.init()
WIDTH, HEIGHT = 500, 500
size = width, height = WIDTH, WIDTH
screen = pygame.display.set_mode(size)


def load_image(path, colorkey=None):
    full_path = os.path.join('data', path)
    # ксли файл не существует, то выходим
    if not os.path.exists(full_path):
        print(f"Файл с изображением '{full_path}' не найден")
        sys.exit()
    im = pygame.image.load(full_path)

    if colorkey is not None:
        im = im.convert()
        if colorkey == -1:
            colorkey = im.get_at((0, 0))
        im.set_colorkey(colorkey)
    else:
        im = im.convert_alpha()
    return im


def main():
    pygame.display.set_caption("Бомбы")
    all_sprites = pygame.sprite.Group()

    clock = pygame.time.Clock()
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        # отрисовка и изменение св-в объектов
        screen.fill('white')
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(30)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
