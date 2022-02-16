from PIL import Image, ImageOps


def mirror():
    im = Image.open('image.jpg')
    res = ImageOps.mirror(ImageOps.flip(im))
    res.save('res.jpg')
