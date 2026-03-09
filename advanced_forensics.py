import cv2
import numpy as np


def noise_inconsistency(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lap = cv2.Laplacian(gray, cv2.CV_64F)

    score = np.var(lap)

    return float(score)