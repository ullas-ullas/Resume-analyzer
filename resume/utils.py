import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

import re

def clean_text(text):

    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()

    return text.strip()

def normalize_text(text):
    replacements = {
        "node.js": "nodejs",
        "react.js": "react",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text