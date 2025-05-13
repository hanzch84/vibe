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
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="원본 이미지", use_column_width=True)

    with col2:
        effect = st.selectbox("적용할 효과를 선택하세요", ["선택 없음", "흑백", "샤픈", "블러", "밝기 증가"])
        if effect == "흑백":
            image = image.convert("L")
        elif effect == "샤픈":
            image = image.filter(ImageFilter.SHARPEN)
        elif effect == "블러":
            image = image.filter(ImageFilter.BLUR)
        elif effect == "밝기 증가":
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(1.5)

        st.image(image, caption="효과 적용 결과", use_column_width=True)

# 갤러리 슬라이더
st.subheader("🖼️ 자동 갤러리 슬라이드")
gallery_images = [
    "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e",
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
    "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846"
]

slide_speed = st.slider("슬라이드 속도 (초)", 1, 5, 2)

for i, img_url in enumerate(gallery_images):
    st.image(img_url, caption=f"갤러리 이미지 {i+1}", use_column_width=True)
    time.sleep(slide_speed)

st.success("🔥 이제 당신만의 화려한 앱을 만들어 보세요!")
