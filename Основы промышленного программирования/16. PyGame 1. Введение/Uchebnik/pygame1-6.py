import pygame


def draw_square(screen):
    color = pygame.Color(50, 100, 150)
    pygame.draw.rect(screen, color, (20, 20, 100, 100), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] +30, hsv[3])
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    draw_square(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
