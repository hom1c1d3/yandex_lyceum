class Functions:

    def __init__(self):
        self._functions = {'x': lambda x: x, 'sqrt_fun': lambda x: x ** 0.5}

    def define(self, name, func_name1, operation, func_name2):
        func1, func2 = getattr(self, func_name1), getattr(self, func_name2)
        if '+' in operation:
            func = (lambda x: func1(x) + func2(x))
        elif '-' in operation:
            func = (lambda x: func1(x) - func2(x))
        elif '*' in operation:
            func = (lambda x: func1(x) * func2(x))
        elif '/' in operation:
            func = (lambda x: func1(x) / func2(x))
        else:
            raise NotImplemented
        self._functions[name] = func

    def calculate(self, func_name, *args):
        func = getattr(self, func_name)
        return [func(i) for i in args]

    @staticmethod
    def get_digit(string):
        try:
            return int(string)
        except ValueError:
            try:
                return float(string)
            except ValueError:
                raise ValueError

    def __getattr__(self, item):
        try:
            return self._functions[item]
        except KeyError:
            try:
                return lambda x: self.get_digit(item)
            except ValueError:
                raise AttributeError

    def __repr__(self):
        return repr(self._functions)


def main():
    functions = Functions()
    for _ in range(int(input())):
        command = input().split()

        if 'define' in command[0]:
            functions.define(*command[1:])
        elif 'calculate' in command[0]:
            print(*functions.calculate(command[1], *map(Functions.get_digit, command[2:])))


main()