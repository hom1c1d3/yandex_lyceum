import os
import random
import sys

import pygame

pygame.init()
WIDTH, HEIGHT = 500, 500
size = width, height = WIDTH, WIDTH
screen = pygame.display.set_mode(size)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


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


class Ball(pygame.sprite.Sprite):

    def __init__(self, radius, x, y, *group):
        super(Ball, self).__init__(*group)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, 'red', (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx, self.vy = random.randint(-5, 5), random.randint(-5, 5)

    def update(self, sprites_group=None, *args, **kwargs) -> None:
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        crashed = pygame.sprite.spritecollide(self, sprites_group, False, self.is_touches)
        crashed_speed = None
        for i in crashed:
            if not isinstance(i, Ball):
                continue
            crashed_speed = True
            i.vx, i.vy = -i.vx, -i.vy
        if crashed_speed is not None:
            self.vx, self.vy = -self.vx, -self.vy

    @staticmethod
    def is_touches(first_sprite, second_sprite):
        if not (isinstance(first_sprite, Ball) and isinstance(second_sprite, Ball)):
            return pygame.sprite.collide_rect(first_sprite, second_sprite)
        (x1, y1), r1 = first_sprite.rect.center, first_sprite.radius
        (x2, y2), r2 = second_sprite.rect.center, second_sprite.radius
        is_touches = (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 + r2) ** 2
        return is_touches


class Border(pygame.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2, *groups):
        super(Border, self).__init__(*groups)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - 1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def main():
    pygame.display.set_caption("Шарики")
    all_sprites = pygame.sprite.Group()

    Border(5, 5, width - 5, 5, all_sprites)
    Border(5, height - 5, width - 5, height - 5, all_sprites)
    Border(5, 5, 5, height - 5, all_sprites)
    Border(width - 5, 5, width - 5, height - 5, all_sprites)

    for i in range(10):
        all_sprites.add(Ball(20, 200, 200))

    clock = pygame.time.Clock()
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        # отрисовка и изменение св-в объектов
        screen.fill('white')
        all_sprites.draw(screen)
        all_sprites.update(all_sprites)
        clock.tick(60)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
