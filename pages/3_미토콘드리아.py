import streamlit as st

st.set_page_config(page_title="미토콘드리아 탐구", page_icon="⚡", layout="wide")

st.title("⚡ 미토콘드리아 (Mitochondria)")
st.caption("📍 위치: 세포질 전반에 분포 (에너지 소비가 많은 세포에 다수 존재)")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포 호흡을 통해 유기물(포도당)을 분해하고, 세포가 사용하는 에너지원인 ATP를 생성하는 발전소입니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("자체 DNA와 리보솜을 가지고 있어 스스로 복제하고 단백질을 합성할 수 있습니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["외막 & 내막", "크리스타 (Cristae)", "기질 (Matrix)"])
    
    if struct == "외막 & 내막":
        st.success("이중막 구조로, 내막은 안쪽으로 주름진 구조를 형성합니다.")
    elif struct == "크리스타 (Cristae)":
        st.success("내막이 접혀 만든 구조로, 표면적을 넓혀 ATP 합성 효소가 효율적으로 작동하게 합니다.")
    elif struct == "기질 (Matrix)":
        st.success("내막 안쪽의 액체 공간으로, 세포 호흡 관련 효소와 자체 DNA가 존재합니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
