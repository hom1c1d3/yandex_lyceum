print('\n'.join(
    eval(
        ' & '.join([{input() for i in range(int(input()))}.__repr__() for _ in range(int(input()))]))
))
