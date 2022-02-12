from PIL import Image, ImageDraw

width, height = int(1920 * (280 / 100)), int(1080 * (280 / 100))
# width, height = 280, 100
bg_color = 241, 241, 241
text_color = 59, 64, 72
text_height = height * (70 / 100)
text_width = width * (65 / 280)
line_width = width * (10 / 280)
delta_x = width * (10 / 280)
delta_y = height * (15 / 100)

im = Image.new('RGB', (width, height), bg_color)
drawer = ImageDraw.Draw(im)

drawer.polygon(((delta_x, delta_y),
                (delta_x, height - delta_y),
                (delta_x + line_width, height - delta_y),
                (delta_x + line_width, delta_y + text_height / 5),
                (delta_x + line_width + text_width // 2, height - delta_y - text_height / 5 * 2),
                (delta_x + line_width + text_width, delta_y + text_height / 5),
                (delta_x + line_width + text_width, height - delta_y),
                (delta_x + line_width + text_width + line_width, height - delta_y),
                (delta_x + line_width + text_width + line_width, delta_y),
                (delta_x + line_width + text_width, delta_y),
                (delta_x + line_width + text_width // 2, height - delta_y - text_height / 5 * 3),
                (delta_x + line_width, delta_y)
                ), text_color)
drawer.polygon(((delta_x + line_width + text_width // 2, height - delta_y - text_height / 5 * 2),
                (delta_x + line_width * 2 + text_width, ((text_height / 5) ** 2 * 2) ** 0.5),
                (delta_x + line_width * 2 + text_width,
                 ((text_height / 5) ** 2 * 2) ** 0.5 + (line_width ** 2 * 2) ** 0.5),
                (delta_x + line_width + text_width // 2,
                 height - delta_y - text_height / 5 * 2 + (line_width ** 2 * 2) ** 0.5)), bg_color)

last_letter_size = delta_x + line_width * 2 + text_width

drawer.polygon(
    ((last_letter_size + delta_x + (text_width + line_width * 2) / 2 - line_width / 2, delta_y),
     (last_letter_size + delta_x, height - delta_y),
     (last_letter_size + delta_x + line_width, height - delta_y),
     (last_letter_size + delta_x + line_width + text_width // 2, delta_y + text_height / 5),
     (last_letter_size + delta_x + line_width + text_width, height - delta_y),
     (last_letter_size + delta_x + line_width * 2 + text_width, height - delta_y),
     (last_letter_size + delta_x + (text_width + line_width * 2) / 2 + line_width / 2), delta_y),
    text_color)
drawer.line(
    ((int(last_letter_size + delta_x + line_width + text_width - line_width / 2),
      int(height - delta_y)),
     (int(last_letter_size + delta_x + (text_width + line_width * 2) / 2 - line_width),
      int(delta_y))),
    bg_color, int(line_width))

last_letter_size = last_letter_size + delta_x + line_width * 2 + text_width
text_width = text_width * .8

drawer.polygon(((last_letter_size + delta_x, delta_y),
                (last_letter_size + delta_x + line_width + text_width, height - delta_y),
                (last_letter_size + delta_x + line_width * 2 + text_width, height - delta_y),
                (last_letter_size + line_width + delta_x, delta_y)),
               text_color)
drawer.polygon(((last_letter_size + delta_x, height - delta_y),
                (last_letter_size + delta_x + line_width + text_width, delta_y),
                (last_letter_size + delta_x + line_width * 2 + text_width, delta_y),
                (last_letter_size + delta_x + line_width, height - delta_y)), text_color)
drawer.line(((int(last_letter_size + delta_x + line_width * 1.6), int(height - delta_y)),
             (int(last_letter_size + delta_x + line_width * 2.1 + text_width + line_width / 2),
              int(delta_y))),
            bg_color, int(line_width))

im.save('name.png', 'PNG')
