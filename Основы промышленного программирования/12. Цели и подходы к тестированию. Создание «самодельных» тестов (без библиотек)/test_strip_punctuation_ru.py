from yandex_testing_lesson import strip_punctuation_ru


def test_strip_punctuation_ru():
    test_data = [('Привет, друг. Как дела?', 'Привет друг Как дела'),
                 ('Что                 . Привет', 'Что Привет'),
                 ('Вутин - пор', 'Вутин пор'),
                 ('Кто-то', 'Кто-то')]
    for inp, correct in test_data:
        try:
            test_res = strip_punctuation_ru(inp)
        except (TypeError, ValueError):
            test_res = None
        if test_res != correct:
            return False
    return True


if __name__ == '__main__':
    if test_strip_punctuation_ru():
        print('YES')
    else:
        print('NO')
