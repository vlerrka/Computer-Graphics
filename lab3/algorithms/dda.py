def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return [(x1, y1)]

    x_inc = dx / steps
    y_inc = dy / steps

    x = float(x1)
    y = float(y1)

    points = []

    for _ in range(steps + 1):
        points.append((round(x), round(y)))

        x += x_inc
        y += y_inc

    return points