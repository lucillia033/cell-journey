import streamlit as st

st.set_page_config(page_title="리보솜 탐구", page_icon="⚙️", layout="wide")

st.title("⚙️ 리보솜 (Ribosome)")
st.caption("📍 위치: 세포질에 떠 있거나 거친소포체 표면에 부착")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 주요 기능")
    st.info("mRNA의 유전 정보를 읽어 아미노산을 연결함으로써 단백질을 합성하는 세포 내 단백질 제조 공장입니다.")
    
    st.subheader("🔗 연계 소기관")
    st.write("핵에서 전달된 mRNA 정보를 바탕으로 단백질을 만들며, 표면에 부착된 소포체로 단백질을 보냅니다.")

with col2:
    st.subheader("🧩 세부 구조 탐구")
    struct = st.radio("구조를 선택하세요", ["대단위체 (Large subunit)", "소단위체 (Small subunit)"])
    
    if struct == "대단위체 (Large subunit)":
        st.success("아미노산 사이의 펩타이드 결합을 촉매하는 공간을 제공합니다.")
    elif struct == "소단위체 (Small subunit)":
        st.success("mRNA 결합 부위를 가지고 있어 유전 정보를 정확하게 해독합니다.")

st.markdown("---")
if st.button("🏠 메인 화면으로 돌아가기", type="primary", use_container_width=True):
    st.switch_page("pages/0_메인.py")
