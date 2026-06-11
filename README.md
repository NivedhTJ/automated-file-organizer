# SysClean 

**SysClean** is a powerful Command-Line Interface (CLI) tool designed to automatically clean up cluttered directories while protecting your privacy. It scans a target folder, categorizes files by type into neat subfolders, removes exact duplicates, and strips hidden metadata from your files before you share them.

## Features

* **Smart Organization:** Automatically sorts files into categorized subfolders (`Images/`, `Documents/`, `Video/`, etc.) based on their extensions.
* **Privacy Protection (Shredding):** Strips identifiable hidden metadata from files:
  * **Images:** Removes EXIF data (GPS coordinates, camera models, dates).
  * **PDFs:** Clears author details, creation dates, and software tags.
  * **Word Docs (.docx):** Wipes core properties like author names and editing history.
* **Deduplication:** Uses SHA-256 hashing to find and delete exact duplicate files, even if they have different file names.
* **Collision Safe:** Intelligently renames files if a file with the same name already exists in the destination folder, preventing accidental overwrites.

## 🛠️ Prerequisites

* Python 3.8 or higher
* Pillow
* pikepdf
* python-docx

Note: SysClean is a fun personal project built for learning and experimentation. Always back up important files before running it, and use it at your own risk.