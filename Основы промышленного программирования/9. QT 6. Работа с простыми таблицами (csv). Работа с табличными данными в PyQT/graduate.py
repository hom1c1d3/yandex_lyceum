import csv


percent = float(input())

with open('vps.csv') as fp:
    reader = csv.reader(fp, delimiter=';')
    title = next(reader)
    percent_col = title.index('соответствует в %')
    res = [i[0] for i in reader if float(i[percent_col]) >= percent]

print(*res, sep='\n')