from PIL import Image, ImageFilter


def motion_blur(n):
    im = Image.open('image.jpg')
    res = im.rotate(270).filter(ImageFilter.GaussianBlur(radius=n))
    res.save('res.jpg')