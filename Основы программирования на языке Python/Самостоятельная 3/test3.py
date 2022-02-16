from PIL import Image, ImageDraw


def chief(filename, w, *colors):
    im = Image.new('RGB', (w * 6, w * 6), (255, 255, 255))
    drawer = ImageDraw.Draw(im)

    drawer.ellipse(((0, 0), (w * 6, w * 6)), fill=colors[0])
    drawer.ellipse(((w, w * 1.5), (w * 6, w * 4.5)), fill=colors[1])
    drawer.ellipse(((w * 3.75, w * 2.25), (w * 5.25, w * 3.75)), fill=colors[2])

    drawer.line(((w, w * 3), (w * 3, w * 6)), fill=colors[3], width=2)
    drawer.line(((w * 4.5, w * 3), (w * 3, w * 6)), fill=colors[3], width=2)
    drawer.line(((w * 6, w * 3), (w * 3, w * 6)), fill=colors[3], width=2)

    im.save(filename)


chief('img.png', 40, '#BFBFBF', '#FFF', '#FFC000', '#00B050')
