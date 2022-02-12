n = int(input())
all_iq = 0

for i in range(n):
    iq = int(input())
    all_iq += iq
    if i == 0 or iq == all_iq / (i + 1):
        print(0)
    elif iq > all_iq / (i + 1):
        print('>')
    else:
        print('<')
