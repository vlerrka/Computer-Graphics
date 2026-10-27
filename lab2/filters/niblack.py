
import cv2
import numpy as np


def niblack(image, window_size=15, k=-0.2):
    # Переводим изображение в тип float
    image = image.astype(np.float32)

    # Вычисляем среднюю яркость в локальном окне
    mean = cv2.boxFilter(
        image,
        -1,
        (window_size, window_size),
        normalize=True
    )

    # Вычисляем среднее значение квадратов яркости
    mean_square = cv2.boxFilter(
        image ** 2,
        -1,
        (window_size, window_size),
        normalize=True
    )

    # Вычисляем дисперсию
    variance = mean_square - mean ** 2

    # Защита от отрицательных значений из-за погрешности вычислений
    variance = np.maximum(variance, 0)

    # Вычисляем стандартное отклонение
    std = np.sqrt(variance)

    # Вычисляем локальный порог Ниблэка
    threshold = mean + k * std

    # Преобразуем изображение в черно-белое
    result = np.where(image > threshold, 255, 0)

    return result.astype(np.uint8)



