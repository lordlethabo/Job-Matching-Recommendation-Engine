from pdfminer.high_level import extract_text

def extract_text_from_resume(path):
    try:
        return extract_text(path)
    except:
        return ""

