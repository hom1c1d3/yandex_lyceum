import csv


with open('input_ways.csv') as fd:
    reader = csv.reader(fd, delimiter=';')
    *raw_paths, from_to = reader

paths = {frm: {} for frm, *_ in raw_paths}
for frm, to, price in raw_paths:
    paths[frm][to] = float(price)

res_path = {}
frm, to, _ = from_to
for node in paths[frm]:
    nxt_nodes = paths.get(node, [])
    if not nxt_nodes:
        if node == to:
            res_path[(node,)] = paths[frm][node]
        continue
    for nxt_node in nxt_nodes:
        if nxt_node == to:
            res_path[(node, nxt_node)] = paths[frm][node] + paths[node][nxt_node]

res_path = (frm,) + min(res_path.items(), key=lambda x: x[1])[0]
print(*res_path)