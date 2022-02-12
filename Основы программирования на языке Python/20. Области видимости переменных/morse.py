# Только буквы, поэтому сокращения теряют смысл

EN = {('m', '−−'), ('p', '.−−.'), ('g', '−−.'), ('i', '..'), ('l', '.−..'), ('x', '−..−'),
      ('w', '.−−'), ('q', '−−.−'), ('r', '.−.'), ('u', '..−'), ('a', '.−'), ('y', '−.−−'),
      ('n', '−.'), ('v', '...−'), ('z', '−−..'), ('j', '.−−−'), ('o', '−−−'), ('k', '−.−'),
      ('h', '....'), ('e', '.'), ('b', '−...'), ('c', '−.−.'), ('d', '−..'), ('f', '..−.'),
      ('s', '...'), ('t', '−')}

RU = {('н', '−.'), ('э', '..−..'), ('т', '−'), ('ы', '−.−−'), ('у', '..−'), ('ж', '...−'),
      ('я', '.−.−'), ('ъ', '−−.−−'), ('п', '.−−.'), ('к', '−.−'), ('е', '.'), ('с', '...'),
      ('р', '.−.'), ('з', '−−..'), ('м', '−−'), ('щ', '−−.−'), ('г', '−−.'), ('ь', '−..−'),
      ('х', '....'), ('й', '.−−−'), ('ю', '..−−'), ('ш', '−−−−'), ('д', '−..'), ('и', '..'),
      ('о', '−−−'), ('а', '.−'), ('б', '−...'), ('ф', '..−.'), ('л', '.−..'),
      ('ц', '−.−.'), ('в', '.−−'), ('ч', '−−−.')}

MorseCode = EN | RU  # не понял как с двумя языками декодировать


def prepare(text):
    text = text.lower()
    text = ''.join(i for i in text if i.isalpha() or i.isspace())
    return text


def encode_to_morse(text):
    translate = dict(MorseCode)
    text = prepare(text)
    res = ' '.join(translate.get(i, ' ') for i in text)
    res = res.replace('   ', '\t')
    return res


def decode_from_morse(code, lang='RU'):
    if lang not in {k for k, v in globals().items() if isinstance(v, set)}:
        raise ValueError('Неверный язык')
    translate = {v: k for k, v in eval(lang)}
    res = ' '.join(''.join(translate[j] for j in i.split()) for i in code.split('\t'))
    return res


def main():
    mode = input('Что делать будем? (кодировать или декодировать): ')
    while mode not in ('кодировать', 'декодировать'):
        print('Выберете один из способов: "кодировать" или "декодировать"')
        mode = input('Что делать будем? (кодировать или декодировать): ')
    text = input('Давайте сюда, что там у вас:\n')
    if mode == 'кодировать':
        res = encode_to_morse(text)
    else:
        must_lang = ", ".join(k for k, v in globals().items() if isinstance(v, set) and k.isupper())
        lang = input(f'Выберете язык: ({must_lang}): ')
        res = decode_from_morse(text, lang=lang)
    print('Вот результат:', res, sep='\n')
