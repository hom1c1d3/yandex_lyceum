import pymorphy2
import sys

verbs = {'увидеть', 'примечать', 'видеть', 'узреть', 'глядеть'}
morph = pymorphy2.MorphAnalyzer()
text = filter(lambda x: x.isalpha() or x.isspace(), sys.stdin.read())
words = ''.join(text).split()

count = 0
for i in words:
    norm = morph.parse(i)[0].normal_form
    if norm in verbs:
        count += 1

print(count)