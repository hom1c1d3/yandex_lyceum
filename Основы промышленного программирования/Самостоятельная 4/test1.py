from sys import stdin

conditionals = input()
strings = stdin.read().splitlines()

res = []

min_strings = []

for sym in conditionals:
    min_string = ""
    sym_count = float("inf")
    for string in strings:
        cnt = string.count(sym)
        if cnt and cnt < sym_count:
            sym_count = cnt
            min_string = string
    min_strings.append((min_string, sym))

diff_symbols_count = []

for string, sym in min_strings:
    diff_symbols = set(string) - {sym, }
    diff_symbols_count.append(len(diff_symbols))


print(*diff_symbols_count)