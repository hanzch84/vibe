import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", layout="centered")

# 🔡 애니메이션 타이틀
components.html("""
<div style="text-align: center; margin-top: 30px;">
  <h1 id="title" style="font-family: 'Arial', sans-serif; font-size: 44px; color: #6c63ff;"></h1>
</div>
<script>
const text = "💡 MBTI 기반 진로 추천기 💡";
let idx = 0;
function typeEffect() {
  if (idx < text.length) {
    document.getElementById("title").innerHTML += text.charAt(idx);
    idx++;
    setTimeout(typeEffect, 60);
  }
}
typeEffect();
</script>
""", height=100)

st.markdown("---")

# 🎯 직업 설명 데이터
job_details = {
    "데이터 사이언티스트": "데이터를 기반으로 인사이트를 도출하고 예측 모델을 설계하는 전문가입니다.",
    "연구개발자": "신기술과 신제품을 연구하고 개발하는 역할로, 창의성과 분석력이 요구됩니다.",
    "시스템 설계자": "IT 시스템의 전체 구조를 설계하고 아키텍처를 설계하는 역할입니다.",
    "AI 연구원": "인공지능 모델을 연구하고 다양한 문제를 해결하는 혁신적인 직군입니다.",
    "개발자": "코드를 통해 기능을 구현하고 제품을 만드는 핵심 기술 인력입니다.",
    "이론 물리학자": "자연 현상을 수학적으로 설명하는 물리학을 연구하는 과학자입니다.",
    "CEO": "기업의 최고 경영자로, 전반적인 전략과 조직 운영을 책임집니다.",
    "전략 컨설턴트": "기업 문제를 분석하고 해결 전략을 제시하는 전문가입니다.",
    "정책 분석가": "사회, 경제, 복지 등 공공 정책을 분석하고 평가하는 일을 합니다.",
    "작가": "자신의 생각과 이야기를 글로 표현하여 세상과 소통합니다.",
    "교사": "학생에게 지식과 가치를 전달하고 성장을 돕는 교육자입니다.",
    "사회복지사": "도움이 필요한 사람들의 삶을 지원하고 개선하는 전문가입니다.",
    "간호사": "환자의 건강을 돌보고 의료진과 함께 치료를 지원하는 의료 전문가입니다.",
    "디자이너": "시각, 제품, 공간 등의 창의적인 디자인 작업을 수행합니다.",
    "연기자": "다양한 캐릭터를 표현하며 감정을 전달하는 공연 예술인입니다.",
    # 필요시 더 추가 가능
}

# 📘 MBTI 유형 및 진로 추천 데이터
mbti_careers = {
    "INTJ": ("전략기획가", ["데이터 사이언티스트", "연구개발자", "시스템 설계자"]),
    "INTP": ("혁신적 사색가", ["AI 연구원", "개발자", "이론 물리학자"]),
    "ENTJ": ("대담한 리더", ["CEO", "전략 컨설턴트", "정책 분석가"]),
    "INFP": ("열정적 중재자", ["작가", "교사", "사회복지사"]),
    "ISFJ": ("헌신적인 보호자", ["간호사", "교사", "행정직"]),
    "ISFP": ("감성적인 장인", ["디자이너", "사진작가", "미술가"]),
    "ESFP": ("에너지 넘치는 연예인", ["연기자", "이벤트 기획자", "여행 가이드"]),
    # 필요시 더 추가 가능
}

# ✅ MBTI 선택
selected = st.selectbox("당신의 MBTI를 선택하세요", [""] + sorted(mbti_careers.keys()))

# 추천 결과 영역
if selected:
    st.balloons()  # 🎈 화려한 효과
    title, careers = mbti_careers[selected]

    st.markdown("""
    <style>
    @keyframes fadeInZoom {
      0% {opacity: 0; transform: scale(0.8);}
      100% {opacity: 1; transform: scale(1);}
    }
    .recommend-box {
      background-color: #f0f8ff;
      padding: 25px;
      border-radius: 15px;
      border-left: 6px solid #6c63ff;
      animation: fadeInZoom 0.8s ease-in-out;
    }
    .recommend-title {
      color: #4b0082;
      font-size: 24px;
      margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""<div class="recommend-box">
    <div class="recommend-title">🧬 {selected} - {title}</div>
    <div>추천 진로:</div>
    </div>""", unsafe_allow_html=True)

    # ✨ 직업 버튼 클릭 시 상세 설명
    for job in careers:
        if st.button(f"👉 {job} 클릭해서 설명 보기", key=job):
            st.markdown(f"""
            <div style="background-color: #fff8dc; padding: 15px; margin-top: 10px; border-radius: 10px;
                        border-left: 5px solid orange; animation: fadeInZoom 0.6s ease-in-out;">
              <strong>{job}</strong><br>
              <p style="margin-top:5px; font-size: 16px;">{job_details.get(job, "상세 설명이 준비되지 않았습니다.")}</p>
            </div>
            """, unsafe_allow_html=True)
