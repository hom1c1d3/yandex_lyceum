num = sum((int(input()) for _ in range(3)))
s1 = set()
s2 = set()

for i in range(num):
    name = input()
    if name in s1:
        if name in s2:
            s1.remove(name)
            s2.remove(name)
        else:
            s2.add(name)
    else:
        s1.add(name)

print(len(s1 & s2) if s1 & s2 else 'NO')
