def check_password(password):
    def get_func(func):
        def wrapper(*args, **kwargs):
            user_passw = input()
            if user_passw == password:
                return func(*args, **kwargs)
            else:
                return print('В доступе отказано')
        return wrapper
    return get_func
