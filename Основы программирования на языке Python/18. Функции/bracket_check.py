def bracket_check(test_string: str):
    while test_string:
        if test_string.startswith(')') or test_string.endswith('('):
            return print('NO')
        close = test_string.find(')')
        if close == -1:
            return print('NO')
        test_string = test_string.replace('(', '', 1).replace(')', '', 1)
    print('YES')
