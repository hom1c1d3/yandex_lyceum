from yandex_testing_lesson import is_palindrome


def test_palindrome():
    test_data = [
        (42, None),
        (['a', 'b', 'c'], False),
        ('', True),
        ('aba', True),
        ('a', True),
        ('abc', False)
    ]
    for inp, correct in test_data:
        try:
            test_res = is_palindrome(inp)
        except TypeError:
            test_res = None
        if test_res != correct:
            return False
    return True


if __name__ == '__main__':
    if test_palindrome():
        print('YES')
    else:
        print('NO')