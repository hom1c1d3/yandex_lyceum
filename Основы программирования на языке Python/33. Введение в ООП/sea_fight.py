from itertools import repeat


class SeaMap:
    def __init__(self):
        self._x, self._y = 10, 10  # Размер
        self._shoots = {}
        self._shoot_results = {None: '.', 'miss': '*', 'hit': 'x', 'sink': 'x'}

    def shoot(self, row, col, result):
        if result == 'sink':
            cells_around_sink = dict(zip(self._get_cells_around_sink(row, col), repeat('miss')))
            self._shoots.update(cells_around_sink)
        self._shoots[(row, col)] = result

    def cell(self, row, col):
        return self._shoot_results[self._shoots.get((row, col))]

    def _get_cells_around(self, row, col):
        cells = ((x, y) for x in range(self._x) for y in range(self._y))
        cells_around = filter(
            lambda a: a[0] in range(row - 1, row + 2) and a[1] in range(col - 1, col + 2) and a != (
                row, col), cells)
        return cells_around

    def _get_hit_around_sink(self, row, col):
        result = {(row, col), }

        def inner_rec(row, col):
            hits = {k for k, v in self._shoots.items() if v == 'hit'}
            cells_around_sink = set(self._get_cells_around(row, col))
            hits = hits & cells_around_sink
            hits = {i for i in hits if i not in result}
            if not hits:
                return {(row, col), }
            result.update(hits)
            return result | hits | inner_rec(*list(hits)[0]) | inner_rec(*list(hits)[-1])

        result = inner_rec(row, col)
        return result

    def _get_cells_around_sink(self, row, col):
        cells = set()
        hits = self._get_hit_around_sink(row, col)
        for i in hits:
            cells |= set(self._get_cells_around(*i))
        cells -= (set(self._shoots) | hits)
        return cells


sm = SeaMap()

sm.shoot(0, 2, 'hit')
sm.shoot(0, 3, 'sink')

sm.shoot(3, 4, 'hit')
sm.shoot(3, 5, 'hit')
sm.shoot(3, 6, 'sink')

sm.shoot(6, 4, 'hit')
sm.shoot(6, 6, 'hit')
sm.shoot(6, 5, 'sink')

sm.shoot(8, 7, 'hit')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
