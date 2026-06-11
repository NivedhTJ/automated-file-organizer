import os
import shutil
from logger.logger import log

def move_file(filepath, base_dir, category):
    
    target_folder = os.path.join(base_dir, category)
    os.makedirs(target_folder, exist_ok=True)
    
    filename = os.path.basename(filepath)
    target_path = os.path.join(target_folder, filename)

    counter = 1
    while os.path.exists(target_path):
        name, ext = os.path.splitext(filename)
        target_path = os.path.join(target_folder, f"{name}_{counter}{ext}")
        counter += 1
        
    try:
        shutil.move(filepath, target_path)
        log.info(f"Moved: {filename} -> {category}/")
        return target_path
    except Exception as e:
        log.error(f"Failed to move {filename}: {e}")
        return filepath