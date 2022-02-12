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
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Свой курсор мыши")
    arrow_im = load_image('arrow.png')
    arrow = pygame.sprite.Sprite()
    arrow.image = arrow_im
    arrow.rect = arrow.image.get_rect()
    arrow_group = pygame.sprite.GroupSingle(arrow)
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                arrow.rect.x = event.pos[0]
                arrow.rect.y = event.pos[1]
        # отрисовка и изменение св-в объектов
        screen.fill('black')
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            arrow_group.draw(screen)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()
