n, m = int(input()), int(input())
numbers = {}

for i in range(n):
    nums = input().split()
    for j in range(m):
        numb = int(nums[j])
        if numb in numbers:
            numbers[numb][0] += (i,)
            numbers[numb][0] = tuple(sorted(set(numbers[numb][0])))
            numbers[numb][1] += (j,)
            numbers[numb][1] = tuple(sorted(set(numbers[numb][1])))
        else:
            numbers[numb] = [(i,), (j,)]

print(numbers)
