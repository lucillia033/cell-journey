import streamlit as st
import os

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 Custom CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="동물세포 탐험대 — 메인",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
    <style>
    .tag {
        display: inline-block;
        background-color: #e8f4f8;
        color: #1e88e5;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: 600;
        font-size: 13px;
        margin-right: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. 메인 세션 상태 관리
# -----------------------------------------------------------------------------
if "selected_preview" not in st.session_state:
    st.session_state["selected_preview"] = "핵"

# 소기관 데이터베이스 (요약용)
ORGANELLES_SUMMARY = {
    "핵": {"icon": "🧠", "desc": "세포의 생명 활동을 조절하는 중심 기관으로, 유전 정보(DNA)를 보관합니다.", "file": "pages/1_핵.py"},
    "리보솜": {"icon": "⚙️", "desc": "mRNA의 유전 정보를 바탕으로 단백질을 합성하는 공장입니다.", "file": "pages/2_리보솜.py"},
    "미토콘드리아": {"icon": "⚡", "desc": "세포 호흡을 통해 유기물을 분해하고 ATP(에너지)를 생성합니다.", "file": "pages/3_미토콘드리아.py"},
    "소포체": {"icon": "📦", "desc": "단백질과 지질을 합성하고 운반하는 막상 구조입니다.", "file": "pages/4_소포체.py"},
    "골지체": {"icon": "📮", "desc": "소포체에서 전달받은 물질을 가공·분류하여 세포 안밖으로 분비합니다.", "file": "pages/5_골지체.py"},
    "리소좀": {"icon": "♻️", "desc": "가수분해 효소를 포함하여 세포 내 물질 및 노폐물을 분해합니다.", "file": "pages/6_리소좀.py"},
    "세포막": {"icon": "🛡️", "desc": "세포의 경계로, 물질 출입을 선택적으로 조절하여 항상성을 유지합니다.", "file": "pages/7_세포막.py"},
    "세포질": {"icon": "🌊", "desc": "세포 내부를 채우는 액체 환경으로, 여러 대사 과정이 일어납니다.", "file": "pages/8_세포질.py"},
    "세포골격": {"icon": "🏗️", "desc": "세포 형태를 유지하고 내부 물질 이동을 돕는 단백질 섬유입니다.", "file": "pages/9_세포골격.py"}
}

# -----------------------------------------------------------------------------
# 3. 메인 레이아웃 (이미지 + 버튼 그리드)
# -----------------------------------------------------------------------------
st.title("🔬 동물세포 한눈에 보기")
st.write("소기관 버튼을 누르면 하단에 **간단 설명**이 표시되며, **'페이지 이동'** 버튼으로 개별 페이지에 접근할 수 있습니다.")

col_img, col_btns = st.columns([1.2, 1])

# 좌측: 세포 전체 이미지 영역
with col_img:
    st.markdown("### 🖼️ 동물세포 구조도")
    image_path = "cell_image.png"  # 불러올 이미지 파일명
    
    if os.path.exists(image_path):
        st.image(image_path, caption="동물세포의 구조 및 소기관 배치", use_column_width=True)
    else:
        st.info("💡 **이미지 등록 안내**\n\n프로젝트 폴더에 `cell_image.png` 이름으로 세포 이미지 파일을 넣으면 이곳에 띄워집니다.")

# 우측: 3x3 소기관 선택 버튼 영역
with col_btns:
    st.markdown("### 🎯 소기관 선택")
    with st.container(border=True):
        b_col1, b_col2, b_col3 = st.columns(3)
        
        with b_col1:
            if st.button("🧠 핵", use_container_width=True): st.session_state["selected_preview"] = "핵"
            if st.button("📦 소포체", use_container_width=True): st.session_state["selected_preview"] = "소포체"
            if st.button("⚙️ 리보솜", use_container_width=True): st.session_state["selected_preview"] = "리보솜"
            
        with b_col2:
            if st.button("⚡ 미토콘드리아", use_container_width=True): st.session_state["selected_preview"] = "미토콘드리아"
            if st.button("📮 골지체", use_container_width=True): st.session_state["selected_preview"] = "골지체"
            if st.button("♻️ 리소좀", use_container_width=True): st.session_state["selected_preview"] = "리소좀"
            
        with b_col3:
            if st.button("🛡️ 세포막", use_container_width=True): st.session_state["selected_preview"] = "세포막"
            if st.button("🌊 세포질", use_container_width=True): st.session_state["selected_preview"] = "세포질"
            if st.button("🏗️ 세포골격", use_container_width=True): st.session_state["selected_preview"] = "세포골격"

# -----------------------------------------------------------------------------
# 4. 하단 미리보기 카드 및 페이지 이동 처리
# -----------------------------------------------------------------------------
st.markdown("---")
selected = st.session_state["selected_preview"]
data = ORGANELLES_SUMMARY[selected]

with st.container(border=True):
    st.subheader(f"{data['icon']} {selected} 요약")
    st.info(data["desc"])
    
    # 해당 개별 페이지로 이동하는 링크 버튼
    st.page_link(data["file"], label=f"🔍 {selected} 상세 페이지로 이동하기 ➔", icon=data["icon"])
