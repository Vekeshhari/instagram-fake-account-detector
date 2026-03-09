import subprocess
from PIL import Image
from PIL.ExifTags import TAGS


def extract_metadata(image_path: str) -> dict:
    # Try exiftool first (if installed on system), otherwise fallback to Pillow
    try:
        res = subprocess.run(["exiftool", "-j", image_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0 and res.stdout:
            # exiftool -j outputs JSON
            import json
            arr = json.loads(res.stdout)
            return arr[0] if isinstance(arr, list) and arr else {}
    except FileNotFoundError:
        pass
    except Exception:
        pass

    # Fallback: use Pillow to extract basic EXIF
    try:
        img = Image.open(image_path)
        info = img._getexif()
        if not info:
            return {}
        data = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            data[decoded] = value
        return data
    except Exception:
        return {}
