import zipfile
from collections import defaultdict
from io import BytesIO
from urllib.request import urlopen
from string import punctuation


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


words = []
passwords = []


def download_passwd_data():
    global words, passwords
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


def open_current_files():
    global words, passwords
    with open('top-9999-words.txt') as f:
        words = [j for j in f.read().split('\n')]
    with open('top 10000 passwd.txt') as f:
        passwords = [j for j in f.read().split('\n')]


def check_password(passwd: str):
    keyboard_rows = [['qwertyuiop', 'asdfghjkl', 'zxcvbnm'],
                     ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']]
    errors = []
    if len(passwd) < 9:
        errors.append(LengthError)

    passwd_letters = ''.join(i for i in passwd if i not in punctuation)
    if not passwd_letters:
        errors.append(LetterError)

    if passwd_letters.isnumeric():
        errors.append(LetterError)  # если все знаки цифры - то ошибка отсутствия букв

    if passwd_letters.islower() or passwd_letters.isupper():
        errors.append(LetterError)
    if not any(i.isnumeric() for i in passwd):
        errors.append(DigitError)

    lower_passwd = passwd.lower()

    def find_seq():
        for lang_layout in keyboard_rows:
            for row in lang_layout:
                for ind in range(len(row) - 2):  # группируем по три поэтому последние два
                    # не нужны
                    bad_sequence = row[ind:ind + 3]
                    if bad_sequence in lower_passwd or bad_sequence[::-1] in lower_passwd:
                        errors.append(SequenceError)
                        return True

    find_seq()

    if any(i in lower_passwd for i in words):
        errors.append(WordError)
    if errors:
        raise PasswordError(errors)
    return 'ok'


download_passwd_data()
res = defaultdict(lambda: 0)
for i in passwords:
    try:
        chk = check_password(i)
    except PasswordError as e:
        for j in e.args[0]:
            res[j.__name__] += 1

for i, j in sorted(res.items()):
    print(i, '-', j)
