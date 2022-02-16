import csv


with open('wares.csv') as fp:
    reader = csv.reader(fp, delimiter=';')
    title = next(reader)
    data = [(a, float(b), float(c)) for a, b, c in reader]


for a, b, c in data:
    if c < b:
        print(a)
