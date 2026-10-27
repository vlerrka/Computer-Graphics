
import streamlit as st
import cv2
import numpy as np

from PIL import Image

from lab2.filters.niblack import niblack
from lab2.filters.sauvola import sauvola
from lab2.filters.laplacian import laplacian_sharpen
from lab2.filters.unsharp import unsharp_mask


# Настройки страницы
st.set_page_config(
    page_title="Лабораторная работа 2",
    page_icon="🖼️",
    layout="wide"
)

st.title("Лабораторная работа 2")

st.divider()

with st.sidebar:

    st.header("Настройки обработки")

    method = st.selectbox(
        "Выберите метод",
        [
            "Ниблэк",
            "Саувола",
            "Фильтр Лапласа",
            "Unsharp Mask"
        ]
    )

    st.divider()

    params = {}

    if method == "Ниблэк":

        st.subheader("Параметры Ниблэка")

        params["window_size"] = st.slider(
            "Размер локального окна",
            3, 51, 15, step=2
        )

        params["k"] = st.slider(
            "Коэффициент k",
            -1.0, 0.0, -0.2, step=0.05
        )

    elif method == "Саувола":

        st.subheader("Параметры Сауволы")

        params["window_size"] = st.slider(
            "Размер локального окна",
            3, 51, 15, step=2
        )

        params["k"] = st.slider(
            "Коэффициент k",
            0.0, 1.0, 0.2, step=0.05
        )

        params["R"] = st.slider(
            "Параметр R",
            1, 255, 128
        )

    elif method == "Фильтр Лапласа":

        st.subheader("Параметры Лапласа")

        params["alpha"] = st.slider(
            "Сила повышения резкости",
            0.0, 10.0, 1.0, step=0.1
        )

    elif method == "Unsharp Mask":

        st.subheader("Параметры Unsharp Mask")

        params["alpha"] = st.slider(
            "Сила повышения резкости",
            0.0, 5.0, 1.5, step=0.1
        )

        params["sigma"] = st.slider(
            "Радиус размытия",
            0.1, 10.0, 1.5, step=0.1
        )


# Загрузка изображения
uploaded_file = st.file_uploader(
    "Загрузите изображение",
    type=["png", "jpg", "jpeg", "bmp", "tiff"]
)


if uploaded_file is not None:

    # Читаем изображение
    file_bytes = np.frombuffer(
        uploaded_file.getvalue(),
        np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    if image is None:
        st.error("Не удалось открыть изображение.")

    else:

        # Обработка
        if method in ["Ниблэк", "Саувола"]:

            gray = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2GRAY
            )

            if method == "Ниблэк":
                result = niblack(gray, **params)

            else:
                result = sauvola(gray, **params)

        elif method == "Фильтр Лапласа":

            result = laplacian_sharpen(
                image,
                **params
            )

        else:

            result = unsharp_mask(
                image,
                **params
            )

        # Преобразование цветов для отображения
        original_rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        if len(result.shape) == 3:
            result_display = cv2.cvtColor(
                result,
                cv2.COLOR_BGR2RGB
            )
        else:
            result_display = result

        # Отображение изображений
        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Исходное изображение**")
            st.image(
                original_rgb,
                use_container_width=True
            )

        with col2:
            st.markdown("**Результат обработки**")
            st.image(
                result_display,
                use_container_width=True
            )

        # Сохранение результата
        success, encoded_image = cv2.imencode(
            ".png",
            result
        )

        if success:

            st.download_button(
                label="Скачать обработанное изображение",
                data=encoded_image.tobytes(),
                file_name="processed_image.png",
                mime="image/png",
                use_container_width=True
            )

else:

    st.info("Загрузите изображение, чтобы начать обработку.")
