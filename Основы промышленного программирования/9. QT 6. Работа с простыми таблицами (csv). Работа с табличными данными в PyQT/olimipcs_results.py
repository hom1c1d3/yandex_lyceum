import csv

school, form = input().split()
school, form = int(school), int(form)

with open('rez.csv', 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    title = next(reader)
    data = []
    for i in reader:
        a, b = i[2].rsplit('-', 3)[1:-1]
        a, b = int(a), int(b)
        if [a, b] == [school, form]:
            data.append((i[1].split()[-2], int(i[-1])))


for a, b in sorted(data, key=lambda x: (x[1], x[0]), reverse=True):
    print(a, b)