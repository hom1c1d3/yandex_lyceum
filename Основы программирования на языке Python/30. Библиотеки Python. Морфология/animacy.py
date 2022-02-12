import pymorphy2
import sys


morph = pymorphy2.MorphAnalyzer()
words = list(sys.stdin)
animacy = {'anim': ('живая',), 'inan': ('не', 'живая')}

for word in words:
    word_parsed = morph.parse(word.strip())[0]
    if 'NOUN' not in word_parsed.tag:
        print('Не существительное')
        continue
    anim = list(animacy[word_parsed.tag.animacy])
    anim[-1] = morph.parse(anim[-1])[0]
    if word_parsed.tag.number == 'plur':
        anim[-1] = anim[-1].inflect({word_parsed.tag.number}).word
    else:
        anim[-1] = anim[-1].inflect({word_parsed.tag.gender}).word
    anim = ' '.join(anim)
    print(anim.capitalize())