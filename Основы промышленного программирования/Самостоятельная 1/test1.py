color_dict_filename = input()
color_pairs_filename = input()
color = input()

with open(color_dict_filename) as f, open(color_pairs_filename) as f1:
    color_dict = f.read()
    color_groups = f1.read()


color_dict = (i.split(' ', 1) for i in color_dict.splitlines())
color_dict = {a: b for a, b in color_dict}

group_for_color = ()

color_groups = (i.split(' ') for i in color_groups.splitlines())
try:
    color_groups = [tuple(color_dict[i] for i in group) for group in color_groups]
except KeyError:
    group_for_color = ('Error', )

if not group_for_color:
    color_ind = list(color_dict.values()).index(color)
    group_for_color = color_groups[color_ind]

with open('regards.txt', 'w') as f:
    print(*group_for_color, sep='\n', file=f)
