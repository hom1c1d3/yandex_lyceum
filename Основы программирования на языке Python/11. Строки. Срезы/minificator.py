num_strings = int(input())


def find_in_quotes(s):
    i = (min(s.find("'"), s.find('"'))
         if s.find("'") > 0 and s.find('"') > 0
         else max(s.find("'"), s.find('"'), 0))
    open_s = s[i] if i and s else ''
    s_close_i = s.replace(f'{open_s}', '\\', 1).replace(rf'\{open_s}', r'\\').find(open_s)
    s_arg = s[i:s_close_i + 1]
    return s_arg if i != -1 and (s_arg and s_close_i) else ''


def get_strings(s):
    indexes = []
    meet = s.find(find_in_quotes(s))
    s_copy = s[:]
    while meet:
        start, finish = meet, meet + len(find_in_quotes(s_copy))
        indexes.append((start, finish))
        s_copy = s[finish:]
        meet = s.find(find_in_quotes(s_copy))
    return indexes


for _ in range(num_strings):
    string = input()
    if string.startswith('#'):
        string = ''
        continue
    start_ind = string.index(string.lstrip()[0])
    string_in_quotes = get_strings(string)
    if not string_in_quotes:
        string = (' ' * start_ind +
                  ' '.join(
                      string[start_ind:].split())
                  )
        grid = string.find('#')
        string = string.replace(string[grid:], '').rstrip() if grid > 0 else string
    else:
        res = ' ' * start_ind
        for st, f in string_in_quotes:
            res += ' '.join(string.split(string[st:f])[0].split())
            if '#' in res:
                res = res.replace(res[res.find('#'):], '')
                string_in_quotes = [(0, len(string))]
                break
            else:
                res += string[st:f]
        after_all = string[string_in_quotes[-1][-1]:]
        after_all = f'{" " * int(bool(after_all.rstrip().count(" ")))}' \
                    f'{after_all.strip()}' \
                    f'{" " * int(bool(after_all.lstrip().count(" ")))}'
        grid = after_all.find('#')
        res += after_all.replace(after_all[grid:], '').rstrip() if grid > 0 else after_all
        string = res
    print(string)
