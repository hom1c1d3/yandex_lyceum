import pygame


def draw(screen):
    size = width, height = screen.get_size()
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (100, 0, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (100, 0, 255), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    draw(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
