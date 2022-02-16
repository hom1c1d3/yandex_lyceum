def print_upper(printer):
    copy_printer = printer

    def wrapper(*args, **kwargs):
        return copy_printer(*(i.upper() for i in args), **kwargs)

    return wrapper


print = print_upper(print)
