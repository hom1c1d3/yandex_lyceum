from itertools import groupby

UNITS = {'B': 1, 'KB': 1024, 'MB': 1024 * 1024, 'GB': 1024 ** 3, 'TB': 1024 ** 4}

with open('input_files.txt', encoding='utf8') as f:
    data = f.read()

files = []
for i in data.splitlines():
    filename, size, unit = i.split()
    size = int(size)
    files.append((filename, size, unit))

grouped = groupby(sorted(files, key=lambda x: (x[0].rsplit('.')[-1], x[0])),
                  key=lambda x: x[0].rsplit('.')[-1])

f = open('output_files.txt', 'w')
for _, filenames in grouped:
    group_size = 0
    filenames = list(filenames)
    for filename, size, unit in filenames:
        file_size = size * UNITS[unit]
        group_size += file_size
        print(filename, file=f)
    group_unit, group_unit_value = min(((k, v) for k, v in UNITS.items() if group_size / v >= 1),
                                       key=lambda x: group_size / x[1])
    group_size /= group_unit_value
    group_size = round(group_size)
    print('----------', file=f)
    print('Summary:', group_size, group_unit, file=f)
    print(file=f)
f.close()
