import random
f = open('lines.txt', 'r', encoding='utf8')

lines_count = sum(1 for _ in f)
if lines_count == 0:
    exit()
line_num = random.randrange(0, lines_count)
f.seek(0)
for line, i in enumerate(f):
    if line == line_num:
        print(i)
        break
        
f.close()