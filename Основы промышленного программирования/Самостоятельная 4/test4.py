import sqlite3


class VisitBombay:

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)

    def selection(self, town, attraction):
        cur = self.con.cursor()
        res = cur.execute(
            "SELECT name, duration, cost FROM registry WHERE town_id = (SELECT id FROM towns WHERE town = ?) AND "
            "type_id = (SELECT id FROM attractions WHERE type = ?)",
            (town, attraction))
        res = sorted(res, key=lambda x: (x[1], x[0]))
        cur.close()
        res = [", ".join(map(str, i)) for i in res]
        return res if res else [None]

    def interest(self, attraction):
        cur = self.con.cursor()
        res = cur.execute("""SELECT towns.town, registry.name FROM towns INNER JOIN registry ON towns.id == 
        registry.town_id INNER JOIN attractions ON registry.type_id = (SELECT attractions.id FROM attractions WHERE 
        attractions.type = ?)""", (attraction,))
        res = sorted(set(res), reverse=True)
        return res
