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


class Car(pygame.sprite.Sprite):
    image = 'car2.png'

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image: pygame.Surface = load_image(self.image)
        self.rect = self.image.get_rect()
        self.delta_move = 3

    def update(self, screen=None, *args, **kwargs) -> None:
        if self.rect.right > screen.get_width() or self.rect.left < 0:
            self.delta_move = -self.delta_move
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.move_ip(self.delta_move, 0)


def main():
    pygame.init()
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Машинка")
    running = True
    group = pygame.sprite.GroupSingle()
    car = Car(group)
    clock = pygame.time.Clock()
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
        # отрисовка и изменение св-в объектов
        car.update(screen)
        screen.fill('white')
        group.draw(screen)
        pygame.display.flip()  # обновление экрана
        clock.tick(30)
    pygame.quit()


if __name__ == '__main__':
    main()
