import sys
import csv

min_sum, min_score = map(int, input().split())

data = list(csv.reader(sys.stdin, delimiter=' '))
data = [i[:2] + list(map(int, i[2:])) for i in data]

res = [i + [sum(i[2:]), ] for i in data if sum(i[2:]) >= min_sum and min(i[2:]) >= min_score]

header = ['Фамилия', 'имя', 'результат 1', 'результат 2', 'результат 3', 'сумма']

with open('exam.csv', 'w', encoding='utf8', newline='') as fp:
    writer = csv.writer(fp, delimiter=';')
    writer.writerow(header)
    writer.writerows(res)
