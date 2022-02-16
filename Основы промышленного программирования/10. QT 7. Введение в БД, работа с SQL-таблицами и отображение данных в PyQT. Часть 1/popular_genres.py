import sqlite3


con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT title FROM genres
 WHERE id IN (SELECT genre FROM films WHERE year BETWEEN 2010 AND 2011)""").fetchall()

for title, in result:
    print(title)