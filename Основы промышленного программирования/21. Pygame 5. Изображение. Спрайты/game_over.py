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
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Машинка")
    running = True
    game_over = load_image('game_over.jpeg')
    game_over = pygame.transform.scale(game_over, (600, 300))
    x_pos = -game_over.get_width()
    fps = 30
    speed = 200
    speed = speed / fps
    clock = pygame.time.Clock()
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        # отрисовка и изменение св-в объектов
        if x_pos < 0:
            x_pos += speed
        screen.fill('blue')
        screen.blit(game_over, (x_pos, 0))
        pygame.display.flip()  # обновление экрана
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
