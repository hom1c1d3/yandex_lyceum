def palindrome():
    with open('input.dat', 'rb') as f:
        data = f.read()
        f.seek(0)
        return data == f.read()[::-1]
