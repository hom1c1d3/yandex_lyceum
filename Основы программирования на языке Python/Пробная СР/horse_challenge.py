humpbacked_horse = float(input())
horse1 = float(input())
horse2 = float(input())
night = int(input())
screw_up = float(input())

if humpbacked_horse * night >= screw_up:
    humpbacked_horse = True
    print('Конек-Горбунок', end=' ')
if horse1 * night >= screw_up:
    horse1 = True
    print('Лошадиный брат - 1', end=' ')
if horse2 * night >= screw_up:
    horse2 = True
    print('Лошадиный брат - 2')

if not any(isinstance(i, bool) for i in (humpbacked_horse, horse1, horse2)):
    print('Не они!')
