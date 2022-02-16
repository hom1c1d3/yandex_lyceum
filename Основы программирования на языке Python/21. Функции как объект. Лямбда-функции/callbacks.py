def ask_password(login, password, success, failure):
    login, password = login.lower(), password.lower()
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    isthreevowels = len(list(filter(lambda a: a in vowels, password))) == 3
    issetequals = list(filter(lambda a: a not in vowels,
                              password)) == list(filter(lambda a: a not in vowels,
                                                        login))
    if not (issetequals or isthreevowels):
        return failure(login, 'Everything is wrong')
    if not isthreevowels:
        return failure(login, 'Wrong number of vowels')
    if not issetequals:
        return failure(login, 'Wrong consonants')
    return success(login)


def main(login, password):
    success = (lambda a: f'Привет, {a}!')
    failure = (lambda a, b: f'Кто-то пытался притвориться пользователем {a}, но в пароле допустил ошибку: {b.upper()}.')
    print(ask_password(login, password, success, failure))
