def people_again(*args, **kwargs):
    res = []
    for word in args:
        new_word = list(word)
        remove = kwargs.get('remove', tuple())
        new_word = filter(lambda x: x[0] not in remove, enumerate(new_word))
        _, new_word = zip(*new_word)
        new_word = list(new_word)
        letter = kwargs.get('letter', '')
        new_word.insert(0, letter if new_word[0] != letter else '')
        new_word = ''.join(new_word)
        to_upper = kwargs.get('to_upper', 1)
        new_word = new_word.lower() if to_upper else new_word.upper()
        new_word = new_word.strip()
        res.append(new_word)
    return res
