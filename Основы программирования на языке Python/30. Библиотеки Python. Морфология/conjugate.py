import pymorphy2


morph = pymorphy2.MorphAnalyzer()
word = input()
word = morph.parse(word)[0]
tenses = (('past', 'прошедшее'),
          ('pres', 'настоящее'))
genders = ('masc', 'femn', 'neut')
persons = tuple(sorted(word.tag.PERSONS))
numbers = ('sing', 'plur')

if {'VERB', 'INFN'} & {word.tag.POS}:
    for lat_ten, ru_ten in tenses:
        print(f'{ru_ten.capitalize()} время:')
        if lat_ten == 'past':
            for gender in genders:
                print(f'{word.inflect({lat_ten, gender}).word}')
            print(f'{word.inflect({lat_ten, numbers[-1]}).word}')
        else:
            for person in persons:
                for number in numbers:
                    print(f'{word.inflect({lat_ten, person, number}).word}')
else:
    print('Не глагол')