import streamlit as st
import os

# 세션 상태 관리
if "preview_target" not in st.session_state:
    st.session_state["preview_target"] = "핵"

ORGANELLES = {
    "핵": {"icon": "🧠", "desc": "세포의 생명 활동을 조절하는 중심 기관으로, 유전 정보(DNA)를 보관합니다.", "path": "pages/1_핵.py"},
    "리보솜": {"icon": "⚙️", "desc": "mRNA의 유전 정보를 바탕으로 단백질을 합성하는 공장입니다.", "path": "pages/2_리보솜.py"},
    "미토콘드리아": {"icon": "⚡", "desc": "세포 호흡을 통해 유기물을 분해하고 ATP(에너지)를 생성합니다.", "path": "pages/3_미토콘드리아.py"},
    "소포체": {"icon": "📦", "desc": "단백질과 지질을 합성하고 세포 내 이동 통로 역할을 합니다.", "path": "pages/4_소포체.py"},
    "골지체": {"icon": "📮", "desc": "소포체에서 온 단백질을 가공·분류하여 세포 안팎으로 분비합니다.", "path": "pages/5_골지체.py"},
    "리소좀": {"icon": "♻️", "desc": "가수분해 효소를 이용해 손상된 소기관이나 노폐물을 분해합니다.", "path": "pages/6_리소좀.py"},
    "세포막": {"icon": "🛡️", "desc": "세포 외부와의 경계로, 물질의 출입을 선택적으로 조절합니다.", "path": "pages/7_세포막.py"},
    "세포질": {"icon": "🌊", "desc": "세포 내부를 채우는 액체 환경으로 여러 대사 과정이 일어납니다.", "path": "pages/8_세포질.py"},
    "세포골격": {"icon": "🏗️", "desc": "세포의 형태를 유지하고 내부 물질의 이동 길을 제공합니다.", "path": "pages/9_세포골격.py"}
}

# CSS 스타일
st.markdown("""
    <style>
    .badge {
        display: inline-block;
        background-color: #0083B0;
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔬 동물세포 한눈에 보기")
st.write("소기관 버튼을 누르면 하단에 **간단 설명 카드**가 표출되며, **이동 버튼**이나 **좌측 사이드바**를 통해 해당 전용 페이지로 완전히 이동할 수 있습니다.")

col_left, col_right = st.columns([1.2, 1])

# 좌측: 세포 이미지
with col_left:
    st.markdown("### 🖼️ 동물세포 전체 구조")
    img_file = "cell_image.png"
    if os.path.exists(img_file):
        st.image(img_file, caption="동물세포의 구조 및 소기관 위치", use_container_width=True)
    else:
        st.info("💡 **이미지 등록 안내**\n\n깃허브 메인 위치에 `cell_image.png` 파일로 세포 구조도 이미지를 업로드해 주세요.")

# 우측: 3x3 소기관 버튼
with col_right:
    st.markdown("### 🎯 소기관 선택하기")
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        
        with c1:
            if st.button("🧠 핵", use_container_width=True): st.session_state["preview_target"] = "핵"
            if st.button("📦 소포체", use_container_width=True): st.session_state["preview_target"] = "소포체"
            if st.button("⚙️ 리보솜", use_container_width=True): st.session_state["preview_target"] = "리보솜"
            
        with c2:
            if st.button("⚡ 미토콘드리아", use_container_width=True): st.session_state["preview_target"] = "미토콘드리아"
            if st.button("📮 골지체", use_container_width=True): st.session_state["preview_target"] = "골지체"
            if st.button("♻️ 리소좀", use_container_width=True): st.session_state["preview_target"] = "리소좀"
            
        with c3:
            if st.button("🛡️ 세포막", use_container_width=True): st.session_state["preview_target"] = "세포막"
            if st.button("🌊 세포질", use_container_width=True): st.session_state["preview_target"] = "세포질"
            if st.button("🏗️ 세포골격", use_container_width=True): st.session_state["preview_target"] = "세포골격"

# 하단 요약 카드 및 페이지 전환
st.markdown("---")
target = st.session_state["preview_target"]
info = ORGANELLES[target]

with st.container(border=True):
    st.markdown('<span class="badge">SELECTED ORGANELLE</span>', unsafe_allow_html=True)
    st.subheader(f"{info['icon']} {target} 요약")
    st.info(info["desc"])
    
    target_path = info["path"]
    if os.path.exists(target_path):
        if st.button(f"🔍 {target} 단독 페이지로 이동하기 ➔", type="primary", use_container_width=True):
            st.switch_page(target_path)
    else:
        st.warning(f"⚠️ `{target}` 상세 파일(`{target_path}`)이 GitHub에 아직 존재하지 않습니다.")
