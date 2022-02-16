from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, y = im.size
    new_im = Image.new('RGB', (x, y))
    coord_left = (0, 0, x // 2, y)
    coord_right = (x // 2, 0, x, y)
    part_left = im.crop(coord_left)
    part_right = im.crop(coord_right)
    new_im.paste(part_left, coord_right[:2])
    new_im.paste(part_right, coord_left[:2])
    new_im.save(output_file_name)
