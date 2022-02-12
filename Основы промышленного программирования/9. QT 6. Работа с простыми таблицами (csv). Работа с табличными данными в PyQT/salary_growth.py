import csv

with open('salary.csv', encoding='utf8') as fd:
    salaries = csv.DictReader(fd, delimiter=';')
    salaries = list(salaries)

federal_district = input()
start_year, finish_year = input().split()

salaries = [row for row in salaries if row['Федеральный округ'] == federal_district]
salaries = [{k: row[k] for k in row if k in ('Субъект', start_year, finish_year)}
            for row in salaries]
if not salaries:
    res = ''
else:
    header = salaries[0].keys()
    salaries = [i.values() for i in salaries]
    res = [(region, start_salary, finish_salary)
           for region, start_salary, finish_salary in salaries
           if (float(finish_salary) / float(start_salary) - 1) * 100 < 4]
if not res:
    res = ''
with open('out_file.csv', 'w') as fd:
    writer = csv.writer(fd, delimiter=';')
    if res == '':
        fd.write('')
        exit()
    writer.writerow(header)
    writer.writerows(res)
