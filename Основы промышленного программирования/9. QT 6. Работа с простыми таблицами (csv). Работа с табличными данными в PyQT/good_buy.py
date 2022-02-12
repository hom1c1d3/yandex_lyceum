import csv

money = 1000

with open('wares.csv', encoding='utf-8') as fp:
    reader = csv.reader(fp, delimiter=';')
    data = [[a, float(b)] for a, b in reader]

res = []
current_ware, price = min(data, key=lambda x: x[1])
while price <= money:
    for i in range(10):
        money -= price
        res.append(current_ware)
        if price > money:
            break
    current_ware, price = min(data, key=lambda x: x[1] if x[0] not in res else float('inf'))

if res:
    print(*res, sep=', ')
else:
    print('error')