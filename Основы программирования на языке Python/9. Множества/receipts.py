products = {input() for _ in range(int(input()))}
num_receipts = int(input())

for i in range(num_receipts):
    name_receipt = input()
    ingredients = {input() for _ in range(int(input()))}
    if ingredients <= products:
        print(name_receipt)
