from tkinter import *
from random import *
from math import cos, sin, radians


size = 600
point_size = 8
radius = 200
# the speed of movement is the modulus of the number: from 1 to 150
# the direction of movement - sign: "positive" - clockwise "negative" - counterclockwise
speed_and_direction = 25


root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()


def draw_central_circle():
    x0 = size // 2 - radius
    y0 = x0
    x1 = size // 2 + radius
    y1 = x1
    color = choice(['aqua', 'fuchsia', 'orange', 'pink', 'yellow', 'violet', 'chartreuse', 'lime', '#f55c4b'])
    canvas.create_oval(x0, y0, x1, y1, fill=color)


def move_point(angle):
    if angle >= 360:
        angle %= 360
    x = radius * cos(radians(angle))
    y = radius * sin(radians(angle))
    if speed_and_direction < 0:
        angle -= (1 + (abs(speed_and_direction) % 151) // 8)
    else:
        angle += (1 + (abs(speed_and_direction) % 151) // 8)
    canvas.coords(point, size // 2 + x - point_size, size // 2 + y - point_size, size // 2 + x + point_size, size // 2 + y + point_size)
    root.after(150 - (abs(speed_and_direction) % 151) + 30, move_point, angle)


draw_central_circle()
color = choice(['blue', 'green', 'maroon', 'purple', 'indigo'])
point = canvas.create_oval(size // 2 + radius - point_size, size // 2 - point_size, size // 2 + radius + point_size, size // 2 + point_size, fill=color)
root.after(10, move_point, 0)
root.mainloop()