import sqlite3


con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT title FROM films""").fetchall()

for title, in result:
    if title.endswith('?'):
        print(title)