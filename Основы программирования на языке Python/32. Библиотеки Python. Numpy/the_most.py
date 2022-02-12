import numpy as np

table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")
print(np.sort(table, order=['Energ_Kcal', 'Shrt_Desc'])[::-1][0]['Shrt_Desc'])