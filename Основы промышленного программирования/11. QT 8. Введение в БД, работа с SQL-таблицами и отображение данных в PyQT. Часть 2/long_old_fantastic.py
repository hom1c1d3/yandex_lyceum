import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE from films
     WHERE genre = (SELECT id FROM genres WHERE title = "фантастика") AND year < 2000 AND duration > 90 """)
    con.commit()