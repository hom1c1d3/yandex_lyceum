kit = [list(map(int, input().split())) for _ in range(int(input()) * 2)]
first = eval(' + '.join(str(i) for i in kit[::2]))
second = eval(' + '.join(str(i) for i in kit[1::2]))
nums = []
for ind, i in enumerate(kit):
    if not ind % 2:
        continue
    for n in i:
        if n not in first:
            nums.append(n)


print(*nums)