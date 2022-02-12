# Следуйте правилам python
# Экранируйте слеши (при вводе через input это не требуется)
# Все что в одинарных или двойных кавычках - одная ячейка

test = """'Дама,сдавала', в багаж
'диван, \\' чемодан,', саквояж,
'картину,\\' \\n корзину,картину', 'ка\\'ртонку',
и ,'мален,\\',ькую', собачонку,,"""


def find_in_quotes(s):
    i = min(s.find("'") if s.find("'") > -1 else s.find('"'),
            s.find('"') if s.find('"') > -1 else s.find("'"))
    open_s = s[i] if i > -1 and s else ''
    s_close_i = s.replace(open_s, '}', 1).replace(rf'\{open_s}', r'\\').find(open_s) if open_s \
        else -1
    return i, s_close_i + 1


def quoted_split(s):
    quoted = find_in_quotes(s)
    if quoted[0] == -1:
        if s.strip()[0] == ',':
            return s[s.find(',') + 1:].split(',') if ',' in s else []
        else:
            return s.split(',')
    else:
        pre_quoted, after_quoted = s.split(s[slice(*quoted)], 1)
        pre_quoted = pre_quoted[:pre_quoted.rfind(',')]
        return ((pre_quoted.split(',') if pre_quoted else [])
                + [s[slice(*quoted)][1:-1]]
                + quoted_split(after_quoted))


def make_test():
    table = test.splitlines()
    res = [quoted_split(i) if '"' in i or "'" in i else i.split(',') for i in table]
    return res


def main():
    table = [input() for _ in range(int(input()))]
    res = [quoted_split(i) if '"' in i or "'" in i else i.split(',') for i in table]
    for _ in range(int(input())):
        row, col = map(int, input().split(','))
        print(res[row][col])


if __name__ == '__main__':
    main()

