import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """PDF 파일에서 텍스트 추출"""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_risk_keywords(path='03_risk_keywords.txt'):
    """키워드 리스트 로드"""
    keywords = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line:
                word, level = line.strip().split(',')
                keywords.append((word.strip(), level.strip()))
    return keywords

def analyze_risk(text, keywords):
    """텍스트 내 키워드 탐지"""
    found = []
    for word, level in keywords:
        if word in text:
            found.append((word, level))
    return found