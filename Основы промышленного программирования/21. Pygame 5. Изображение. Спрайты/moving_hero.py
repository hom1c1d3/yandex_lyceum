import os
import sys
import pygame


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
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Свой курсор мыши")
    hero_im = load_image('creature.png')
    hero = pygame.sprite.Sprite()
    hero.image = hero_im
    hero.rect = hero.image.get_rect()
    hero_group = pygame.sprite.GroupSingle(hero)
    step = 10
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            key_states = pygame.key.get_pressed()
            dx, dy = 0, 0
            if key_states[pygame.K_DOWN]:
                dy += step
            if key_states[pygame.K_LEFT]:
                dx -= step
            if key_states[pygame.K_UP]:
                dy -= step
            if key_states[pygame.K_RIGHT]:
                dx += step
            hero.rect.move_ip(dx, dy)
        # отрисовка и изменение св-в объектов
        screen.fill('white')
        hero_group.draw(screen)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
