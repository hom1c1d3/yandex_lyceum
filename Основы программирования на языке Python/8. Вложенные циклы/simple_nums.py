n = int(input())
nums = list(range(2, n + 1))
simple = 2
res = []
wo_zeroes = [1, 2, 3]

while simple**2 <= n:
    rm_nums = nums[nums.index(simple**2)::simple]
    for i in rm_nums:
        nums[nums.index(i)] = 0
    wo_zeroes = list(filter(lambda k: k, nums))
    simple = wo_zeroes[(wo_zeroes.index(simple) + 1) % len(wo_zeroes)]

for j in wo_zeroes:
    if j > n:
        break
    print(j)
