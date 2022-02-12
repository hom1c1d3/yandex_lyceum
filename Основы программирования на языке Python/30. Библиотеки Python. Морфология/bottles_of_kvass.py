import pymorphy2


morph = pymorphy2.MorphAnalyzer()
bottle = morph.parse('бутылка')[0]

for i in range(99, 0, -1):
    print(f'В холодильнике {i} {bottle.make_agree_with_number(i).word} кваса.')
    i -= 1
    if i < 0:
        break
    print('Возьмём одну и выпьем.')
    if i % 10 == 1 and i != 11:
        verb = 'Осталась'
    else:
        verb = 'Осталось'
    print(f'{verb} {i} {bottle.make_agree_with_number(i).word} кваса.')