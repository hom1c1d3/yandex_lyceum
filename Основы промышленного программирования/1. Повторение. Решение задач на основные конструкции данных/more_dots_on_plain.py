dots = []
for i in range(int(input())):
    x, y = map(int, input().split())
    dots.append((x, y))

# точки которые лежат между графиками
for x, y in dots:
    if abs(x) > abs(y):
        print((x, y))

most_left = min(dots, key=lambda a: a[0])
print('left:', most_left)
most_right = max(dots, key=lambda a: a[0])
print('right:', most_right)
top = max(dots, key=lambda a: a[1])
print('top:', top)
bottom = min(dots, key=lambda a: a[1])
print('bottom:', bottom)