import cv2
import numpy as np


def unsharp_mask(image, alpha=1.5, sigma=1.5):
    blurred = cv2.GaussianBlur(
        image,
        (0, 0),
        sigmaX=sigma
    )

    mask = (
        image.astype(np.float32)
        - blurred.astype(np.float32)
    )

    sharpened = (
        image.astype(np.float32)
        + alpha * mask
    )

    sharpened = np.clip(sharpened, 0, 255)

    return sharpened.astype(np.uint8)