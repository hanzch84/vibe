import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
from PIL import Image, ImageEnhance, ImageFilter
import time

# 페이지 설정
st.set_page_config(
    page_title="🔥 화려한 Streamlit 앱 🔥",
    page_icon="🌈",
    layout="wide"
)

# 배경 스타일 커스텀
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .css-1v0mbdj.edgvbvh3 {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀과 인사
st.title("🌟 나의 N번째 Streamlit App 🌟")
st.header("✨ Nice to see you!!! ✨")

# Lottie 애니메이션 로딩 함수
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie 애니메이션
lottie_url = "https://assets9.lottiefiles.com/packages/lf20_touohxv0.json"
lottie_json = load_lottie_url(lottie_url)
st_lottie(lottie_json, height=250, key="hello")

# 인터랙티브 섹션
st.subheader("🎨 이미지 효과 체험")
uploaded_file = st.file_u
