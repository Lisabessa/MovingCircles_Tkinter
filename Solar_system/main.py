from tkinter import *

import cosmic_bodies

size = 600
root = Tk()
root.attributes("-alpha", 0.95)
canvas = Canvas(root, width=size, height=size, bg='grey')
canvas.pack()

sun = cosmic_bodies.Sun(60, '#FFEC8B', size, canvas)
planet1 = cosmic_bodies.Planet(18, sun, 70, '#C4C4C4', 1, 50, 120, canvas)
planet2 = cosmic_bodies.Planet(12, sun, 80, '#C4C4C4', -1, 100, 10, canvas)
planet3 = cosmic_bodies.Planet(23, sun, 230, '#C4C4C4', -1, 18, 230, canvas)
planet4 = cosmic_bodies.Planet(38, sun, 120, '#C4C4C4', -1, 1, 300, canvas)
planet5 = cosmic_bodies.Planet(15, sun, 100, '#C4C4C4', 1, 15, 90, canvas)
moon1 = cosmic_bodies.Planet(5, planet3, 45, 'black', -1, 100, 180, canvas)
moon2 = cosmic_bodies.Planet(3, planet3, 40, 'black', 1, 80, 23, canvas)
moon3 = cosmic_bodies.Planet(7, planet3, 52, 'black', -1, 50, 40, canvas)
moon4 = cosmic_bodies.Planet(4, planet4, 48, 'black', -1, 30, 129, canvas)
moon5 = cosmic_bodies.Planet(6, planet4, 55, 'black', 1, 50, 11, canvas)
moon6 = cosmic_bodies.Planet(3, planet5, 25, 'black', -1, 40, 230, canvas)
moon7 = cosmic_bodies.Planet(6, planet5, 35, 'black', -1, 76, 327, canvas)
moon8 = cosmic_bodies.Planet(3, planet2, 17, 'black', 1, 140, 188, canvas)
asteroid1 = cosmic_bodies.Planet(5, sun, 165, '#B2DFEE', 1, 1, 97, canvas)
asteroid2 = cosmic_bodies.Planet(5, sun, 170, '#B2DFEE', -1, 5, 54, canvas)
asteroid3 = cosmic_bodies.Planet(5, sun, 160, '#B2DFEE', 1, 9, 11, canvas)
asteroid4 = cosmic_bodies.Planet(5, sun, 165, '#B2DFEE', -1, 14, 199, canvas)
asteroid5 = cosmic_bodies.Planet(5, sun, 170, '#B2DFEE', 1, 18, 209, canvas)
asteroid6 = cosmic_bodies.Planet(5, sun, 170, '#B2DFEE', -1, 22, 355, canvas)
asteroid7 = cosmic_bodies.Planet(5, sun, 165, '#B2DFEE', 1, 26, 233, canvas)
asteroid8 = cosmic_bodies.Planet(5, sun, 160, '#B2DFEE', -1, 28, 112, canvas)
asteroid9 = cosmic_bodies.Planet(5, sun, 170, '#B2DFEE', 1, 32, 23, canvas)
asteroid10 = cosmic_bodies.Planet(5, sun, 165, '#B2DFEE', -1, 36, 0, canvas)

cosmic_bodies_list = [planet1, planet2, planet3, planet4, planet5, moon1, moon2, moon3, moon4, moon5, moon6, moon7, moon8,
                 asteroid1, asteroid2, asteroid3, asteroid4, asteroid5, asteroid6, asteroid7, asteroid8, asteroid9,
                 asteroid10]

root.after(10, cosmic_bodies.move_planets, cosmic_bodies_list, canvas, root)
root.mainloop()