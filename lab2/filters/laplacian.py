import cv2
import numpy as np


def laplacian_sharpen(image, alpha=0.7):
    image_float = image.astype(np.float32)

    laplacian = cv2.Laplacian(
        image_float,
        cv2.CV_32F,
        ksize=1
    )

    sharpened = image_float - alpha * laplacian

    sharpened = np.clip(sharpened, 0, 255)

    return sharpened.astype(np.uint8)