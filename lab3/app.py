
import streamlit as st
import matplotlib.pyplot as plt

from algorithms.step_by_step import step_by_step_line
from algorithms.dda import dda_line
from algorithms.bresenham_line import bresenham_line
from algorithms.bresenham_circle import bresenham_circle

from visualization.drawing import draw_pixels


st.set_page_config(
    page_title="Растровые алгоритмы",
    layout="wide"
)

st.title("Лабораторная работа №3")
st.subheader("Базовые растровые алгоритмы")

algorithm = st.selectbox(
    "Выбери алгоритм",
    [
        "Пошаговый алгоритм",
        "Алгоритм ЦДА",
        "Алгоритм Брезенхема (линия)",
        "Алгоритм Брезенхема (окружность)"
    ]
)

st.divider()

# Ползунок масштаба
scale = st.slider(
    "Масштаб изображения",
    min_value=1.0,
    max_value=8.0,
    value=1.0,
    step=0.5,
    format="%.1fx"
)

st.caption(f"Текущий масштаб: {scale}x")

if algorithm == "Алгоритм Брезенхема (окружность)":

    st.write("### Построение окружности")

    col1, col2, col3 = st.columns(3)

    with col1:
        cx = st.number_input("Центр X", value=0, step=1)

    with col2:
        cy = st.number_input("Центр Y", value=0, step=1)

    with col3:
        radius = st.number_input(
            "Радиус",
            min_value=1,
            value=5,
            step=1
        )

    pixels = bresenham_circle(
        int(cx), int(cy), int(radius)
    )

    fig = draw_pixels(
        pixels,
        title="Окружность — алгоритм Брезенхема",
        center=(cx, cy),
        scale=scale
    )

else:

    st.write("### Построение отрезка")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Начало X", value=1, step=1)
        y1 = st.number_input("Начало Y", value=1, step=1)

    with col2:
        x2 = st.number_input("Конец X", value=10, step=1)
        y2 = st.number_input("Конец Y", value=6, step=1)

    if algorithm == "Пошаговый алгоритм":
        pixels = step_by_step_line(
            int(x1), int(y1), int(x2), int(y2)
        )

    elif algorithm == "Алгоритм ЦДА":
        pixels = dda_line(
            int(x1), int(y1), int(x2), int(y2)
        )

    else:
        pixels = bresenham_line(
            int(x1), int(y1), int(x2), int(y2)
        )

    fig = draw_pixels(
        pixels,
        title=algorithm,
        scale=scale
    )

st.pyplot(fig)
plt.close(fig)
