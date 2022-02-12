menu = {}
for _ in range(int(input())):
    ice_cream_name, price = input().split('\t')
    price = int(price)
    menu[ice_cream_name] = price
input()
orders_earnings = [0]
order = input()
while order != '.':
    if not order:
        orders_earnings.append(0)
        order = input()
        continue
    ice_cream_name, count = order.split('\t')
    count = int(count)
    order_earn = menu[ice_cream_name] * count
    orders_earnings[-1] += order_earn
    order = input()

orders_earnings = list(filter(None, orders_earnings))
for ind, i in enumerate(orders_earnings, 1):
    print(f'{ind})', i)
print('Итого:', sum(orders_earnings))