from math import cos, sin, radians


class Sun:
    def __init__(self, radius, color, size, canvas):
        self.radius = radius
        x0 = size // 2 - radius
        x1 = size // 2 + radius
        self.object = canvas.create_oval(x0, x0, x1, x1, fill=color)


class Planet:
    def __init__(self, radius, center_object, distance, color, direction, speed, angle, canvas):
        self.radius = radius
        self.center_object = center_object
        self.distance = distance
        self.color = color
        self.direction = direction
        self.speed = speed
        self.object = canvas.create_oval(0, 0, radius, radius, fill=color)
        self.angle = angle


def move_planets(cosmic_bodies_list, canvas, root):
    for cosmic_body in cosmic_bodies_list:
        if cosmic_body.angle >= 360:
            cosmic_body.angle %= 360
        x = cosmic_body.distance * cos(radians(cosmic_body.angle))
        y = cosmic_body.distance * sin(radians(cosmic_body.angle))
        if cosmic_body.direction < 0:
            cosmic_body.angle -= (1 + cosmic_body.speed // 8)
        else:
            cosmic_body.angle += (1 + cosmic_body.speed // 8)
        x0, y0, x1, y1 = canvas.coords(cosmic_body.center_object.object)
        canvas.coords(cosmic_body.object,
                      x0 + cosmic_body.center_object.radius + x - cosmic_body.radius,
                      y0 + cosmic_body.center_object.radius + y - cosmic_body.radius,
                      x1 - cosmic_body.center_object.radius + x + cosmic_body.radius,
                      y1 - cosmic_body.center_object.radius + y + cosmic_body.radius)
    root.after(30, move_planets, cosmic_bodies_list, canvas, root)