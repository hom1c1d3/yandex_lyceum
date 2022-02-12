import sys

gematry = sorted(sys.stdin,
                 key=lambda x: (sum([ord(i) - ord('A') + 1 for i in x.strip().upper()]), x))
print(*map(lambda x: x.strip(), gematry), sep='\n')
#
# lines = map(lambda x: (f'Line {x[0] + 1}', x[1].strip()), enumerate(sys.stdin.readlines()))
# comment = filter(lambda x: x[1].startswith('#'), lines)
# res = map(lambda x: x[0] + ': ' + x[1].replace('#', '', 1).strip(), comment)
# print(*res, sep='\n')