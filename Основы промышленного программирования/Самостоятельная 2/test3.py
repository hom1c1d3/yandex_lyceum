import sqlite3
import csv


con = sqlite3.connect('fish_base.db')
cur = con.cursor()


def importance(*properties):
    k = f"""SELECT Fish.name, Fish.size, Properties.property
     FROM Fish INNER JOIN Properties
      ON Fish.property_id = Properties.id WHERE {" or ".join(f"Properties.property = '{i}' " for i in properties)} """
    data = cur.execute(k)
    with open('discovery.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['fish', 'size', 'property'])
        data = sorted(data, key=lambda x: (-int(x[1]), x[2]))
        writer.writerows(data)


v = ["glowing", "protein", "low-fat"]
importance(*v)