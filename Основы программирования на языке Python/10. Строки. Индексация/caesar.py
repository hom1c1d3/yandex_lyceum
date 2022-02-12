num_letters_alpha = 32  # без ё
first_letter_alpha = 'А'
offset = int(input())
string = input()
res = ''

for letter in string:
    if letter.isalpha():
        if letter.isupper():
            letter_offset = chr((((ord(letter) + offset)
                                  - ord(first_letter_alpha)) % num_letters_alpha
                                 + ord(first_letter_alpha)))
        else:
            letter_offset = chr((((ord(letter) + offset)
                                  - ord(first_letter_alpha.lower())) % num_letters_alpha
                                 + ord(first_letter_alpha.lower())))
    else:
        letter_offset = letter
    res += letter_offset

print(res)
