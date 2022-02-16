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
    if len(passwd) < 9:
        raise LengthError

    if passwd.isnumeric():
        raise LetterError  # если все знаки цифры - то ошибка отсутствия букв

    if passwd.islower() or passwd.isupper():
        raise LetterError

    if not any(i.isnumeric() for i in passwd):
        raise DigitError

    lower_passwd = passwd.lower()
    for lang_layout in keyboard_rows:
        for row in lang_layout:
            for ind in range(len(row) - 2):  # группируем по три поэтому последние два
                # не нужны
                bad_sequence = row[ind:ind + 3]
                if bad_sequence in lower_passwd:
                    raise SequenceError

    return 'ok'
