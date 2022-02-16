import sqlite3


con = sqlite3.connect('dutch_herring.db')
cur = con.cursor()

min_size = int(input())
max_weight = int(input())

data = cur.execute(f"""SELECT type, size, quantity FROM Fish
 WHERE size >= {min_size} AND weight <= {max_weight} """).fetchall()
choice = {}
tps = sorted(set(i[0] for i in data))
sizes = sorted(set(i[1] for i in data), reverse=True)
total = sum(i[2] for i in data)
choice['types'] = tps
choice['sizes'] = sizes
choice['total'] = total
