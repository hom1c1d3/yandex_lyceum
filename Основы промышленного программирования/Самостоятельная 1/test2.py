with open('boat_suits.txt') as f:
    data = f.read()

color = input()

data = [i.split() for i in data.splitlines()]
data = [(a, b, int(c)) for a, b, c in data]

choosed_color = [(a, b, c) for a, b, c in data if b == color]
name = sorted((a for a, _, _ in choosed_color), key=lambda x: (len(x), x), reverse=True)[0]
count_items = sum(c for _, _, c in choosed_color)
count = len(choosed_color)

with open('colored_dress.txt', 'w') as f:
    print(count, name, count_items, sep='\n', file=f)