import random

import pygame


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    for i in range(10000):
            screen.fill(pygame.Color(tuple(random.randint(0, 255) for _ in range(3))), (random.random() * width, random.random() * height, 2, 2))

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
