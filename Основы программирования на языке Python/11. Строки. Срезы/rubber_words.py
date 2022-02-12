word = input()
middle = round(len(word) / 2) if len(word) % 2 == 0 else round(len(word) / 2 + 0.5)
to_middle = word[:middle]
after_middle = word[middle:]
res_to_middle = '\n'.join([(l.rjust(i + 1)).ljust(len(to_middle))
                           for i, l in sorted(enumerate(to_middle))[::-1]])
res_after_middle = '\n'.join([(l.rjust(i + 1))
                              for i, l in enumerate(after_middle)])
res_after_middle = '\n' * (len(res_to_middle.split('\n')) - len(res_after_middle.split('\n'))) \
                   + res_after_middle
res = '\n'.join(a + b for a, b in zip(res_to_middle.split('\n'), res_after_middle.split('\n')))

print(res)
