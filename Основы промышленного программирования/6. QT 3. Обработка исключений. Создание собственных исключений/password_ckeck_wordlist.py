import zipfile
from collections import defaultdict
from io import BytesIO
from urllib.request import urlopen


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


class WordError(PasswordError):
    ...


resp = urlopen('http://lyceum.s3.yandex.net/content/resources/5.3/data.zip')
file = BytesIO(resp.read())
data = zipfile.ZipFile(file)
for i in data.filelist:
    if '/' not in i.filename and not i.is_dir():
        with data.open(i.filename, 'r') as f:
            if 'words' in i.filename:
                words = [j.decode() for j in f.read().split(b'\n')]
            else:
                passwords = [j.decode() for j in f.read().split(b'\n')]

data.close()


def check_password(passwd: str):
    keyboard_rows = [['qwertyuiop', 'asdfghjkl', 'zxcvbnm'],
                     ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']]
    errors = []
    if len(passwd) < 9:
        errors.append(LengthError)

    if passwd.isnumeric():
        errors.append(LetterError)  # если все знаки цифры - то ошибка отсутствия букв

    if passwd.islower() or passwd.isupper():
        errors.append(LetterError)

    if not any(i.isnumeric() for i in passwd):
        errors.append(DigitError)

    lower_passwd = passwd.lower()
    for lang_layout in keyboard_rows:
        for row in lang_layout:
            for ind in range(len(row) - 2):  # группируем по три поэтому последние два
                # не нужны
                bad_sequence = row[ind:ind + 3]
                if bad_sequence in lower_passwd:
                    errors.append(SequenceError)

    if any(i in lower_passwd for i in words):
        errors.append(WordError)
    if errors:
        raise PasswordError(errors)
    return 'ok'


res = defaultdict(lambda: 0)
for i in passwords:
    try:
        chk = check_password(i)
    except PasswordError as e:
        for j in e.args[0]:
            res[j.__name__] += 1

for i, j in sorted(res.items()):
    print(i, '-', j)