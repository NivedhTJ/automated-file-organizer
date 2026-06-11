import docx
from logger.logger import log

def clean_docx_metadata(filepath):
    try:
        doc = docx.Document(filepath)
        prop = doc.core_properties
        prop.author = ""
        prop.comments = ""
        prop.last_modified_by = ""
        prop.subject = ""
        prop.title = ""
        doc.save(filepath)
        log.info(f"Stripped metadata from DOCX: {filepath}")
    except Exception as e:
        log.error(f"Could not strip metadata from {filepath}: {e}")