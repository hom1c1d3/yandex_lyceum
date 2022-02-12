money = int(input())
herd_num = int(input())
byk_cost = 20
cow_cost = 10
telenok_cost = 5

for byk in range(1, money // byk_cost + 1):
    for cow in range((money - byk * byk_cost) // cow_cost + 1):
        telenok = herd_num - byk - cow
        if byk * byk_cost + cow * cow_cost + telenok * telenok_cost == money:
            print(byk, cow, telenok)