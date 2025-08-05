import streamlit as st
import os
from analyzer import extract_text_from_pdf, load_risk_keywords, analyze_risk

# 📁 업로드 폴더 없으면 생성
os.makedirs("uploaded", exist_ok=True)

st.set_page_config(page_title="등기부등본 위험 키워드 분석기", layout="centered")
st.title("📄 등기부등본 위험 키워드 분석기")
st.write("PDF를 업로드하면 위험 키워드를 분석합니다.")

uploaded_file = st.file_uploader("📤 등기부등본 PDF 업로드", type="pdf")

if uploaded_file is not None:
    file_path = os.path.join("uploaded", uploaded_file.name)

    # 파일 저장
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ 파일 업로드 완료: {uploaded_file.name}")

    # 텍스트 추출 및 분석
    text = extract_text_from_pdf(open(file_path, "rb"))
    keywords = load_risk_keywords("risk_keywords.txt")
    results = analyze_risk(text, keywords)

    st.subheader("🧾 분석 결과")
    if results:
        for word, level in results:
            if level == "매우위험":
                st.error(f"❗ '{word}' → {level}")
            elif level == "주의":
                st.warning(f"⚠️ '{word}' → {level}")
            else:
                st.info(f"ℹ️ '{word}' → {level}")
    else:
        st.success("🔍 위험 키워드가 발견되지 않았습니다.")