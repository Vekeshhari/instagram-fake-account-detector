import os

from image_forensics.jpeg_analysis import error_level_analysis
from image_forensics.pixel_analysis import detect_clone
from image_forensics.advanced_forensics import noise_inconsistency
from image_forensics.ai_face_detection import ai_face_score


def analyze_images(folder):

    results = []

    for root, _, files in os.walk(folder):

        for f in files:

            if not f.lower().endswith(".jpg"):
                continue

            path = os.path.join(root, f)

            r = {
                "image": path,
                "clone_score": detect_clone(path),
                "noise_score": noise_inconsistency(path),
                "ai_face_score": ai_face_score(path),
                "ela": error_level_analysis(path)
            }

            results.append(r)

    return results  