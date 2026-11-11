
import streamlit as st
import matplotlib.pyplot as plt
import time
import pandas as pd

from algorithms.step_by_step import step_by_step_line
from algorithms.dda import dda_line
from algorithms.bresenham_line import bresenham_line
from algorithms.bresenham_circle import bresenham_circle

from visualization.drawing import draw_pixels


# Количество повторений для измерения времени
REPEATS = 1000


def measure_time(function, *args):
    """
    Измеряет среднее время одного запуска алгоритма.
    Возвращает время в миллисекундах и результат алгоритма.
    """

    result = None

    start = time.perf_counter()

    for _ in range(REPEATS):
        result = function(*args)

    end = time.perf_counter()

    average_time = (end - start) / REPEATS * 1000

    return average_time, result


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

scale = st.slider(
    "Масштаб изображения",
    min_value=1.0,
    max_value=8.0,
    value=1.0,
    step=0.5,
    format="%.1fx"
)


# --------------------------------------------------
# ПОСТРОЕНИЕ ОКРУЖНОСТИ
# --------------------------------------------------

if algorithm == "Алгоритм Брезенхема (окружность)":

    st.write("### Параметры окружности")

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

    # Замер времени
    elapsed, pixels = measure_time(
        bresenham_circle,
        int(cx),
        int(cy),
        int(radius)
    )

    st.divider()
    st.write("### Результаты измерения")

    col1, col2 = st.columns(2)

    col1.metric(
        "Среднее время выполнения",
        f"{elapsed:.6f} мс"
    )

    col2.metric(
        "Количество пикселей",
        len(pixels)
    )

    st.caption(
        f"Время рассчитано как среднее значение "
        f"за {REPEATS} запусков алгоритма."
    )

    fig = draw_pixels(
        pixels,
        title="Окружность — алгоритм Брезенхема",
        center=(cx, cy),
        scale=scale
    )

    st.pyplot(fig)
    plt.close(fig)


# --------------------------------------------------
# ПОСТРОЕНИЕ ОТРЕЗКА
# --------------------------------------------------

else:

    st.write("### Параметры отрезка")

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Начало X", value=1, step=1)
        y1 = st.number_input("Начало Y", value=1, step=1)

    with col2:
        x2 = st.number_input("Конец X", value=10, step=1)
        y2 = st.number_input("Конец Y", value=6, step=1)

    args = (
        int(x1),
        int(y1),
        int(x2),
        int(y2)
    )

    # Все три алгоритма получают одинаковые координаты
    algorithms = {
        "Пошаговый алгоритм": step_by_step_line,
        "Алгоритм ЦДА": dda_line,
        "Алгоритм Брезенхема": bresenham_line
    }

    results = {}
    timings = {}

    for name, function in algorithms.items():
        elapsed, pixels = measure_time(function, *args)

        timings[name] = elapsed
        results[name] = pixels

    # Получаем результат выбранного алгоритма
    if algorithm == "Пошаговый алгоритм":
        pixels = results["Пошаговый алгоритм"]

    elif algorithm == "Алгоритм ЦДА":
        pixels = results["Алгоритм ЦДА"]

    else:
        pixels = results["Алгоритм Брезенхема"]

    st.divider()
    st.write("### Результат построения")

    col1, col2 = st.columns(2)

    col1.metric(
        "Время выбранного алгоритма",
        f"{timings.get(algorithm, timings.get('Алгоритм Брезенхема')):.6f} мс"
    )

    col2.metric(
        "Количество пикселей",
        len(pixels)
    )

    fig = draw_pixels(
        pixels,
        title=algorithm,
        scale=scale
    )

    st.pyplot(fig)
    plt.close(fig)

    # Сравнение алгоритмов
    st.divider()
    st.write("### Сравнение времени выполнения")

    table_data = []

    for name, elapsed in timings.items():
        table_data.append({
            "Алгоритм": name,
            "Среднее время (мс)": round(elapsed, 6),
            "Количество пикселей": len(results[name])
        })

    df = pd.DataFrame(table_data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        f"Каждый алгоритм запускался {REPEATS} раз "
        "на одинаковых входных координатах. "
        "Указано среднее время одного запуска."
    )
