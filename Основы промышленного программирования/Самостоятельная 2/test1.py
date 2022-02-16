import csv

lat, lon = float(input()), float(input())

with open('best_things.csv') as f:
    reader = csv.reader(f, delimiter=':')
    header = next(reader)
    res = {i[-1] for i in reader if abs(float(i[1])) >= lat and abs(float(i[2])) >= lon}

print(*res, sep='\n')
