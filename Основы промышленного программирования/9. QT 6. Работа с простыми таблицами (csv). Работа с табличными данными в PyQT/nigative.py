with open('input.bmp', 'rb') as f:
    header = f.read(54)
    data = []
    while True:
        try:
            value = f.read(1)
            value = int(value.hex(), 16)
        except ValueError:
            break
        value = 255 - value
        data.append(value)

with open('res.bmp', 'wb') as f:
    f.write(header)
    f.write(bytes(data))