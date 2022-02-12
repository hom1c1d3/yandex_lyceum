class PasswordError(Exception):
    ...


class LengthError(PasswordError):
    ...


class LetterError(PasswordError):
    ...


class DigitError(PasswordError):
    ...


class SequenceError(PasswordError):
    ...


def check_password(passwd: str):
    keyboard_rows = [['qwertyuiop', 'asdfghjkl', 'zxcvbnm'],
                     ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']]
    assert not len(passwd) < 9, 'длина должна быть больше 8'

    assert not passwd.isnumeric(), 'пароль должен содержать буквы'

    assert not (passwd.islower() or passwd.isupper()), 'пароль в одном регистре'

    assert any(i.isnumeric() for i in passwd), 'нет цифр в пароле'

    lower_passwd = passwd.lower()
    for lang_layout in keyboard_rows:
        for row in lang_layout:
            for ind in range(len(row) - 2):  # группируем по три поэтому последние два
                # не нужны
                bad_sequence = row[ind:ind + 3]
                assert bad_sequence not in lower_passwd, 'последовательность неверна'

    return 'ok'


passwd = input()

try:
    print(check_password(passwd))
except AssertionError:
    print('error')