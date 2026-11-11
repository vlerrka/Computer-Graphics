def bresenham_circle(cx, cy, radius):
    points = set()

    x = 0
    y = radius

    decision = 3 - 2 * radius

    while x <= y:

        points.update([
            (cx + x, cy + y),
            (cx - x, cy + y),
            (cx + x, cy - y),
            (cx - x, cy - y),

            (cx + y, cy + x),
            (cx - y, cy + x),
            (cx + y, cy - x),
            (cx - y, cy - x)
        ])

        if decision < 0:
            decision += 4 * x + 6
        else:
            decision += 4 * (x - y) + 10
            y -= 1

        x += 1

    return sorted(points)