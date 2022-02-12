import string
import random


def generate_password(m):
    letters = string.ascii_letters
    nums = string.digits
    letters = letters.replace('l', '').replace('I', '').replace('O', '').replace('o', '')
    nums = nums.replace('1', '').replace('0', '')
    sym = list(set(letters) | set(nums))
    random.shuffle(sym)
    passw = ''.join(random.sample(sym, m))
    return passw


def main(n, m):
    already = set()
    for i in range(n):
        passw = generate_password(m)
        while passw in already:
            passw = generate_password(m)
        already.add(passw)
    return list(already)
