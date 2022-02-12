num = int(input())

k = 1
k_list = []
remains = []
while k not in k_list:
    k_list.append(k)
    remains.append(10 * k // num)
    k = 10 * k % num

print(*remains[k_list.index(k):], sep='')
