import math
import colorsys
import pygame
from pygame import Vector2, Vector3


def vector_3d_to_2d(v3):
    angle = 45
    k = math.sin(math.radians(angle))
    return pygame.Vector2(v3.x + k * v3.z * math.cos(-math.radians(angle)),
                          v3.y + k * v3.z * math.sin(-math.radians(angle)))


def vectors2d_to_coordinates(vectors):
    coordinates = [i.xy for i in vectors]
    return coordinates


def vector3d_to_2d_coordinates(vectors):
    return vectors2d_to_coordinates(vector_3d_to_2d(v3) for v3 in vectors)


def hsv2rgb(h, s, v):
    rgb = colorsys.hsv_to_rgb(h, s, v)
    return round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255)


def draw(screen, cube_size, hue_value):
    width, height = screen.get_size()
    # это середина верхней стороны передней грани
    draw_center = Vector2(width // 2 - cube_size // 4, height // 2 - cube_size // 4)
    front_color = pygame.Color(hsv2rgb(hue_value, 1, .75))
    frontal = [Vector3(draw_center.x - cube_size // 2, draw_center.y, 0),
               Vector3(draw_center.x + cube_size // 2, draw_center.y, 0),
               Vector3(draw_center.x + cube_size // 2, draw_center.y + cube_size, 0),
               Vector3(draw_center.x - cube_size // 2, draw_center.y + cube_size, 0)]
    frontal_2d = vector3d_to_2d_coordinates(frontal)
    bound_rect = pygame.draw.polygon(screen, front_color, frontal_2d)
    top_color = pygame.Color(hsv2rgb(hue_value, 1, 1))
    top = [Vector3(draw_center.x - cube_size // 2, draw_center.y, 0),
           Vector3(draw_center.x - cube_size // 2, draw_center.y, cube_size),
           Vector3(draw_center.x + cube_size // 2, draw_center.y, cube_size),
           Vector3(draw_center.x + cube_size // 2, draw_center.y, 0)]
    top_2d = vector3d_to_2d_coordinates(top)
    bound_rect = bound_rect.union(pygame.draw.polygon(screen, top_color, top_2d))
    side_color = pygame.Color(hsv2rgb(hue_value, 1, .5))
    top = [Vector3(draw_center.x + cube_size // 2, draw_center.y, 0),
           Vector3(draw_center.x + cube_size // 2, draw_center.y, cube_size),
           Vector3(draw_center.x + cube_size // 2, draw_center.y + cube_size, cube_size),
           Vector3(draw_center.x + cube_size // 2, draw_center.y + cube_size, 0)]
    side_2d = vector3d_to_2d_coordinates(top)
    bound_rect.union(pygame.draw.polygon(screen, side_color, side_2d))


def main():
    standard_err = 'Неправильный формат ввода'
    try:
        cube_side, hue_value = map(int,
                                   input('Размер стороны куба (кратен 4 и не болше 100)'
                                         ' и оттенок (от 0 до 360): ').split())
    except ValueError:
        print(standard_err)
        return
    if hue_value not in range(0, 361) or cube_side % 4 or cube_side > 100:
        print(standard_err)
        return
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    screen.fill('black')
    pygame.display.set_caption('Куб')
    draw(screen, cube_side, hue_value)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


if __name__ == '__main__':
    main()
