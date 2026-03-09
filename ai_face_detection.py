import cv2
import numpy as np


def ai_face_score(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    left = edges[:, :edges.shape[1]//2]
    right = edges[:, edges.shape[1]//2:]

    symmetry = abs(np.mean(left) - np.mean(right))

    return float(symmetry)