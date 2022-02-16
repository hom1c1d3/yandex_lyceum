import sqlite3

genre = input()

con = sqlite3.connect('music_db.sqlite')

cur = con.cursor()

result = cur.execute(f"""SELECT Title FROM Album
 WHERE AlbumId IN (SELECT AlbumId FROM Track 
 WHERE GenreId = (SELECT GenreId FROM Genre 
 WHERE Name = "{genre}" ) ) ORDER BY ArtistId, Title""").fetchall()

for title, in result:
    print(title)