# -----------------------------------------------------------------------------
# 5. PAGE 1: Home — 세포 한눈에 보기
# -----------------------------------------------------------------------------
if st.session_state["current_page"] == "Home":
    st.title("🔬 동물세포 한눈에 보기")
    st.write("아래 세포 내부에 위치한 **세포소기관 버튼**을 클릭하면 해당 소기관의 상세 정보로 이동합니다.")

    # 세포 영역을 표현하는 컨테이너
    with st.container():
        st.markdown("""
        <div style="
            background: radial-gradient(circle, #e8f5e9 0%, #c8e6c9 100%);
            border: 4px solid #4CAF50;
            border-radius: 30px;
            padding: 20px;
            text-align: center;
            margin-bottom: 20px;
        ">
            <h4 style="color: #2e7d32; margin: 0;">🛡️ 세포막 (Cell Membrane) / 🌊 세포질 (Cytosol)</h4>
            <p style="color: #666; font-size: 13px;">세포 내부의 소기관을 선택해 탐구를 시작해보세요.</p>
        </div>
        """, unsafe_allow_html=True)

    # 세포 내 소기관 격자(Grid) 배치 및 클릭 버튼
    st.subheader("📍 세포소기관 선택")
    
    # 3x3 구역으로 세포 내부 표현
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🧠 핵\n(DNA 저장 / 유전자 조절)", key="btn_nucle", use_container_width=True):
            st.session_state["selected_organelle"] = "핵"
            st.session_state["current_page"] = "Explorer"
            st.rerun()
            
        if st.button("📦 소포체\n(단백질 및 지질 수송)", key="btn_er", use_container_width=True):
            st.session_state["selected_organelle"] = "소포체"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

        if st.button("⚙️ 리보솜\n(단백질 합성 공장)", key="btn_ribo", use_container_width=True):
            st.session_state["selected_organelle"] = "리보솜"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

    with col2:
        if st.button("⚡ 미토콘드리아\n(세포 호흡 & ATP 생성)", key="btn_mito", use_container_width=True):
            st.session_state["selected_organelle"] = "미토콘드리아"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

        if st.button("📮 골지체\n(단백질 가공 및 분비)", key="btn_golgi", use_container_width=True):
            st.session_state["selected_organelle"] = "골지체"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

        if st.button("♻️ 리소좀\n(세포 내 물질 분해)", key="btn_lyso", use_container_width=True):
            st.session_state["selected_organelle"] = "리소좀"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

    with col3:
        if st.button("🛡️ 세포막\n(선택적 투과성 & 출입 조절)", key="btn_mem", use_container_width=True):
            st.session_state["selected_organelle"] = "세포막"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

        if st.button("🌊 세포질\n(대사 과정 진행 공간)", key="btn_cyto", use_container_width=True):
            st.session_state["selected_organelle"] = "세포질"
            st.session_state["current_page"] = "Explorer"
            st.rerun()

        if st.button("🏗️ 세포골격\n(형태 유지 & 물질 이동)", key="btn_skel", use_container_width=True):
            st.session_state["selected_organelle"] = "세포골격"
            st.session_state["current_page"] = "Explorer"
            st.rerun()
