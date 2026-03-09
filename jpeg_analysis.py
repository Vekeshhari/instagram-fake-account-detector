import cv2
import numpy as np
import os


def error_level_analysis(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return None

    _, enc = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    recompressed = cv2.imdecode(enc, 1)

    ela = cv2.absdiff(img, recompressed)

    gray = cv2.cvtColor(ela, cv2.COLOR_BGR2GRAY)

    amplified = np.clip(gray * 10, 0, 255).astype(np.uint8)

    heatmap = cv2.applyColorMap(amplified, cv2.COLORMAP_JET)

    outdir = os.path.join(os.path.dirname(__file__), '..', 'ela_output')

    os.makedirs(outdir, exist_ok=True)

    base = os.path.basename(image_path)

    outpath = os.path.join(outdir, f"ela_{base}")

    cv2.imwrite(outpath, heatmap)

    return outpath