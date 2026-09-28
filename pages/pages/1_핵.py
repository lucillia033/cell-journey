import streamlit as st

st.set_page_config(page_title="핵 탐구", page_icon="🧠", layout="wide")

st.title("🧠 핵 (Nucleus)")
st.caption("📍 위치: 대부분의 진핵세포 중앙부에 위치")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("세포의 생명 활동을 총괄 조절하며, 유전 정보(DNA)를 보관하고 복제·전사하는 세포의 핵심 제어 센터입니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("핵막 표면은 소포체와 직접 연결되어 있으며, 리보솜에서 만들어진 단백질의 지시 정보를 제공합니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["핵막 (Nuclear Membrane)", "인 (Nucleolus)", "염색질 (Chromatin)"])
    
    if struct == "핵막 (Nuclear Membrane)":
        st.success("이중막 구조로 되어 있으며, 핵공(Nuclear pore)을 통해 물질의 출입을 조절합니다.")
    elif struct == "인 (Nucleolus)":
        st.success("핵 내부에서 가장 짙게 보이는 부분으로, 리보솜 RNA(rRNA)를 합성하고 리보솜을 조립합니다.")
    elif struct == "염색질 (Chromatin)":
        st.success("DNA와 히스톤 단백질이 결합된 형태이며, 세포 분열 시 염색체로 응축됩니다.")

st.markdown("---")

# 수정된 메인 페이지(pages/0_메인.py) 이동 구문
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
