from PIL import Image, ImageDraw


def gradient(color):
    im = Image.new('RGB', (512, 200))
    drawer = ImageDraw.Draw(im)
    color_ind = 'RGB'.index(color)  # индекс для списка RGB
    color_line = [0, 0, 0]

    delta = 0  # расстояние от левого конца до линии
    for _ in range(2**8):
        for _ in range(2):
            drawer.line((delta, 0, delta, 200), tuple(color_line), width=1)
            delta += 1
        color_line[color_ind] += 1
    im.save('res.png', 'PNG')
