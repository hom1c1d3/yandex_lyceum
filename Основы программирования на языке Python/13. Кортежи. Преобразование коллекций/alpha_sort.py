words = [input() for _ in range(int(input()))]

for i in range(len(words) - 1):
    for j in range(len(words) - 1 - i):
        if words[j] > words[j + 1]:
            words[j], words[j + 1] = words[j + 1], words[j],
print(*words, sep='\n')
