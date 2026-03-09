from skimage.feature import match_template
import cv2


def detect_clone(image_path):

    img = cv2.imread(image_path, 0)

    if img is None:
        return None

    h, w = img.shape

    if h < 100 or w < 100:
        return None

    th, tw = min(100, h//3), min(100, w//3)

    template = img[h//4:h//4+th, w//4:w//4+tw]

    try:
        result = match_template(img, template)
        return float(result.max())
    except:
        return None