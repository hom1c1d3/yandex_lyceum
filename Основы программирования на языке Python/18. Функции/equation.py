def equation(a, b):
    x0, y0 = map(float, a.split(';'))
    x1, y1 = map(float, b.split(';'))
    if x0 == x1:
        return print(x0)
    elif y0 == y1:
        return print(y0)
    k = (y1 - y0) / (x1 - x0)
    b = y0 - k * x0
    print(k, b)


equation('2.5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла;3', '-2;5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла')