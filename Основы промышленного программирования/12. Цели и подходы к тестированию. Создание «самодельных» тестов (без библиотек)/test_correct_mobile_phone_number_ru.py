from yandex_testing_lesson import is_correct_mobile_phone_number_ru


def test_correct_mobile_phone_number_ru():
    test_data = [
        ('+7 999 123-45-67', True),
        ('+7,999*123-45-67', False),
        ('79991234567', False),
        ('+8 999 123-45-67', False),
        ('8 999 123-45-67', True),
        ('+7(999)1234567', True),
        ('+7(99)1234567', False),
        ('+7(999)12(34)567', False),
        ('+7991234(567)', False)
    ]
    for inp, correct in test_data:
        try:
            test_res = is_correct_mobile_phone_number_ru(inp)
        except (TypeError, ValueError):
            test_res = None
        if test_res != correct:
            return False
    return True


if __name__ == '__main__':
    if test_correct_mobile_phone_number_ru():
        print('YES')
    else:
        print('NO')