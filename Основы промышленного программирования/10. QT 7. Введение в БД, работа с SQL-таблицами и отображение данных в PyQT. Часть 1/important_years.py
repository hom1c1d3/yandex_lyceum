import sqlite3


con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT DISTINCT year FROM films
    WHERE title like "Х%" """).fetchall()

for year, in result:
    print(year)