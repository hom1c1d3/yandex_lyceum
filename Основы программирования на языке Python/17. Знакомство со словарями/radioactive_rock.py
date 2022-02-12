decay = input().split()
decay = dict(zip(decay[::2], map(int, decay[1::2])))
elements, radiacy = [input().split() for _ in range(2)]
activity = list(zip(elements, map(float, radiacy)))
radiation = float(input())

day = 0
while sum([i[1] for i in activity]) > radiation:
    day += 1
    for ind, elem in enumerate(elements):
        if day % decay[activity[ind][0]] == 0:
            activity[ind] = activity[ind][0], activity[ind][1] / 2


print(day)
print(*[i[1] for i in activity])