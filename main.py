import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="동적 타이틀 데모", layout="centered")

# CSS + JS를 이용한 타이핑 애니메이션
html_code = """
<div style="text-align: center; margin-top: 50px;">
  <h1 id="title" style="font-family: 'Arial', sans-serif; font-size: 48px; color: #ff4b4b;"></h1>
</div>
<script>
const text = "🔥 나의 N번째 Streamlit App 🔥";
let idx = 0;
function typeEffect() {
  if (idx < text.length) {
    document.getElementById("title").innerHTML += text.charAt(idx);
    idx++;
    setTimeout(typeEffect, 100);
  }
}
typeEffect();
</script>
"""

# HTML 삽입
components.html(html_code, height=150)
