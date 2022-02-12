def late(now, classes, bus):
    now, classes = (int(i.split(':')[0]) * 60 + int(i.split(':')[1]) for i in (now, classes))
    delta = classes - now - 5 - 15
    if delta < min(bus):
        return 'Опоздание'
    bus = [i - 5 for i in bus if 0 <= i - 5 <= delta]
    return f'Выйти через {max(bus)} минут' if bus else 'Опоздание'


print(late('12:59', '13:45', [3, 35, 46, 55]))
