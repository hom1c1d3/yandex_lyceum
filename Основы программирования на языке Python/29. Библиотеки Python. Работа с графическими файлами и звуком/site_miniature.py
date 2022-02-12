from PIL import Image


def make_preview(size, n_colors):
    im = Image.open('image.jpg')
    res = im.resize(size)
    res = res.quantize(n_colors)
    res.save('res.bmp')


make_preview((400, 200), 64)