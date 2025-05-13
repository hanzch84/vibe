import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", layout="centered")

# 💡 타이틀 애니메이션
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

# 📘 스타일: 다크/라이트 모드 자동 대응
st.markdown("""
<style>
.recommend-box, .detail-card {
    padding: 25px;
    border-radius: 15px;
    margin-top: 10px;
    animation: fadeInZoom 0.6s ease-in-out;
    border-left: 6px solid var(--accent-color);
}
@keyframes fadeInZoom {
  0% {opacity: 0; transform: scale(0.95);}
  100% {opacity: 1; transform: scale(1);}
}
button[kind="primary"] {
    padding: 8px 14px;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    transition: 0.3s;
    margin-bottom: 5px;
    cursor: pointer;
}
button[kind="primary"]:hover {
    filter: brightness(1.1);
}
@media (prefers-color-scheme: dark) {
  .recommend-box {
      background-color: #1e1f22;
      color: #eaeaea;
      border-left-color: #6c63ff;
      box-shadow: 0 0 10px rgba(108, 99, 255, 0.2);
  }
  .detail-card {
      background-color: #2a2a2d;
      color: #f5f5f5;
      border-left-color: #ffaa33;
  }
  button[kind="primary"] {
      background-color: #3a3a3d;
      color: white;
  }
}
@media (prefers-color-scheme: light) {
  .recommend-box {
      background-color: #f0f8ff;
      color: #202020;
      border-left-color: #6c63ff;
      box-shadow: 0 0 10px rgba(108, 99, 255, 0.2);
  }
  .detail-card {
      background-color: #fffbe6;
      color: #303030;
      border-left-color: #ffaa33;
  }
  button[kind="primary"] {
      background-color: #eeeeee;
      color: black;
  }
}
</style>
""", unsafe_allow_html=True)

# 📘 전문 직업 정보
job_details = {
    "연기자": {
        "요약": "다양한 캐릭터를 표현하며 감정을 전달하는 공연 예술인입니다.",
        "학위/전공": "연극영화학, 뮤지컬학, 방송연예학 등 (전문대졸 이상 권장)",
        "요구 능력": "표현력, 감정 조절, 무대/카메라 감각, 창의성, 협업 능력",
        "준비 방법": "청소년기부터 연극반/뮤지컬 활동 참여, 말하기 훈련, 감정 표현 연습",
        "추천 활동": "문화센터 연기과정 수강, 예술대학 준비, 오디션 참여, 포트폴리오 제작",
        "참고 링크": "https://www.career.go.kr/cnet/front/base/job/jobView.do?SEQ=289"
    },
    "이벤트 기획자": {
        "요약": "공연, 축제, 박람회 등의 행사를 기획하고 실행하는 직업입니다.",
        "학위/전공": "관광학, 홍보·광고학, 커뮤니케이션 등",
        "요구 능력": "기획력, 커뮤니케이션, 일정 관리, 예산 운영, 창의성",
        "준비 방법": "행사 도우미 활동, 지역 축제 스태프, 기획서 작성 경험 쌓기",
        "추천 활동": "동아리 행사 기획, 공모전 참여, 현장 실습 인턴",
        "참고 링크": "https://www.career.go.kr/cnet/front/base/job/jobView.do?SEQ=415"
    },
    "여행 가이드": {
        "요약": "국내외 여행지에서 관광객을 안내하며 정보를 전달하는 직업입니다.",
        "학위/전공": "관광학, 국제학, 외국어 관련 전공",
        "요구 능력": "언어 능력, 친화력, 여행 지식, 설명 능력, 체력",
        "준비 방법": "외국어 학습, 국내 여행 다니며 지식 습득, 관광통역안내사 자격증 준비",
        "추천 활동": "가이드 체험 프로그램 참여, 현장 실습, 여행 블로그 운영",
        "참고 링크": "https://www.career.go.kr/cnet/front/base/job/jobView.do?SEQ=487"
    }
}

# MBTI 추천 직업 매핑
mbti_careers = {
    "ESFP": ("에너지 넘치는 연예인", ["연기자", "이벤트 기획자", "여행 가이드"]),
    # 필요한 다른 MBTI 유형도 이 구조로 추가 가능
}

# ✅ 사용자 선택
selected = st.selectbox("당신의 MBTI를 선택하세요", [""] + list(mbti_careers.keys()))

if selected:
    st.balloons()
    title, jobs = mbti_careers[selected]

    st.markdown(f"""
    <div class="recommend-box">
        <div class="recommend-title">🎯 {selected} - {title}</div>
        <div>추천 진로:</div>
    </div>
    """, unsafe_allow_html=True)

    for job in jobs:
        if st.button(f"👉 {job} 클릭해서 설명 보기", key=job):
            info = job_details.get(job)
            if info:
                st.markdown(f"""
                <div class="detail-card">
                    <h4 style='margin-bottom:10px;'>{job}</h4>
                    <p><strong>✅ 요약:</strong> {info["요약"]}</p>
                    <p><strong>🎓 관련 학위/전공:</strong> {info["학위/전공"]}</p>
                    <p><strong>🛠 요구 능력:</strong> {info["요구 능력"]}</p>
                    <p><strong>📚 준비 방법:</strong> {info["준비 방법"]}</p>
                    <p><strong>🧑‍🏫 추천 활동:</strong> {info["추천 활동"]}</p>
                    <p><strong>🌐 참고 링크:</strong> <a href="{info["참고 링크"]}" target="_blank">직업정보 더 보기</a></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("상세 정보가 아직 준비되지 않았습니다.")
