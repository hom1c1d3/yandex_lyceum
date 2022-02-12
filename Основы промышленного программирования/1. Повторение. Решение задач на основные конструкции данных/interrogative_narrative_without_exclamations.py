import re
import sys
from collections import defaultdict

text = sys.stdin.read().replace('\n', ' ')
sentences = re.split(r'([.!?])', text)
sentences = [(a + b).strip() for a, b in zip(sentences[::2], sentences[1::2])]
group_words = defaultdict(list)

for i in sentences:
    punct_chr = i[-1]
    words = re.sub(r'[^\w\s]', '', i.lower()).split()
    group_words[punct_chr] += words

res = []
for i in group_words['.']:
    if i in group_words['?'] and i not in group_words['!']:
        res.append(i)

res = sorted(set(res))
print(*res)