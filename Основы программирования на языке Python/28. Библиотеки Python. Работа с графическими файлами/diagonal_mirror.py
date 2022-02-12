from PIL import Image, ImageOps


def mirror():
    im = Image.open('image.jpg')
    res = ImageOps.mirror(im.rotate(90, expand=True))
    res.save('res.jpg')
