from PIL import Image, ImageDraw


def picture(file_name, width, height,
            sky_color='#87CEEB', ocean_color='#017B92',
            boat_color='#874535', sail_color='#FFFFFF', sun_color='#FFCF40'):
    im = Image.new('RGB', (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)), ocean_color)
    drawer.ellipse(((int(0.8 * width), -int(0.2 * height)),
                    (int(1.2 * width), int(0.2 * height))), sun_color)

    drawer.polygon(((width * .49, height * .3),
                    (width * .49, height * .65),
                    (width * .25, height * .65),
                    (width * .3, height * .85),
                    (width * .7, height * .85),
                    (width * .75, height * .65),
                    (width * .51, height * .65),
                    (width * .51, height * .3)), boat_color)
    drawer.polygon(((width * .51, height * .3),
                    (width * .51, height * .6),
                    (width * .66, height * .45)), sail_color)
    im.save(file_name)
