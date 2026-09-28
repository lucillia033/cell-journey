import streamlit as st

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 Custom CSS 적용
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="세포소기관 탐험대",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 레이아웃 스타일 개선용 CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .info-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        margin-bottom: 15px;
    }
    .tag {
        display: inline-block;
        background-color: #e8f4f8;
        color: #1e88e5;
        padding: 4px 12px;
        border-radius: 15px;
        font-weight: 600;
        font-size: 13px;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. 세션 상태(Session State) 선제 초기화 (NameError 및 상태 유실 방지)
# -----------------------------------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

if "selected_organelle" not in st.session_state:
    st.session_state["selected_organelle"] = "핵"

# -----------------------------------------------------------------------------
# 3. 세포소기관 데이터베이스 (고등학교 생명과학 과정 기준)
# -----------------------------------------------------------------------------
ORGANELLES_DATA = {
    "핵": {
        "icon": "🧠",
        "description": "세포의 생명 활동을 조절하는 중심 기관으로, 유전 정보(DNA)를 보관합니다.",
        "location": "세포의 중앙 부근",
        "relationship": "리보솜, 소포체, 골지체와 연계되어 단백질 합성의 시작점 역할을 함",
        "keywords": ["DNA 저장", "유전자 발현 조절", "전사 과정"],
        "structures": {
            "핵막": "2중막 구조로 내부의 DNA를 보호하고, 핵공을 통해 물질 이동을 조절합니다.",
            "핵공": "핵막에 존재하는 구멍으로, RNA나 단백질 등의 물질이 출입하는 통로입니다.",
            "염색질": "DNA와 히스톤 단백질이 결합된 형태이며, 세포 분열 시 염색체로 응축됩니다."
        }
    },
    "리보솜": {
        "icon": "⚙️",
        "description": "mRNA의 유전 정보를 바탕으로 아미노산을 연결하여 단백질을 합성하는 공장입니다.",
        "location": "세포질에 떠 있거나 거친면 소포체 표면에 부착됨",
        "relationship": "핵의 mRNA를 전달받아 단백질을 만든 뒤, 거친면 소포체로 전달함",
        "keywords": ["단백질 합성", "mRNA 번역", "아미노산 결합"],
        "structures": {
            "대단위체": "아미노산 간의 결합(펩타이드 결합)을 촉진하는 활성 부위를 가집니다.",
            "소단위체": "mRNA와 결합하여 유전 정보를 읽어들이는 역할을 합니다."
        }
    },
    "미토콘드리아": {
        "icon": "⚡",
        "description": "세포 호흡을 통해 유기물을 분해하고 ATP(세포 에너지)를 생성하는 발전소입니다.",
        "location": "세포질 전체 (에너지 소비가 많은 곳에 집중)",
        "relationship": "세포질에서의 당분해 작용 이후 산물을 받아 ATP를 대량 생산함",
        "keywords": ["ATP 생성", "세포 호흡", "에너지 공급"],
        "structures": {
            "외막": "미토콘드리아의 매끄러운 바깥쪽 막으로 형태를 유지합니다.",
            "내막": "안쪽으로 주름진 막으로 전자전달계 효소들이 배치되어 있습니다.",
            "크리스타": "내막이 안쪽으로 꺾여 들어간 주름 구조로, 표면적을 넓혀 ATP 합성 효율을 높입니다.",
            "기질": "내막 안쪽의 액체 공간으로, 세포 호흡 관련 효소와 독자적 DNA, 리보솜이 존재합니다."
        }
    },
    "소포체": {
        "icon": "📦",
        "description": "단백질과 지질을 합성하고, 세포 내 운반 통로 역할을 하는 막상 구조입니다.",
        "location": "핵막과 연결되어 세포질 넓은 범위에 분포",
        "relationship": "리보솜에서 합성된 단백질을 가공하여 수송 소포를 통해 골지체로 보냄",
        "keywords": ["단백질 가공", "지질 합성", "물질 이동 통로"],
        "structures": {
            "거친면 소포체": "표면에 리보솜이 붙어 있으며, 합성된 단백질을 수송 소포로 보냅니다.",
            "매끈면 소포체": "리보솜이 없으며, 지질 합성, 독성 물질 해독, 칼슘 이온 저장 등을 담당합니다."
        }
    },
    "골지체": {
        "icon": "📮",
        "description": "소포체로부터 전달받은 단백질과 지질을 수정·가공·분류하여 세포 안팎으로 분비합니다.",
        "location": "소포체 근처, 세포막 부근",
        "relationship": "소포체에서 수송 소포를 받아 분비 소포로 싸서 세포막이나 리소좀으로 전달함",
        "keywords": ["단백질 가공", "분류 및 포장", "세포 외 분비"],
        "structures": {
            "시스 면(Cis face)": "소포체에서 오는 수송 소포를 받아들이는 쪽입니다.",
            "트랜스 면(Trans face)": "가공이 완료된 물질을 분비 소포에 담아 보내는 쪽입니다."
        }
    },
    "리소좀": {
        "icon": "♻️",
        "description": "다양한 가수분해 효소를 포함하여 세포 내 물질, 손상된 소기관, 외부 이물질을 분해합니다.",
        "location": "세포질 내부",
        "relationship": "골지체에서 형성되며, 식세포 작용으로 들어온 물질이나 노폐물과 융합하여 분해함",
        "keywords": ["세포 내 소화", "가수분해 효소", "자가포식 작용"],
        "structures": {
            "단일막": "강한 산성 효소가 세포질로 새어나가지 않도록 보호하는 단일 막입니다.",
            "가수분해 효소": "산성 환경(pH 4.5~5.0)에서 단백질, 지질, 핵산 등을 분해하는 효소입니다."
        }
    },
    "세포막": {
        "icon": "🛡️",
        "description": "세포와 외부 환경의 경계로, 물질의 출입을 선택적으로 조절하여 항상성을 유지합니다.",
        "location": "세포의 가장 바깥쪽 둘레",
        "relationship": "수송 단백질, 수용체 등을 통해 세포 외부 신호 및 물질 전달을 담당함",
        "keywords": ["선택적 투과성", "인지질 이중층", "막단백질"],
        "structures": {
            "인지질 이중층": "친수성 머리와 소수성 꼬리를 가진 인지질이 2중으로 배열되어 물질의 통과를 조절합니다.",
            "막단백질": "물질 수송, 세포 간 인식, 신호 전달 수용체 등의 다양한 기능을 수행합니다."
        }
    },
    "세포질": {
        "icon": "🌊",
        "description": "세포막 내부를 채우고 있는 액체 상태의 환경으로, 세포소기관들이 위치하고 여러 대사 과정이 일어납니다.",
        "location": "핵을 제외한 세포막 내부 전반",
        "relationship": "모든 소기관의 이동 및 물질 교환의 매개체 역할을 함",
        "keywords": ["대사 공간", "당분해 작용", "세포액"],
        "structures": {
            "세포액(Cytosol)": "물, 이온, 가용성 단백질, 효소 등이 용해되어 있는 액체 성분입니다."
        }
    },
    "세포골격": {
        "icon": "🏗️",
        "description": "세포의 형태를 유지하고, 소기관의 이동 및 세포 분열을 돕는 단백질 섬유 네트워크입니다.",
        "location": "세포질 전반에 그물망처럼 분포",
        "relationship": "모터 단백질과 함께 수송 소포 및 소기관 이동의 길 역할을 함",
        "keywords": ["세포 형태 유지", "내부 물질 이동", "세포 분열 도움"],
        "structures": {
            "미세관": "튜불린 단백질로 구성되며, 세포골격 중 가장 굵고 소기관 이동의 도로 역할을 합니다.",
            "중간섬유": "세포의 기계적 강도를 유지하고 핵의 위치를 고정합니다.",
            "미세섬유": "액틴 단백질로 구성되며, 세포 운동과 형태 변화, 세포질 분열에 참여합니다."
        }
    }
}

# -----------------------------------------------------------------------------
# 4. 사이드바 네비게이션
# -----------------------------------------------------------------------------
st.sidebar.title("🔬 세포 탐험 메뉴")
page_selection = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["Home — 세포 한눈에 보기", "Organelle Explorer — 소기관 상세 탐구", "Quiz & Simulation — 학습 확인"],
    index=0 if st.session_state["current_page"] == "Home" else (1 if st.session_state["current_page"] == "Explorer" else 2)
)

if "Home" in page_selection:
    st.session_state["current_page"] = "Home"
elif "Explorer" in page_selection:
    st.session_state["current_page"] = "Explorer"
else:
    st.session_state["current_page"] = "Quiz"

st.sidebar.markdown("---")
st.sidebar.caption("고등학교 생명과학 I / II 연계 수행평가용 웹앱")

# -----------------------------------------------------------------------------
# 5. PAGE 1: Home — 세포 한눈에 보기 (세포 모양 테두리 보완)
# -----------------------------------------------------------------------------
if st.session_state["current_page"] == "Home":
    st.title("🔬 동물세포 한눈에 보기")
    st.write("아래 **세포(Green Box)** 내부에 위치한 세포소기관 버튼을 클릭하면 상세 탐구 페이지로 이동합니다.")

    # 세포 전체를 나타내는 큰 테두리 박스 (세포막/세포질 표현)
    with st.container(border=True):
        st.markdown("### 🛡️ 세포막 (Cell Membrane) & 🌊 세포질 (Cytosol)")
        st.caption("※ 세포 내부에 배치된 소기관 버튼을 누르면 해당 소기관으로 이동합니다.")
        st.markdown("---")

        # 세포 내부 3x3 격자 배치
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🧠 핵\n\n(DNA 저장 / 유전자 조절)", key="btn_nucle", use_container_width=True):
                st.session_state["selected_organelle"] = "핵"
                st.session_state["current_page"] = "Explorer"
                st.rerun()
                
            if st.button("📦 소포체\n\n(단백질 및 지질 수송)", key="btn_er", use_container_width=True):
                st.session_state["selected_organelle"] = "소포체"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

            if st.button("⚙️ 리보솜\n\n(단백질 합성 공장)", key="btn_ribo", use_container_width=True):
                st.session_state["selected_organelle"] = "리보솜"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

        with col2:
            if st.button("⚡ 미토콘드리아\n\n(세포 호흡 & ATP 생성)", key="btn_mito", use_container_width=True):
                st.session_state["selected_organelle"] = "미토콘드리아"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

            if st.button("📮 골지체\n\n(단백질 가공 및 분비)", key="btn_golgi", use_container_width=True):
                st.session_state["selected_organelle"] = "골지체"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

            if st.button("♻️ 리소좀\n\n(세포 내 물질 분해)", key="btn_lyso", use_container_width=True):
                st.session_state["selected_organelle"] = "리소좀"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

        with col3:
            if st.button("🛡️ 세포막\n\n(선택적 투과성 조절)", key="btn_mem", use_container_width=True):
                st.session_state["selected_organelle"] = "세포막"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

            if st.button("🌊 세포질\n\n(대사 과정 진행 공간)", key="btn_cyto", use_container_width=True):
                st.session_state["selected_organelle"] = "세포질"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

            if st.button("🏗️ 세포골격\n\n(형태 유지 & 물질 이동)", key="btn_skel", use_container_width=True):
                st.session_state["selected_organelle"] = "세포골격"
                st.session_state["current_page"] = "Explorer"
                st.rerun()

# -----------------------------------------------------------------------------
# 6. PAGE 2: Organelle Explorer — 세포소기관 탐구
# -----------------------------------------------------------------------------
elif st.session_state["current_page"] == "Explorer":
    st.title("🔬 Organelle Explorer — 소기관 상세 탐구")
    st.write("상단 메뉴에서 소기관을 변경하고, 세부 구조 버튼을 클릭하여 깊이 있게 학습해 보세요.")

    organelles = list(ORGANELLES_DATA.keys())
    cols = st.columns(len(organelles))

    for idx, name in enumerate(organelles):
        btn_label = f"{ORGANELLES_DATA[name]['icon']} {name}"
        if cols[idx].button(btn_label, key=f"exp_btn_{name}", use_container_width=True):
            st.session_state["selected_organelle"] = name
            st.rerun()

    selected = st.session_state["selected_organelle"]
    data = ORGANELLES_DATA[selected]

    st.markdown("---")

    st.header(f"{data['icon']} {selected}")
    st.caption(f"📍 **세포 내 위치:** {data['location']}")

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.subheader("📌 주요 기능")
        st.info(data["description"])

        st.subheader("🔗 연계된 세포소기관")
        st.write(data["relationship"])

        st.subheader("🔑 핵심 키워드")
        keywords_html = "".join([f'<span class="tag">#{kw}</span>' for kw in data["keywords"]])
        st.markdown(keywords_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.subheader("🧩 구조 인터랙티브 탐구")
        st.write("아래 구조 버튼을 눌러 세부 설명과 역할을 확인하세요.")

        structures = data["structures"]
        struct_names = list(structures.keys())

        s_cols = st.columns(len(struct_names))
        selected_struct = st.session_state.get(f"struct_{selected}", struct_names[0])

        for s_idx, s_name in enumerate(struct_names):
            if s_cols[s_idx].button(s_name, key=f"s_btn_{selected}_{s_name}", use_container_width=True):
                selected_struct = s_name
                st.session_state[f"struct_{selected}"] = s_name

        if selected_struct in structures:
            st.success(f"**[{selected_struct}]**\n\n{structures[selected_struct]}")
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 7. PAGE 3: Quiz & Simulation — 학습 확인
# -----------------------------------------------------------------------------
elif st.session_state["current_page"] == "Quiz":
    st.title("🧩 학습 확인 & 미니 시뮬레이션")

    tab1, tab2 = st.tabs(["📝 개념 확인 퀴즈", "🔄 단백질 합성/분비 과정 시뮬레이션"])

    with tab1:
        st.subheader("세포소기관 개념 퀴즈")

        q1 = st.radio(
            "1. 세포 호흡을 통해 ATP를 대량 생성하는 소기관은 무엇인가요?",
            ["핵", "미토콘드리아", "골지체", "리소좀"],
            index=None
        )
        if q1 == "미토콘드리아":
            st.success("정답입니다! 미토콘드리아의 크리스타와 기질에서 ATP가 생성됩니다.")
        elif q1 is not None:
            st.error("다시 시도해 보세요!")

        st.markdown("---")

        q2 = st.radio(
            "2. 리보솜에서 합성된 단백질이 가공되어 외부로 분비되는 올바른 경로 순서는?",
            [
                "소포체 ➔ 골지체 ➔ 분비 소포 ➔ 세포막",
                "골지체 ➔ 소포체 ➔ 핵 ➔ 세포막",
                "리소좀 ➔ 미토콘드리아 ➔ 골지체",
                "세포골격 ➔ 핵 ➔ 리보솜"
            ],
            index=None
        )
        if q2 == "소포체 ➔ 골지체 ➔ 분비 소포 ➔ 세포막":
            st.success("정답입니다! 소포체와 골지체를 거쳐 세포 밖으로 분비됩니다.")
        elif q2 is not None:
            st.error("다시 시도해 보세요!")

    with tab2:
        st.subheader("⚙️ 단백질 분비 경로 단계별 시뮬레이션")
        st.write("슬라이더를 움직여 단백질 이동 경로를 확인해 보세요.")

        step = st.slider("단계 선택", min_value=1, max_value=4, value=1, step=1)

        steps_info = {
            1: ("🧠 핵 (Nucleus)", "DNA의 유전 정보가 mRNA로 전사되어 핵공을 통해 세포질로 나옵니다."),
            2: ("⚙️ 리보솜 & 거친면 소포체", "리보솜이 mRNA를 번역하여 단백질을 합성하고 소포체로 들어갑니다."),
            3: ("📮 골지체 (Golgi apparatus)", "수송 소포로 전달된 단백질이 골지체에서 최종 가공 및 포장됩니다."),
            4: ("🛡️ 세포막 및 분비 (Exocytosis)", "분비 소포가 세포막과 융합하여 단백질을 세포 외부로 분비합니다.")
        }

        title, desc = steps_info[step]
        st.markdown(f"### Step {step}: {title}")
        st.info(desc)
        st.progress(step / 4)
