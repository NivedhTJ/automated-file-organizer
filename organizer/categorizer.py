import os

CATEGORY_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov']
}

def get_category(filepath):
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return 'Others'