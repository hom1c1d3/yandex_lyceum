# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError('Expected str, got {}'.format(type(s)))

    return s[::-1]

# # Тестируемая функция
# def reverse(s):
#     return 1/0


if __name__ == '__main__':
    print(reverse("5"))
    print(reverse(5))