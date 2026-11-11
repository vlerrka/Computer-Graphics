import math


def round_pixel(value):
    if(value >= 0):
        return math.floor(value + 0.5)
    else:
        return math.ceil(value - 0.5)

def step_by_step_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if (dx == 0) & (dy == 0):
        return [(x1, y1)]

    points = []

    if abs(dx) >= abs(dy):
        step = 1 if dx > 0 else -1

        for x in range(x1, x2 + step, step):
            y = y1 + dy * (x - x1) / dx
            points.append((x, round_pixel(y)))

    else:
        step = 1 if dy > 0 else -1

        for y in range(y1, y2 + step, step):
            x = x1 + dx * (y - y1) / dy
            points.append((round_pixel(x), y))

    return points