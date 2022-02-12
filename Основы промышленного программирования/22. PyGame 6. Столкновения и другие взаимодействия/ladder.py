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


class GameModel(pygame.sprite.Sprite):
    size = None
    color = None

    def __init__(self, x, y, *groups):
        super().__init__(*groups)
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


class Player(GameModel):
    size = 20, 20
    color = pygame.Color('blue')
    delta_speed = pygame.Vector2(10, 10)
    fall_speed = pygame.Vector2(0, 50 / FPS)

    def __init__(self, x, y, *groups):
        super(Player, self).__init__(x, y, *groups)
        self.speed = pygame.Vector2(0, 0)
        self.key_pressed = {pygame.K_RIGHT: False, pygame.K_LEFT: False,
                            pygame.K_UP: False, pygame.K_DOWN: False}
        self.is_ladder_moving = False

    def move(self, event=None, ladders=None):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_pressed.keys():
                    self.key_pressed[event.key] = True
            if event.type == pygame.KEYUP:
                if event.key in self.key_pressed.keys():
                    self.key_pressed[event.key] = False
            return
        if self.key_pressed[pygame.K_RIGHT]:
            self.pos.x += self.delta_speed.x
        if self.key_pressed[pygame.K_LEFT]:
            self.pos.x -= self.delta_speed.x

        delta_speed_y = self.fall_speed.y
        self.is_ladder_moving = False
        if ladders is not None:
            if pygame.sprite.spritecollideany(self, ladders):
                if self.key_pressed[pygame.K_UP]:
                    self.pos.y -= self.delta_speed.y
                if self.key_pressed[pygame.K_DOWN]:
                    self.pos.y += self.delta_speed.y
                self.is_ladder_moving = True
                delta_speed_y = 0
        self.update_pos(self.pos.x, self.pos.y + delta_speed_y, center=True)

    def solve_collision(self, platforms):
        if platforms is None or self.is_ladder_moving:
            return
        hits = pygame.sprite.spritecollide(self, platforms, False)
        new_pos = pygame.Vector2(self.pos.x, -float('inf'))
        if not hits:
            return
        for hit in hits:
            new_pos.y = max(new_pos.y, hit.rect.top - self.rect.height // 2)
        self.update_pos(*new_pos.xy, center=True)

    def update(self, event=None, platforms=None, ladders=None, *args, **kwargs) -> None:
        self.move(event, ladders)
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


class Ladder(GameModel):
    size = 10, 50
    color = pygame.Color('red')

    def __init__(self, x, y, *groups):
        super(Ladder, self).__init__(x, y, *groups)
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
    pygame.display.set_caption("Лесенки")
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    ladders = pygame.sprite.Group()

    player = None

    clock = pygame.time.Clock()
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN
                    and event.button == 1
                    and pygame.key.get_mods() & pygame.KMOD_CTRL):
                ladder = Ladder(*event.pos, all_sprites)
                ladders.add(ladder)
                ladder.update_pos(*event.pos, True)
            elif event.type == pygame.MOUSEBUTTONDOWN:
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
        all_sprites.update(platforms=platforms, ladders=ladders)
        all_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
