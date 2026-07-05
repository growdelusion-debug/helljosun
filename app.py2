import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정 및 다크 테마 고정
st.set_page_config(page_title="헤르조르센 (Herzorsen)", layout="centered")

# 2. 인트로 및 진영 선택용 전통 사극풍 & 스타일리시 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gungsuh&family=Noto+Sans+KR:wght@400;700&display=swap');
    
    /* 기본 배경 및 폰트 세팅 */
    .stApp {
        background-color: #1a0000;
        color: #ffffff;
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 인트로 타이틀: 네온 레드 궁서체 */
    .intro-title {
        font-family: 'Gungsuh', '궁서', serif;
        color: #ff3333;
        font-size: 70px;
        text-align: center;
        font-weight: bold;
        margin-top: 40px;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #8b0000;
        letter-spacing: 5px;
    }
    
    /* 인트로 스토리 상자 */
    .intro-box {
        background: border-box;
        border: 2px solid #ffd700;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        line-height: 1.8;
        margin: 30px auto;
        max-width: 600px;
        background-color: #2b0000;
    }
    
    /* 진영 선택 카드 디자인 */
    .faction-card {
        background: #111111;
        border: 2px solid #333333;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .faction-card:hover {
        transform: translateY(-5px);
    }
    .card-catmom:hover {
        border-color: #00ffcc;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
    }
    .card-cathate:hover {
        border-color: #ff4444;
        box-shadow: 0 0 15px rgba(255, 68, 68, 0.4);
    }
    
    /* 공통 스타일 버튼 */
    .stButton>button {
        background-color: #ffd700;
        color: #000000;
        font-weight: bold;
        font-size: 18px;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        box-shadow: 0 0 10px #ffd700;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 세션 상태(Session State) 관리
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
if 'faction' not in st.session_state:
    st.session_state.faction = None

# --- [화면 1: 인트로 세션] ---
if st.session_state.stage == 'intro':
    st.markdown('<div class="intro-title">헤르조르센</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="intro-box">
        당신은 시공간의 균열로 현대의 <b>헤르조르센</b>에 떨어진 <b>효령대군</b>입니다.<br>
        도시를 뒤흔드는 아수라장 속에서 진영을 선택하고,<br>
        밀려오는 적들로부터 방어 구역을 끝까지 수호하여 승리하십시오!
    </div>
    """, unsafe_allow_html=True)
    
    col_center = st.columns
