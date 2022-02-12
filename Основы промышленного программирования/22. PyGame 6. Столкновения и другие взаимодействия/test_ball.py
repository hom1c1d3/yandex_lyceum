from random import randint, uniform
from math import hypot
import pygame
import sys

SCREEN_SIZE = WIDTH, HEIGHT = (1000, 1000)

# Готовим 200 кругов в случайных местах случайного радиуса и цвета
N = 200
CIRCLES = [
    {
        'xy': [uniform(0 + 30, WIDTH - 30), uniform(30, HEIGHT - 30)],
        'r': (r := randint(5, 30)),
        'm': r * r * r,
        'color': [randint(0, 255), randint(0, 255), randint(0, 255)],
        'v': [uniform(-40, 40) / r, uniform(-40, 40) / r]
    }
    for __ in range(N)
]
MAX_R = max(circ['r'] for circ in CIRCLES)


def move_circles(circs):
    for circ in circs:
        xy = circ['xy']
        v = circ['v']
        r = circ['r']
        xy[0] += v[0]
        xy[1] += v[1]
        if xy[0] < r:
            xy[0] = r
            v[0] *= -1
        elif xy[0] > WIDTH - r:
            xy[0] = WIDTH - r
            v[0] *= -1
        if xy[1] < r:
            xy[1] = r
            v[1] *= -1
        elif xy[1] > HEIGHT - r:
            xy[1] = HEIGHT - r
            v[1] *= -1


def collide(x1, y1, x2, y2, m1, m2, r1, r2, vx1, vy1, vx2, vy2):
    dx = x1 - x2
    dy = y1 - y2
    sum_r = r1 + r2
    if dx * dx + dy * dy > sum_r * sum_r:
        return False, 0, 0, 0, 0, 0, 0, 0, 0
    dist = hypot(dx, dy)
    ndx = dx / dist
    ndy = dy / dist
    proj = (ndx * (vx2 - vx1) + ndy * (vy2 - vy1))
    dvx = ndx * proj
    dvy = ndy * proj
    coef1 = 2 * m2 / (m1 + m2)
    coef2 = 2 * m1 / (m1 + m2)
    dvx1 = + dvx * coef1
    dvy1 = + dvy * coef1
    dvx2 = - dvx * coef2
    dvy2 = - dvy * coef2
    # Раздвигаем шары так, чтобы они касались
    fix = (sum_r - dist) * 1.01 / (r1 ** 2 + r2 ** 2)
    fix1 = fix * r2 ** 2  # Чем больше второй шар, тем сильнее мы смещаем первый
    fix2 = fix * r1 ** 2
    dx1 = + ndx * fix1
    dy1 = + ndy * fix1
    dx2 = - ndx * fix2
    dy2 = - ndy * fix2
    return True, dvx1, dvy1, dvx2, dvy2, dx1, dy1, dx2, dy2


def collide_circles(circs):
    # Сортируем по х-координате. Проверяем коллизии только с теми, у кого х-координата на расстоянии не больше max_r
    circs.sort(key=lambda circ: circ['xy'][0])
    for left in range(len(circs) - 1):
        right = left
        # сдвигаем левый край до первого теоретически возможного столкновения
        while right < len(circs) - 1 and circs[right]['xy'][0] < circs[left]['xy'][0] + 2 * MAX_R:
            right += 1
            circ1 = circs[left]
            circ2 = circs[right]
            m1 = circ1['m']
            r1 = circ1['r']
            x1, y1 = circ1['xy']
            vx1, vy1 = circ1['v']
            m2 = circ2['m']
            r2 = circ2['r']
            x2, y2 = circ2['xy']
            vx2, vy2 = circ2['v']
            collision, dvx1, dvy1, dvx2, dvy2, dx1, dy1, dx2, dy2 = collide(x1, y1, x2, y2, m1, m2, r1, r2, vx1, vy1,
                                                                            vx2, vy2)
            if collision:
                circ1['v'][0] += dvx1
                circ1['v'][1] += dvy1
                circ2['v'][0] += dvx2
                circ2['v'][1] += dvy2
                # Раздвигаем шары так, чтобы они касались
                circ1['xy'][0] += dx1
                circ1['xy'][1] += dy1
                circ2['xy'][0] += dx2
                circ2['xy'][1] += dy2


def update():
    # Обновляем координаты и скорости всех кругов
    move_circles(CIRCLES)
    collide_circles(CIRCLES)


def render():
    # Чистим экран и отрисовываем каждый круг
    screen.fill((0, 0, 0))  # Заливаем всё чёрным
    for circ in CIRCLES:
        pygame.draw.circle(screen, circ['color'], circ['xy'], circ['r'], 0)
    pygame.display.update()
    fps.tick(27)  # Не обновляем экран чаще, чем 60 раз в секунду


# Главный цикл: пока на нажали крестик обновляем и отрисовываем
# Немного pygame-магии
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update()
    render()