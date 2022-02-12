with open('prices.txt', encoding='utf8') as f:
    data = f.read()

res = 0

for i in data.splitlines():
    name, cnt, price = i.split('\t')
    cnt, price = int(cnt), float(price)
    res += cnt * price


print(f'{res:.2f}')