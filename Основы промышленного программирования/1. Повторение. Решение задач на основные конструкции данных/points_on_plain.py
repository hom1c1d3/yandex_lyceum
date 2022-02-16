quarters = [0, 0, 0, 0]  # первое значение -- первая четверть
for i in range(int(input())):
    x, y = map(int, input().split())
    if 0 in (x, y):
        print(f'({x}, {y})')
    elif x > 0 and y > 0:
        quarters[0] += 1
    elif x < 0 and y > 0:
        quarters[1] += 1
    elif x < 0 and y < 0:
        quarters[2] += 1
    else:
        quarters[3] += 1

print(f'I: {quarters[0]}, II: {quarters[1]}, III: {quarters[2]}, IV: {quarters[3]}.')
