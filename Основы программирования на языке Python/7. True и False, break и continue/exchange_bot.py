price1 = int(input())
price2 = int(input())
bought = False
price_bought = price1
price_sold = price1

while price2:
    if not bought:
        if price2 > price1:
            price_bought = price2
            bought = True
    else:
        if price2 < price1:
            price_sold = price2
            break
    price1 = price2
    price2 = int(input())

print(price_bought, price_sold, price_sold - price_bought)
