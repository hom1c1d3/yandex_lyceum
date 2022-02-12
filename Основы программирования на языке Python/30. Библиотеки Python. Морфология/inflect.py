import pymorphy2


morph = pymorphy2.MorphAnalyzer()
word = input()
word = morph.parse(word)[0]
cases = (('nomn', 'именительный'),
         ('gent', 'родительный'),
         ('datv', 'дательный'),
         ('accs', 'винительный'),
         ('ablt', 'творительный'),
         ('loct', 'предложный'))
numbers = (('sing', 'единственное'), ('plur', 'множественное'))

if 'NOUN' in word.tag:
    for lat_num, ru_num in numbers:
        print(f"{ru_num.capitalize()} число:")
        for lat_case, ru_case in cases:
            print(f"{ru_case.capitalize()} падеж: {word.inflect({lat_num, lat_case}).word}")
else:
    print("Не существительное")