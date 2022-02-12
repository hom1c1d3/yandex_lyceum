from PIL import ImageDraw, Image


class MyImageDraw(ImageDraw.ImageDraw):
    def __init__(self, im, mode=None):
        super().__init__(im, mode)

    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        xy = ImageDraw._compute_regular_polygon_vertices((center_coords, radius), sides, rotation)
        self.polygon(xy, fill, outline)


if __name__ == '__main__':
    im = Image.new('RGB', (800, 600), 'white')
    drawer = MyImageDraw(im)
    drawer.regular_polygon((400, 300), 6, 100, 70, 'grey', 'black')
    im.show()

