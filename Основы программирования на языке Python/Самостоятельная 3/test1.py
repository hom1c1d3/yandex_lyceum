import random


def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


fuels = input().split()
power_from, power_to = map(int, input().split())
fill_from, fill_to = map(float, input().split())
lamp_num = int(input())

fuels = random.sample(fuels, lamp_num)
powers = random.choices(range(power_from, power_to + 1), k=lamp_num)
fills = list(map(lambda x: round(x, 1), random.sample(list(frange(fill_from, fill_to, 0.1)), lamp_num)))

for number, fuel, power, fill in zip(range(1, lamp_num + 1), fuels, powers, fills):
    print(f'Lamp {number}: works on {fuel}, light intensity {power} cd, volume {fill} l, cost {round(fill * power, 1)}'
          f' coins')
