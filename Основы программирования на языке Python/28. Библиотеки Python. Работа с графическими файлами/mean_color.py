from PIL import Image

im = Image.open('image.jpg')
pixels = im.load()
x, y = pixels.size()
num_pixels = x * y
R, G, B = 0, 0, 0

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        R += r
        G += g
        B += b

res = map(lambda a: a // num_pixels, (R, G, B))
print(*res)