import pikepdf
from logger.logger import log

def clean_pdf_metadata(filepath):
    try:
        with pikepdf.Pdf.open(filepath, allow_overwriting_input=True) as pdf:
            if pdf.docinfo:
                for key in list(pdf.docinfo.keys()):
                    del pdf.docinfo[key]
            pdf.save(filepath)
        log.info(f"Stripped metadata from PDF: {filepath}")
    except Exception as e:
        log.error(f"Could not strip metadata from {filepath}: {e}")