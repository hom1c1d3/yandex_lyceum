hours, minutes = ([i.zfill(2) for i in sorted(input().split(), key=int)] for _ in range(2))
for h in hours:
    for m in minutes:
        if sum(map(int, h)) != sum(map(int, m)):
            print(f'{h}:{m}')
