from swift import words
import string
import random


def get_after_word(word):
    for ind, i in enumerate(words):
        if i == word:
            yield ' '.join(words[ind + 1:ind + 2])


a = random.choice(words)
res = ''
while a[0] != '.':
    res += ' ' + a
    a = random.choice(list(get_after_word(a.split()[-1])))
res = res.strip(' ' + string.punctuation)
res += '.'
res = res.capitalize()
print(res)