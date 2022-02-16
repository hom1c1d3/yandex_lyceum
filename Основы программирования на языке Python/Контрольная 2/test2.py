def morning(*args):
    vowels = 'aeuio'
    data = ''.join(''.join(set(i)) for i in args).lower()
    res = {i: data.count(i) for i in vowels}
    return res
