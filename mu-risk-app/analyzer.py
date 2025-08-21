import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """PDF 파일에서 텍스트 추출"""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

import os

def load_risk_keywords(path="risk_keywords.txt"):
    base_path = os.path.dirname(__file__)   # analyzer.py 파일이 있는 폴더 기준
    file_path = os.path.join(base_path, path)
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip().split(",") for line in f if line.strip()]

def analyze_risk(text, keywords):
    """텍스트 내 키워드 탐지"""
    found = []
    for word, level in keywords:
        if word in text:
            found.append((word, level))
    return found
