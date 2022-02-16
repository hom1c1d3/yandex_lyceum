def check_password(func):
    def wrapper(*args, **kwargs):
        password = input()
        if password == 'ультрамегасложныйпароль':
            return func(*args, **kwargs)
        else:
            return print('В доступе отказано')
    return wrapper


@check_password
def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
