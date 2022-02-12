import sqlite3

artist = input()

con = sqlite3.connect('music_db.sqlite')

cur = con.cursor()

query = f"""SELECT DISTINCT Name FROM Track 
WHERE AlbumId IN (SELECT AlbumId FROM Album WHERE 
ArtistId = (SELECT ArtistId FROM Artist WHERE Name = "{artist}")) ORDER BY Name"""


result = cur.execute(query).fetchall()

for name, in result:
    print(name)