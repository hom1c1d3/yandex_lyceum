square_size = float(input())
speed = float(input())

moves = 0
while square_size - speed >= 0.01:
    moves += 1
    square_size = ((square_size - speed)**2 + speed**2)**.5

print(moves)
