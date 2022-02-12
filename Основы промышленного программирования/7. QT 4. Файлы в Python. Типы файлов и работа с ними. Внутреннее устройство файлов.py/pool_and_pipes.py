with open('pipes.txt', 'r', encoding='utf8') as f:
    data = f.read()

single_pipes, using_pipes = data.split('\n \n')
single_pipes = list(map(float, single_pipes.splitlines()))
using_pipes = list(map(int, using_pipes.split()))
using_pipes_time = [single_pipes[i - 1] for i in using_pipes]
speed_sum = sum(1 / i for i in using_pipes_time)  # 1 это весь бассейн
res_time = 1 / speed_sum  # speed_sum это скорость всех используемых труб вместе
res_time = res_time * 60  # получаем минуты
with open('time.txt', 'w', encoding='utf8') as f:
    f.write(str(res_time))