import os
from logger.logger import log

def scan_directory(target_dir):
    if not os.path.exists(target_dir):
        log.error(f"Directory not found: {target_dir}")
        return []

    log.info(f"Scanning directory: {target_dir}")
    for root, _, files in os.walk(target_dir):
        for file in files:
            yield os.path.join(root, file)