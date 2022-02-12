n = int(input())
bumps = list(zip([int(input()) for _ in range(n)], [input() for _ in range(n)]))

res = ''
for times, word in bumps:
    letters_in_word = [word.count(i) for i in word]
    if times in letters_in_word:
        if letters_in_word.count(times) == times:
            res += word[letters_in_word.index(times)]
        else:
            res = 'нечленораздельно'
            break
    else:
        res = 'нечленораздельно'
        break

print(res)