num = int(input())
num_list = list(map(int, str(num)))
half_sum = (max(num_list) + min(num_list)) / 2
num_list.pop(num_list.index(max(num_list)))
num_list.pop(num_list.index(min(num_list)))
if half_sum == num_list[0]:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")
