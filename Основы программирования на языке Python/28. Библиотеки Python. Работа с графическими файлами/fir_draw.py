from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD', snow_color='#FFFAFA',
            trunk_color='#A45A52', needls_color='#01796F', sun_color='#FFDB00'):
    im = Image.new('RGB', (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)), snow_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)),
                    (int(1.2 * width), int(0.2 * height))), sun_color)

    for i in range(1, 4):  # три уровня елки
        drawer.polygon((
            (width * .5, height * .1 * i),
            (width * .5 - (width * .05 + width * .05 * i), height * .1 + height * .2 * i),
            (width * .5 + (width * .05 + width * .05 * i), height * .1 + height * .2 * i)
        ), needls_color)
    drawer.rectangle(((width * .45, height * .7), (width * .55, height * .9)), trunk_color)

    im.save(file_name)
