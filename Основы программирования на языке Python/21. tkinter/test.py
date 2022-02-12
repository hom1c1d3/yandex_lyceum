import tkinter

master = tkinter.Tk()
HEIGHT, WIDTH = 600, 600
canvas = tkinter.Canvas(master, bg='white', height=HEIGHT, width=WIDTH)


def make_field(length=8):
    start, end = [0, 0], [0, 600]
    step = HEIGHT / length
    for i in range(length):
        canvas.create_line(start, end)
        canvas.create_line(start[::-1], end[::-1])
        start[0], end[0] = start[0] + step, end[0] + step


def make_shashki(length=8):
    step = HEIGHT / length
    coord = 0, 0
    for j in range(length // 2 - 1):
        for i in range(0, length + (length // 2 - 2), 2):
            canvas.create_oval(coord, (coord[0] + step, coord[1] + step), fill='#ED462F')
            second = WIDTH - coord[0], HEIGHT - coord[1]
            canvas.create_oval(second, (second[0] - step, second[1] - step), fill='#1A4AFB')
            coord = coord[0] + step * 2, coord[1]
        coord = -step * ((j % (length // 2 - 1)) + 1), coord[1] + step


make_field()
make_shashki()
canvas.pack()
master.mainloop()
