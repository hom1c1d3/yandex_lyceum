import re


def get_re_pattern(string):
    glas = '[аяоёуюиыэе]'
    non_glas = '[бмкхлфзпгвцжчйнсштщърдь]'
    RE_PATTERN = ''
    for i in string:
        if i == '1':
            RE_PATTERN += non_glas
        elif i == '0':
            RE_PATTERN += glas
        elif i == '?':
            RE_PATTERN += r'\w{1}'
        elif i == '*':
            RE_PATTERN += r'\w*'
        else:
            raise Exception('pattern error')
    return re.compile(RE_PATTERN)


pattern = input()
dish = input()
food = []
while dish:
    food.append(dish)
    dish = input()
re_pattern = get_re_pattern(pattern)
food = list(filter(lambda a: len(a) >= len(pattern.replace('*', '')), food))
results = '\n'.join(filter(re_pattern.fullmatch, food))
if results:
    print(results)
else:
    print('Есть нечего, значить!')
