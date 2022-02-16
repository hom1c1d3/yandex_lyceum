import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT title FROM films 
WHERE title LIKE "%Астерикс%" AND title NOT LIKE "%Обеликс%" """).fetchall()

for title, in result:
    print(title)
