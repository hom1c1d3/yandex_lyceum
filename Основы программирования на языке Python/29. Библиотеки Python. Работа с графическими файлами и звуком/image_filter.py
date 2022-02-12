import random
from PIL import Image

SEED = 3  # число для велечены ближайших слоев
# 1 почти незаметно, 5. QT 2. QtDesigner, pyuic, два способа подключения uic-файла формы еле заметны


def get_layers(i, j, layers):
    start_i = max(0, i - layers)
    stop_i = i + layers
    start_j = max(0, j - layers)
    stop_j = j + layers
    return (((row, col) for col in range(start_j, stop_j)) for row in range(start_i, stop_i))


def image_filter(pixels, i, j):
    """Заменяет пиксел на рандомное значение для каждого канала относиттельно окружения"""
    pixel_layers = [pixels[row, col] for _ in get_layers(i, j, SEED) for row, col in _]
    r_min, g_min, b_min = (min(pixel_layers, key=lambda z: z[a]) for a in range(3))
    r_min, g_min, b_min = list(zip(*(a[b:] for a, b in zip((r_min, g_min, b_min), range(3)))))[0]
    r_max, g_max, b_max = (max(pixel_layers, key=lambda z: z[a]) for a in range(3))
    r_max, g_max, b_max = list(zip(*(a[b:] for a, b in zip((r_max, g_max, b_max), range(3)))))[0]
    return (random.randint(r_min, r_max),
            random.randint(g_min, g_max),
            random.randint(b_min, b_max))


def main():
    im = Image.open('image.jpg')
    pixels = im.load()
    x, y = im.size

    for i in range(x):
        if (i + SEED) < x:
            for j in range(y):
                if (j + SEED) < y:
                    pixels[i, j] = image_filter(pixels, i, j)

    im.save('res.jpg')


if __name__ == '__main__':
    main()