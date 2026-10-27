
import cv2
import numpy as np


def sauvola(image, window_size=15, k=0.2, R=128):
    # Переводим изображение в float
    image = image.astype(np.float32)

    # Вычисляем среднюю яркость локального окна
    mean = cv2.boxFilter(
        image,
        -1,
        (window_size, window_size),
        normalize=True
    )

    # Вычисляем среднее значение квадратов
    mean_square = cv2.boxFilter(
        image ** 2,
        -1,
        (window_size, window_size),
        normalize=True
    )

    # Вычисляем дисперсию
    variance = mean_square - mean ** 2

    # Убираем возможные отрицательные значения
    variance = np.maximum(variance, 0)

    # Вычисляем стандартное отклонение
    std = np.sqrt(variance)

    # Вычисляем локальный порог Сауволы
    threshold = mean * (1 + k * (std / R - 1))

    # Выполняем бинаризацию
    result = np.where(image > threshold, 255, 0)

    return result.astype(np.uint8)



