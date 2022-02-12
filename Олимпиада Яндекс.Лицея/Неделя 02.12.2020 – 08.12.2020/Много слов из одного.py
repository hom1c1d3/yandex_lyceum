origin = list(input())
points = 0
for i in range(int(input())):
    word = input()
    org = origin[:]
    p = 0
    for j in word:
        if j in org:
            org.remove(j)
            p += 1
        else:
            p = 0
            break
    points += p

print(points)
