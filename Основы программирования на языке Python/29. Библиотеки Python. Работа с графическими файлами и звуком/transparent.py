from PIL import Image


def transparency(filename1, filename2):
    im1 = Image.open(filename1)
    pixels1 = im1.load()
    im2 = Image.open(filename2)
    pixels2 = im2.load()
    x, y = im1.size
    res = Image.new('RGB', (x, y))
    pixels_res = res.load()
    for i in range(x):
        for j in range(y):
            r1, g1, b1 = pixels1[i, j]
            r2, g2, b2 = pixels2[i, j]
            r = int(.5 * r1 + .5 * r2)
            g = int(.5 * g1 + .5 * g2)
            b = int(.5 * b1 + .5 * b2)
            pixels_res[i, j] = r, g, b
    res.save('res.jpg')
