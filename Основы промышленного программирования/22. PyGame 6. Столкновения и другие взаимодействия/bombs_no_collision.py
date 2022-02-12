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


class Bomb(pygame.sprite.Sprite):
    image = load_image('bomb.png')
    image_boom = load_image('boom.png')
    # image_boom = pygame.transform.scale(image_boom, image.get_size())

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Bomb.image
        self.mask = self.image.get_masks()
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(random.randrange(WIDTH - self.rect.width),
                                   random.randrange(HEIGHT - self.rect.height))

    def update(self, event=None, *args, **kwargs) -> None:
        if (event is not None and event.type == pygame.MOUSEBUTTONDOWN
                and self.rect.collidepoint(*event.pos)):
            self.image = self.image_boom


def main():
    pygame.display.set_caption("Boom them all — 2")
    all_sprites = pygame.sprite.Group()
    for i in range(20):
        b = Bomb()
        while pygame.sprite.spritecollideany(b, all_sprites):
            b = Bomb()
        all_sprites.add(b)

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
        screen.fill('black')
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(30)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
