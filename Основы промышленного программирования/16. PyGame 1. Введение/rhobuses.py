import pygame


def draw(screen, rhombus_diagonal):
    width, height = screen.get_size()
    color = pygame.Color('orange')
    for i in range(0, width - rhombus_diagonal, rhombus_diagonal):
        for j in range(0, height - rhombus_diagonal, rhombus_diagonal):
            center = i + rhombus_diagonal / 2, j + rhombus_diagonal / 2
            coords = ((center[0], j),
                      (i + rhombus_diagonal, center[1]),
                      (center[0], j + rhombus_diagonal),
                      (i, center[1]))
            pygame.draw.polygon(screen, color, coords)


def main():
    standard_err = 'Неправильный формат ввода'
    try:
        rhombus_diagonal = int(input('Размер ромбиков: '))
    except ValueError:
        print(standard_err)
        return
    if rhombus_diagonal < 1:
        print(standard_err)
        return
    pygame.init()
    screen = pygame.display.set_mode((400, 500))
    screen.fill('yellow')
    pygame.display.set_caption('Ромбики')
    draw(screen, rhombus_diagonal)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


if __name__ == '__main__':
    main()
