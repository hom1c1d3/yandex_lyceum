from sys import stdin
source_word = input()
words = stdin.read()
words = words.splitlines()
res = []
for i in words:
    src_word = list(source_word)
    for j in i:
        try:
            src_word.remove(j)
        except ValueError:
            src_word = None
            break
    if src_word is not None:
        res.append(i)
print(len(res), *res, sep='\n')