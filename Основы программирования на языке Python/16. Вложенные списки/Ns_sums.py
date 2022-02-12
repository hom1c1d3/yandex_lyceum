n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
whole_sum_Ns = []

for x in range(n - 2):
    for y in range(n - 2):
        N = []
        for i in range(3):
            if i % 2 == 0:
                step = 2
            else:
                step = 1
            for j in range(0, 3, step):
                N.append(matrix[x + i][y + j])
        whole_sum_Ns.append(sum(N))

res = max(whole_sum_Ns)
print(res)