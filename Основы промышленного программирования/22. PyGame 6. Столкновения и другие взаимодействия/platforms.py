import os
import sys

import pygame

pygame.init()
WIDTH, HEIGHT = 500, 500
size = width, height = WIDTH, WIDTH
screen = pygame.display.set_mode(size)
FPS = 60


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


class Player(pygame.sprite.Sprite):
    size = 20, 20
    color = pygame.Color('blue')
    delta_speed = pygame.Vector2(FPS / 10, FPS / 50)

    def __init__(self, x, y, *groups):
        super(Player, self).__init__(*groups)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.pos = pygame.Vector2((x, y))
        self.rect.topleft = self.pos.xy
        self.speed = pygame.Vector2(0, 0)

        self.key_pressed = {}

    def update_pos(self, x, y, center=False):
        if center:
            self.rect.center = x, y
        else:
            self.rect.topleft = x, y
        self.pos.xy = x, y

    def move(self, event=None):
        if getattr(event, 'type', None) is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.key_pressed[pygame.K_RIGHT] = True
                if event.key == pygame.K_LEFT:
                    self.key_pressed[pygame.K_LEFT] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.key_pressed[pygame.K_RIGHT] = False
                if event.key == pygame.K_LEFT:
                    self.key_pressed[pygame.K_LEFT] = False
            return
        if self.key_pressed.get(pygame.K_RIGHT, False):
            self.pos.x += self.delta_speed.x
        if self.key_pressed.get(pygame.K_LEFT, False):
            self.pos.x -= self.delta_speed.x
        self.rect.move_ip(self.pos.x - self.rect.centerx, self.delta_speed.y)

    def solve_collision(self, platforms):
        if platforms is None:
            return
        hits = pygame.sprite.spritecollide(self, platforms, False)
        new_pos = pygame.Vector2(self.pos.x, -float('inf'))
        if not hits:
            return
        for hit in hits:
            new_pos.y = max(new_pos.y, hit.rect.top - self.rect.height // 2)
        self.update_pos(*new_pos.xy, center=True)

    def update(self, event=None, platforms=None, *args, **kwargs) -> None:
        self.move(event)
        self.solve_collision(platforms)


class Platform(pygame.sprite.Sprite):
    size = 50, 10
    color = pygame.Color('grey')

    def __init__(self, x, y, *groups):
        super(Platform, self).__init__(*groups)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2((x, y))
        self.rect.topleft = self.pos.xy

    def update_pos(self, x, y, center=False):
        if center:
            self.rect.center = x, y
        else:
            self.rect.topleft = x, y
        self.pos.xy = x, y


def main():
    pygame.display.set_caption("Платформы")
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    player = None

    clock = pygame.time.Clock()
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if player is not None:
                        player.update_pos(*event.pos, True)
                    else:
                        player = Player(*event.pos, all_sprites)
                if event.button == 1:
                    platform = Platform(*event.pos, all_sprites)
                    platforms.add(platform)
                    platform.update_pos(*event.pos, True)
            all_sprites.update(event)
        # отрисовка и изменение св-в объектов
        screen.fill('black')
        all_sprites.update(platforms=platforms)
        all_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
