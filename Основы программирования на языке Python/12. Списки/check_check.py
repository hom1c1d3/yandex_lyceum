n, whole_sum = input().split()
n, whole_sum = int(n), int(whole_sum)
check_items = [''.join(input().split()) for _ in range(n)]
true_prices = [int(eval(i.split('=')[0])) for i in check_items]
difference_sums = whole_sum - sum(true_prices)
if not difference_sums:
    print(difference_sums)
    exit()

print(difference_sums)
not_conformity = [ind + 1 for ind in range(len(check_items))
                  if eval(check_items[ind].split('=')[0]) != int(check_items[ind].split('=')[1])]
print(*not_conformity)