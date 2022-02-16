import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    cur.execute("""DELETE from films WHERE title LIKE "Я%а" """)
    con.commit()