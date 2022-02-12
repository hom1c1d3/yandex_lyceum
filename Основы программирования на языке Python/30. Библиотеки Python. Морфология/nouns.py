import pymorphy2
import sys
from collections import Counter

morph = pymorphy2.MorphAnalyzer()
text = map(lambda x: x if x.isalpha() or x.isspace() else ' ', sys.stdin.read())
words = ''.join(text).split()
nouns = Counter()

for i in words:
    word_morph = morph.parse(i)[0]
    if 'NOUN' in word_morph.tag and word_morph.score > 0.5:
        nouns[word_morph.normal_form] += 1

res, _ = zip(*sorted(nouns.most_common(), key=lambda x: (x[1], x[0]), reverse=True)[:10])
print(*res)