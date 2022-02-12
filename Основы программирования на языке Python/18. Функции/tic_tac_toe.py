def tic_tac_toe(field):
    for i in field:
        if len(set(i)) == 1:
            return print(*set(i), 'win')
    field_r = [[field[j][i] for j in range(len(field))] for i in range(len(field))]
    for i in field_r:
        if len(set(i)) == 1:
            return print(*set(i), 'win')
    # диагонали
    a = {field[i][i] for i in range(len(field))}
    b = {field[i][-(i + 1)] for i in range(len(field))}
    if len(a) == 1:
        return print(*a, 'win')
    if len(b) == 1:
        return print(*b, 'win')
    return print('draw')


data = '''x 0 x
0 x 0
x 0 0'''

tic_tac_toe([i.split() for i in data.splitlines()])

ones = {0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}

tens = {10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'}

months = [('January', 'Январь'), ('February', 'Февраль'), ('March', 'Март'), ('April', 'Апрель'),
          ('May', 'Май'), ('June', 'Июнь'), ('July', 'Июль'), ('August', 'Август'),
          ('September', 'Сентябрь'), ('October', 'Октябрь'), ('November', 'Ноябрь'),
          ('December', 'Декабрь')]
