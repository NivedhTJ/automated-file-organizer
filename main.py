import argparse
import os
from logger.logger import log
from organizer.scanner import scan_directory
from organizer.categorizer import get_category
from organizer.mover import move_file
from dedupe.duplicate_finder import find_and_remove_duplicates
from metadata.image_cleaner import clean_image_metadata
from metadata.pdf_cleaner import clean_pdf_metadata
from metadata.docx_cleaner import clean_docx_metadata

def process_metadata(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext in ['.jpg', '.jpeg', '.png']:
        clean_image_metadata(filepath)
    elif ext == '.pdf':
        clean_pdf_metadata(filepath)
    elif ext == '.docx':
        clean_docx_metadata(filepath)

def main():
    parser = argparse.ArgumentParser(description="FILE-SHRED: Automated System Organizer & Metadata Stripper")
    parser.add_argument("target_dir", help="The directory to organize and shred")
    parser.add_argument("--no-dedupe", action="store_true", help="Skip duplicate removal")
    parser.add_argument("--no-shred", action="store_true", help="Skip metadata stripping")
    
    args = parser.parse_args()
    target_dir = args.target_dir
    
    log.info("Starting FILE ORGANIZER process...")
    
    all_files = list(scan_directory(target_dir))
    
    if not args.no_dedupe:
        files_to_process = find_and_remove_duplicates(all_files)
    else:
        files_to_process = all_files
        
    log.info("Organizing and shredding metadata...")
    for filepath in files_to_process:
        if not os.path.exists(filepath):
            continue 
        if not args.no_shred:
            process_metadata(filepath)
            
        category = get_category(filepath)
        move_file(filepath, target_dir, category)
        
    log.info("FILE-ORGANIZING operations completed successfully.")

if __name__ == "__main__":
    main()