from PIL import Image, ImageDraw


class Drawer:

    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_colors = dict(((j, 'black') for i in draw_map for j in i))
        self.cell_size = cell_size

    def numbers(self):
        return sorted({j for i in self.draw_map for j in i})

    def set_color(self, number, color):
        self.cell_colors[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        width = len(self.draw_map[0]) * self.cell_size
        height = len(self.draw_map) * self.cell_size
        return width, height

    def draw(self):
        im = Image.new('RGB', self.size())
        drawer = ImageDraw.Draw(im)
        for i, row in enumerate(self.draw_map):
            for j, cell in enumerate(row):
                x, y = j * self.cell_size, i * self.cell_size
                drawer.rectangle(
                    ((x, y), (x + self.cell_size, y + self.cell_size)),
                    fill=self.cell_colors[cell]
                                 )
        return im
