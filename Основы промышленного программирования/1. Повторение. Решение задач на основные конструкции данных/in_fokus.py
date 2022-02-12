from PIL import Image

im: Image.Image = Image.open('image.png')
pixels = im.load()


def get_non_bg_pixels(bg_pixel_coord):
    bg_pixel = pixels[bg_pixel_coord]
    for x in range(im.width):
        non_bg_pixels_row = ((x, y) for y in range(im.height) if pixels[x, y] != bg_pixel)
        if non_bg_pixels_row:
            yield non_bg_pixels_row


min_x = min((j[0] for i in get_non_bg_pixels((0, 0)) for j in i))
max_x = max((j[0] for i in get_non_bg_pixels((0, 0)) for j in i))
min_y = min((j[1] for i in get_non_bg_pixels((0, 0)) for j in i))
max_y = max((j[1] for i in get_non_bg_pixels((0, 0)) for j in i))
res = im.crop((min_x, min_y, max_x + 1, max_y + 1))
res.save('res.png')