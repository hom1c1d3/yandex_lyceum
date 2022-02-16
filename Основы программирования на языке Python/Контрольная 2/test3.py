from PIL import Image, ImageOps


def flattery(file_name, save_name):
    im = Image.open(file_name)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            g += int(((r + b) / 2) / 2)
            g = 255 if g > 255 else g
            r -= 20
            r = 0 if r < 0 else r
            b -= 20
            b = 0 if b < 0 else b
            pixels[i, j] = r, g, b
    res = ImageOps.flip(im)
    res.save(save_name)