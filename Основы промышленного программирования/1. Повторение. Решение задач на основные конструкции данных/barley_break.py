from PIL import Image

im: Image.Image = Image.open('image.bmp')
width = im.width
width_step = width // 4
height = im.height
height_step = height // 4
for col in range(0, width, width_step):
    for row in range(0, height, height_step):
        piece_im = im.crop((col, row, col + width_step, row + height_step))
        col_num, row_num = row // width_step + 1, col // height_step + 1
        if (col_num, row_num) == (4, 4):
            continue
        piece_im.save(fr'image{col_num}{row_num}.bmp')