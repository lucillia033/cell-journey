import streamlit as st

st.set_page_config(
    page_title="Cell Explorer",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Cell Explorer")
st.subheader("세포소기관 탐험")

st.write(
    "세포 전체의 구조를 살펴보고, "
    "각 세포소기관의 역할을 탐구하는 웹앱입니다."
)

st.divider()

st.info(
    "왼쪽 메뉴에서 세포소기관 탐구 페이지를 선택해 주세요."
)

st.markdown("### 🧫 이 웹앱에서 알아볼 소기관")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("🔵 핵")
    st.write("유전정보를 저장하고 유전자 발현을 조절합니다.")

with col2:
    st.write("🟠 미토콘드리아")
    st.write("세포 호흡과 ATP 생성에 관여합니다.")

with col3:
    st.write("🟢 리보솜")
    st.write("단백질을 합성합니다.")
