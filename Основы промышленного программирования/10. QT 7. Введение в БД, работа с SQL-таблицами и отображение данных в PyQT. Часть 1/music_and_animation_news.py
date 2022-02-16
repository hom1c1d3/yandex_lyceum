import sqlite3


con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""SELECT title FROM films
    WHERE genre IN (
    SELECT id FROM genres WHERE title = "музыка" OR title = "анимация")
     AND year >= 1997""").fetchall()

for title, in result:
    print(title)