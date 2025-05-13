import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", layout="centered")

# 🔡 타이틀 애니메이션
html_code = """
<div style="text-align: center; margin-top: 50px;">
  <h1 id="title" style="font-family: 'Arial', sans-serif; font-size: 48px; color: #6c63ff;"></h1>
</div>
<script>
const text = "💡 MBTI 기반 진로 추천기 💡";
let idx = 0;
function typeEffect() {
  if (idx < text.length) {
    document.getElementById("title").innerHTML += text.charAt(idx);
    idx++;
    setTimeout(typeEffect, 80);
  }
}
typeEffect();
</script>
"""
components.html(html_code, height=120)

st.markdown("---")

# 📊 MBTI 추천 데이터
mbti_careers = {
    "INTJ": ("전략기획가", "데이터 사이언티스트, 연구개발자, 시스템 설계자"),
    "INTP": ("혁신적 사색가", "AI 연구원, 개발자, 이론 물리학자"),
    "ENTJ": ("대담한 리더", "CEO, 전략 컨설턴트, 정책 분석가"),
    "ENTP": ("아이디어 뱅크", "기획자, 창업가, 마케팅 디렉터"),
    "INFJ": ("통찰력 있는 조언자", "상담가, 심리학자, 작가"),
    "INFP": ("열정적 중재자", "작가, 교사, 사회복지사"),
    "ENFJ": ("카리스마 리더", "교사, HR 매니저, 정치가"),
    "ENFP": ("자유로운 영혼", "광고기획자, 유튜버, 창작자"),
    "ISTJ": ("책임감 있는 관리자", "공무원, 회계사, 법률 관련 직업"),
    "ISFJ": ("헌신적인 보호자", "간호사, 교사, 행정직"),
    "ESTJ": ("체계적인 리더", "경영자, 프로젝트 매니저, 군 간부"),
    "ESFJ": ("사교적인 돌보미", "상담교사, 의료 행정, 복지 분야"),
    "ISTP": ("실용적인 해결사", "엔지니어, 파일럿, 응급구조사"),
    "ISFP": ("감성적인 장인", "디자이너, 사진작가, 미술가"),
    "ESTP": ("모험적인 실행가", "세일즈, 스포츠 선수, 사업가"),
    "ESFP": ("에너지 넘치는 연예인", "연기자, 이벤트 기획자, 여행 가이드")
}

# 🧠 MBTI 선택
mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", options=sorted(mbti_careers.keys()))

# 🎓 진로 추천 결과
if mbti_type:
    title, careers = mbti_careers[mbti_type]
    st.markdown(f"""
    <div style="background-color:#f0f8ff; padding: 20px; border-radius: 10px;">
        <h2 style="color: #4b0082;">🧬 {mbti_type} - {title}</h2>
        <p style="font-size: 18px;">추천 진로: <strong>{careers}</strong></p>
    </div>
    """, unsafe_allow_html=True)

