from tkinter import *
from random import *
from tkinter import colorchooser

size = 800
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()


while True:
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime', '#f55c4b'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size // 5)
    canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
    root.update()