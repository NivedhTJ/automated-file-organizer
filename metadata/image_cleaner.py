from PIL import Image
from logger.logger import log

def clean_image_metadata(filepath):
    try:
        image = Image.open(filepath)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save(filepath)
        log.info(f"Stripped metadata from image: {filepath}")
    except Exception as e:
        log.error(f"Could not strip metadata from {filepath}: {e}")