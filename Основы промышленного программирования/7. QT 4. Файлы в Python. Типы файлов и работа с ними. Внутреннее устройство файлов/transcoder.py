transcode_table = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
                   "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
                   "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
                   "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
                   "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
                   "б": "b", "ю": "ju", "ё": "jo"}


with open('cyrillic.txt', encoding='utf8') as f:
    data = f.read()

new_data = ''

for i in data:
    if i.lower() not in transcode_table:
        new_data += i
        continue
    transcode_letter = transcode_table[i.lower()]
    if i.isupper():
        transcode_letter = transcode_letter.capitalize()
    new_data += transcode_letter


with open('transliteration.txt', 'w', encoding='utf8') as f:
    f.write(new_data)
