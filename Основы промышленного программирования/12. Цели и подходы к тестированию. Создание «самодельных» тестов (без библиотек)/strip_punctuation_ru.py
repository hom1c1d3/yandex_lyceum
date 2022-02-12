from string import punctuation


def strip_punctuation_ru(data):
    new_punctuation = punctuation.replace('-', '')
    res = ' '.join(''.join(' ' if i in new_punctuation else i for i in data).split())
    res = res.replace(' - ', ' ')
    res = ' '.join(res.split())
    return res
