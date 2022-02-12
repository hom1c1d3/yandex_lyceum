from yandex_testing_lesson import is_prime


def test_prime():
    test_data = [
        (2, True),
        (3, True),
        (-1, None),
        (0, None),
        (1, None),
        (7919, True),
        (961, False)
    ]
    for inp, correct in test_data:
        try:
            test_res = is_prime(inp)
        except (TypeError, ValueError):
            test_res = None
        if test_res != correct:
            return False
    return True


if __name__ == '__main__':
    if test_prime():
        print('YES')
    else:
        print('NO')