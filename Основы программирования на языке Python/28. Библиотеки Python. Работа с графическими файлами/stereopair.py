from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    r, g, b = im.split()
    r = r.rotate(0, translate=(delta, 0))
    anagliph = Image.merge('RGB', (r, g, b))
    anagliph.save('res.jpg')
