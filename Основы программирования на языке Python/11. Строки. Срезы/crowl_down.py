instruction = input()
symbol = instruction[0]
instruction = instruction[1:]

length = 1
res = symbol
for arrow in instruction:
    if arrow == '>':
        res += symbol
        length += 1
    elif arrow == 'V':
        res += '\n'
        res += symbol.rjust(length)
    elif arrow == '<':
        to = res[:res.rfind('\n') + 1]
        length -= 1
        after = (symbol.rjust(length) + res[res.rfind('\n'):].lstrip())
        res = to + after

print(res)
