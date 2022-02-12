import string
import random


def generate_password(m):
    letters_up = string.ascii_uppercase
    letters_low = string.ascii_lowercase
    nums = string.digits
    letters_up = letters_up.replace('I', '').replace('O', '')
    letters_low = letters_low.replace('l', '').replace('o', '')
    nums = nums.replace('1', '').replace('0', '')
    sym = set(letters_up) | set(letters_low) | set(nums)
    passw = random.choice(letters_up) + random.choice(letters_low) + random.choice(nums)
    passw = list(passw) + random.choices(
        list(sym), k=m - 3)
    random.shuffle(passw)
    return ''.join(passw)


def main(n, m):
    already = set()
    for i in range(n):
        passw = generate_password(m)
        while passw in already:
            passw = generate_password(m)
        already.add(passw)
    return list(already)
