def eratosthenes(N):
    simple = 2
    already = {2, 1}
    nums = list(range(1, N + 1))
    res = []

    while simple:
        n = 0
        while n < len(nums):
            i = nums[n]
            if i % simple == 0 and i != simple:
                res.append(i)
                nums.remove(i)
            else:
                n += 1
        simple = min(set(nums) - already, default=0)
        already.add(simple)
    print(res)


eratosthenes(1000)