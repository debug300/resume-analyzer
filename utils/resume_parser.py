import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return clean_text(text)


def clean_resume_for_ats(text):
    ignore_keywords = [
        "interests", "hobbies", "languages", "objective"
    ]

    lines = text.lower().split("\n")
    filtered = [
        line for line in lines
        if not any(word in line for word in ignore_keywords)
    ]

    return " ".join(filtered)

