
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math


def draw_pixels(pixels, title="Растровое изображение",
                center=None, scale=1.0):

    pixels = set(pixels)

    fig, ax = plt.subplots(figsize=(9, 9))

    if pixels:
        xs = [p[0] for p in pixels]
        ys = [p[1] for p in pixels]

        min_x = min(xs) - 2
        max_x = max(xs) + 2
        min_y = min(ys) - 2
        max_y = max(ys) + 2
    else:
        min_x, max_x = -5, 5
        min_y, max_y = -5, 5

    # Центр области просмотра
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    # Размер области просмотра.
    # Чем больше scale, тем сильнее приближение.
    half_width = (max_x - min_x + 1) / (2 * scale)
    half_height = (max_y - min_y + 1) / (2 * scale)

    left = center_x - half_width
    right = center_x + half_width
    bottom = center_y - half_height
    top = center_y + half_height

    ax.set_xlim(left, right)
    ax.set_ylim(bottom, top)

    # Рисуем пиксели
    for x, y in pixels:
        square = Rectangle(
            (x - 0.5, y - 0.5),
            1,
            1,
            facecolor="#2685d9",
            edgecolor="none",
            zorder=2
        )
        ax.add_patch(square)

    # Целочисленные координаты, попадающие в область просмотра
    x_start = math.ceil(left - 0.5)
    x_end = math.floor(right - 0.5)
    y_start = math.ceil(bottom - 0.5)
    y_end = math.floor(top - 0.5)

    # Подписи координат в центрах клеток
    ax.set_xticks(range(math.ceil(left), math.floor(right) + 1))
    ax.set_yticks(range(math.ceil(bottom), math.floor(top) + 1))

    # Границы клеток
    ax.set_xticks(
        [x + 0.5 for x in range(x_start, x_end + 1)],
        minor=True
    )
    ax.set_yticks(
        [y + 0.5 for y in range(y_start, y_end + 1)],
        minor=True
    )

    ax.grid(
        which="minor",
        color="#999999",
        linewidth=0.7,
        zorder=3
    )

    # Координатные оси
    ax.axhline(0, color="black", linewidth=1.5, zorder=4)
    ax.axvline(0, color="black", linewidth=1.5, zorder=4)

    # Центр окружности
    if center is not None:
        cx, cy = center
        ax.scatter(
            cx, cy,
            color="red",
            marker="+",
            s=100,
            linewidths=2,
            zorder=5
        )

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"{title} | Масштаб: {scale}x")

    fig.tight_layout()
    return fig
