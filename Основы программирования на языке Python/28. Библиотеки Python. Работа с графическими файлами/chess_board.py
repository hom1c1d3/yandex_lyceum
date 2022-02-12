from PIL import Image, ImageDraw


def board(num, size):
    im_size = num * size
    im = Image.new('RGB', (im_size, im_size))
    drawer = ImageDraw.Draw(im)

    color = False  # черный
    for i in range(0, im_size, size):
        for j in range(0, im_size, size):
            drawer.rectangle(((j, i), (j + size, i + size)),
                             tuple([256 * int(color) for i in range(3)]))
            color = not color
        color = not bool(num % 2) == (not color)
    im.save('res.png', 'PNG')
