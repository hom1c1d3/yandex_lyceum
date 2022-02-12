def password_check(passwd: str):
    keyboard_rows = [['qwertyuiop', 'asdfghjkl', 'zxcvbnm'],
                     ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']]
    if len(passwd) < 9:
        return 'error'

    if passwd.isnumeric():
        return 'error'

    if passwd.islower() or passwd.isupper():
        return 'error'

    if not any(i.isnumeric() for i in passwd):
        return 'error'

    lower_passwd = passwd.lower()
    for lang_layout in keyboard_rows:
        for row in lang_layout:
            for ind in range(len(row) - 2):  # группируем по три поэтому последние два
                # не нужны
                bad_sequence = row[ind:ind + 3]
                if bad_sequence in lower_passwd:
                    return 'error'

    return 'ok'


res = password_check(input())
print(res)