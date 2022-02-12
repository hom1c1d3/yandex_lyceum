# b = h + r*256 + m*256**2
# b = h + 256(r + m*256), если разделить на 256, то h выпадет в остаток. h = b % 256
# Если нацело разделить b на 256 то мы получим то, что в скобках, b = r + m*256
# b = r + m*256, если получить остаток деления на 256, то выпадет r. r = b % 256
# Если нацело разделить b на 256, то мы получим просто m


blocks_num = int(input())
h = 0
blockchain_correct = True
non_correct_block = -1

for i in range(blocks_num):
    h_prev = h

    b = int(input())
    h = b % 256
    b //= 256
    r = b % 256
    b //= 256
    m = b
    h_check = 37 * (m + r + h_prev) % 256
    if (h != h_check or h >= 100) and blockchain_correct:
        non_correct_block = i
        blockchain_correct = False

print(non_correct_block)
