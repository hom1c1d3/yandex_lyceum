import pygame


def draw(screen, brick_size):
    width, height = screen.get_size()
    color = pygame.Color('red')
    canvas = pygame.Surface((width, brick_size.height))
    canvas.fill(screen.get_at((0, 0)))
    delta = 2  # это прослойка
    brick_y = 0
    for brick_x in range(0, canvas.get_width(), brick_size.width + delta):
        rect = pygame.draw.rect(canvas, color, (brick_x, brick_y,
                                                brick_size.width, brick_size.height))
    canvas = pygame.transform.flip(canvas, True, False)
    for brick_y in range(0, height, brick_size.height + delta):
        canvas = pygame.transform.flip(canvas, True, False)
        screen.blit(canvas, (0, brick_y))


def main():
    brick = pygame.Rect(0, 0, 30, 15)
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    screen.fill('white')
    pygame.display.set_caption('Кирпичи')
    draw(screen, brick)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


if __name__ == '__main__':
    main()
