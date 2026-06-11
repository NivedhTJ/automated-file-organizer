import hashlib
import os
from logger.logger import log

def hash_file(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        log.error(f"Error hashing {filepath}: {e}")
        return None

def find_and_remove_duplicates(file_paths):
    seen_hashes = set()
    unique_files = []
    
    log.info("Scanning for duplicates...")
    for filepath in file_paths:
        file_hash = hash_file(filepath)
        if not file_hash:
            continue
            
        if file_hash in seen_hashes:
            log.warning(f"Duplicate found and deleted: {filepath}")
            os.remove(filepath)
        else:
            seen_hashes.add(file_hash)
            unique_files.append(filepath)
            
    return unique_files