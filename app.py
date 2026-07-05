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
    
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button("🚨 헤르조르센 입장하기", use_container_width=True):
            st.session_state.stage = 'select_faction'
            st.rerun()

# --- [화면 2: 진영 선택 세션] ---
elif st.session_state.stage == 'select_faction':
    st.markdown("<h2 style='text-align: center; color: #ffd700; font-family: 궁서;'>- 진영 선택 (Faction) -</h2>", unsafe_allow_html=True)
    st.write("\n")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="faction-card card-catmom">
            <h3 style="color: #00ffcc;">🐱 캣맘파</h3>
            <p style="font-size: 50px; margin: 10px 0;">🧑‍🤝‍🧑</p>
            <p style="color: #bbb;"><b>무기:</b> 고전 목제 새총 (돌멩이)</p>
            <p style="color: #bbb;"><b>방어 대상:</b> 상처 입은 새들의 공습</p>
            <p style="font-size: 13px; color: #777;">"생명은 소중합니다. 새들의 보복을 막으세요!"</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🟢 캣맘파 선택", use_container_width=True):
            st.session_state.faction = 'cat_mom'
            
    with col2:
        st.markdown("""
        <div class="faction-card card-cathate">
            <h3 style="color: #ff4444;">🐦 캣싫어파</h3>
            <p style="font-size: 50px; margin: 10px 0;">🦅</p>
            <p style="color: #bbb;"><b>무기:</b> SF 네온 물총 (물줄기)</p>
            <p style="color: #bbb;"><b>방어 대상:</b> 고양이를 안은 사람들의 진격</p>
            <p style="font-size: 13px; color: #777;">"공태기 파괴범들! 집착 섞인 진격을 저지하세요!"</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔴 캣싫어파 선택", use_container_width=True):
            st.session_state.faction = 'cat_hate'

    st.write("---")
    if st.session_state.faction:
        f_name = "🐱 캣맘파" if st.session_state.faction == 'cat_mom' else "🐦 캣싫어파"
        st.markdown(f"<h4 style='text-align: center;'>선택된 세력: <span style='color:#ffd700;'>{f_name}</span></h4>", unsafe_allow_html=True)
        
        if st.button("⚔️ 선택 완료, 전쟁 시작", use_container_width=True):
            st.session_state.stage = 'battle'
            st.rerun()

# --- [화면 3 & 4: 인게임 전투 및 결과창 (HTML5 Canvas 엔진)] ---
elif st.session_state.stage == 'battle':
    
    # 세력 정보에 따른 캔버스 데이터 연동
    faction = st.session_state.faction
    theme_color = "#00ffcc" if faction == 'cat_mom' else "#ff4444"
    
    # 하이브리드 자바스크립트 엔진 소스코드
    game_html = f"""
    <div id="game-wrapper" style="text-align: center; font-family: 'Noto Sans KR', sans-serif; background-color: #0c0c0c; padding: 15px; border-radius: 12px;">
        <canvas id="gameCanvas" width="500" height="600" style="border: 3px solid {theme_color}; box-shadow: 0 0 20px {theme_color}; background:#151518; border-radius: 8px; cursor: crosshair;"></canvas>
    </div>

    <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // --- 게임 상태 관리 변수 ---
    let timeLeft = 60;        // 최적화된 60초 제한시간
    let myScore = 0;
    let enemyScore = 0;
    let gameState = 'countdown'; 
    let countdownTime = 3;
    let phase = 1;
    let hasUlt = true;         // 스페이스바 필살기 소유 여부
    let ultActiveTimer = 0;    // 필살기 번쩍임 이펙트 타이머
    
    // 화면 흔들림(Screen Shake) 효과 변수
    let shakeTimer = 0;
    let shakeIntensity = 0;

    // 객체 배열
    let bullets = [];
    let enemies = [];
    let particles = [];        // 타격 파편 이펙트 입자

    // 4개 고정 라인 무기 좌표
    const lanes = [62, 187, 312, 437];
    const weapons = lanes.map(x => ({{ x: x, y: 550, lastFired: 0 }}));
    const fireCooldown = 150; // 0.15초 연속발사 제한

    // 키 입력 리스너 (1, 2, 3, 4: 무기 발사 / Space: 필살기)
    window.addEventListener('keydown', (e) => {{
        if (gameState !== 'playing') return;
        const now = Date.now();
        if (e.key === '1' && now - weapons[0].lastFired > fireCooldown) {{ fireBullet(0); weapons[0].lastFired = now; }}
        if (e.key === '2' && now - weapons[1].lastFired > fireCooldown) {{ fireBullet(1); weapons[1].lastFired = now; }}
        if (e.key === '3' && now - weapons[2].lastFired > fireCooldown) {{ fireBullet(2); weapons[2].lastFired = now; }}
        if (e.key === '4' && now - weapons[3].lastFired > fireCooldown) {{ fireBullet(3); weapons[3].lastFired = now; }}
        
        if (e.key === ' ' || e.code === 'Space') {{
            e.preventDefault();
            if (hasUlt) useUltimate();
        }}
    }});

    function fireBullet(index) {{
        bullets.push({{ x: weapons[index].x, y: weapons[index].y - 25 }});
    }}

    // 효령대군의 가호 필살기 (화면 안 적 전멸 및 대형 타격)
    function useUltimate() {{
        hasUlt = false;
        ultActiveTimer = 15; // 15 프레임 동안 화면 번쩍임
        triggerShake(15, 10);
        
        enemies.forEach(e => {{
            myScore += 5;
            createParticles(e.x, e.y, "{theme_color}");
        }});
        enemies = [];
    }}

    // 화면 흔들림 발동 함수
    function triggerShake(duration, intensity) {{
        shakeTimer = duration;
        shakeIntensity = intensity;
    }}

    // 적 처치 시 튀는 파편 생성
    function createParticles(x, y, color) {{
        for (let i = 0; i < 6; i++) {{
            particles.push({{
                x: x, y: y,
                vx: (Math.random() - 0.5) * 6,
                vy: (Math.random() - 0.5) * 6,
                radius: Math.random() * 3 + 2,
                alpha: 1,
                color: color
            }});
        }}
    }}

    // 타이머 처리 시스템
    let countdownInterval = setInterval(() => {{
        if (gameState === 'countdown') {{
            countdownTime--;
            if (countdownTime <= 0) {{
                gameState = 'playing';
                clearInterval(countdownInterval);
                startMainTimer();
            }}
        }}
    }}, 1000);

    function startMainTimer() {{
        let timer = setInterval(() => {{
            if (gameState === 'playing') {{
                timeLeft--;
                
                // 페이즈 변동 벨런스 적용
                if (timeLeft <= 40 && timeLeft > 15) phase = 2;
                else if (timeLeft <= 15) phase = 3;

                if (timeLeft <= 0) {{
                    gameState = 'ended';
                    clearInterval(timer);
                }}
            }}
        }, 1000);
    }}

    // 적 스폰 시스템 (페이즈에 맞춰 주기 단축)
    let spawnCounter = 0;
    function handleEnemySpawning() {{
        spawnCounter++;
        let spawnInterval = phase === 1 ? 45 : (phase === 2 ? 25 : 12); // 난이도 대폭 상승
        
        if (spawnCounter >= spawnInterval) {{
            spawnCounter = 0;
            let randomLane = Math.floor(Math.random() * 4);
            let baseSpeed = phase === 1 ? 2.5 : (phase === 2 ? 4.2 : 6.0);
            enemies.push({{
                x: lanes[randomLane],
                y: -20,
                speed: baseSpeed + Math.random() * 1.5,
                pulse: 0
            }});
        }}
    }}

    // --- 메인 60FPS 렌더링 루프 ---
    function render() {{
        ctx.save();
        
        // 화면 흔들림 효과 연출 연산
        if (shakeTimer > 0) {{
            let dx = (Math.random() - 0.5) * shakeIntensity;
            let dy = (Math.random() - 0.5) * shakeIntensity;
            ctx.translate(dx, dy);
            shakeTimer--;
        }}

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 1. 인게임 배경 그리기 (사이버펑크 아스팔트 격자 패턴)
        ctx.fillStyle = "#16161a";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        ctx.strokeStyle = "#222226";
        ctx.lineWidth = 1;
        for(let i=0; i<canvas.width; i+=40) {{
            ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
        }}
        for(let j=0; j<canvas.height; j+=40) {{
            ctx.beginPath(); ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); ctx.stroke();
        }}

        // 공격/방어 네온 경계선 
        ctx.strokeStyle = "{theme_color}";
        ctx.shadowBlur = 10;
        ctx.shadowColor = "{theme_color}";
        ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(0, 460); ctx.lineTo(500, 460); ctx.stroke();
        ctx.shadowBlur = 0; // 그림자 초기화

        // 카운트다운 연출
        if (gameState === 'countdown') {{
            ctx.fillStyle = "#ffd700";
            ctx.font = "bold 80px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText(countdownTime, canvas.width/2, canvas.height/2 + 20);
            ctx.restore();
            requestAnimationFrame(render);
            return;
        }}

        // 최종 게임 종료 결과창 (완전 암전 및 트렌디 이펙트)
        if (gameState === 'ended') {{
            ctx.fillStyle = "#000000";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.textAlign = "center";
            
            let win = myScore >= enemyScore;
            if (win) {{
                ctx.fillStyle = "#FFD700";
                ctx.font = "bold 75px sans-serif";
                ctx.shadowBlur = 15; ctx.shadowColor = "#FFD700";
                ctx.fillText("WIN", canvas.width/2, canvas.height/2 - 20);
            }} else {{
                ctx.fillStyle = "#757575";
                ctx.font = "bold 75px sans-serif";
                ctx.fillText("LOSE", canvas.width/2, canvas.height/2 - 20);
            }}
            ctx.shadowBlur = 0;
            
            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 20px sans-serif";
            ctx.fillText("최종 스코어 리포트", canvas.width/2, canvas.height/2 + 50);
            ctx.font = "16px sans-serif";
            ctx.fillStyle = "#aaa";
            ctx.fillText("효령대군(우리 팀): " + myScore + " 점 | 상대 세력: " + enemyScore + " 점", canvas.width/2, canvas.height/2 + 85);
            ctx.fillStyle = "#ffd700";
            ctx.fillText("하단의 '🔄 다시 도전하기' 버튼을 눌러주세요.", canvas.width/2, canvas.height/2 + 130);
            ctx.restore();
            return;
        }}

        // --- 2. 실시간 오브젝트 연산 (Playing) ---
        handleEnemySpawning();

        // [UI 스코어보드]
        ctx.fillStyle = "rgba(0, 0, 0, 0.6)";
        ctx.fillRect(10, 10, 480, 45);
        ctx.fillStyle = "#ffffff";
        ctx.font = "bold 15px sans-serif";
        ctx.textAlign = "left";
        ctx.fillText("⏱️ 시간: " + timeLeft + "초 (PHASE " + phase + ")", 25, 38);
        ctx.textAlign = "center";
        ctx.fillText("🏆 우리 점수: " + myScore, 250, 38);
        ctx.textAlign = "right";
        ctx.fillText("😈 상대 점수: " + enemyScore, 475, 38);

        // 필살기 가이드 UI
        if(hasUlt) {{
            ctx.fillStyle = "#ffd700";
            ctx.font = "12px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText("[SPACEBAR] 효령대군의 가호 발동 가능", canvas.width/2, 80);
        }}

        // 아군 무기 오브젝트 렌더링
        weapons.forEach((w, i) => {{
            ctx.fillStyle = "{theme_color}";
            if ("{faction}" === "cat_mom") {{
                // 새총 모양 묘사 (V자 프레임)
                ctx.lineWidth = 4;
                ctx.strokeStyle = "#8b5a2b";
                ctx.beginPath();
                ctx.moveTo(w.x - 15, w.y - 15); ctx.lineTo(w.x, w.y + 10); ctx.lineTo(w.x + 15, w.y - 15);
                ctx.stroke();
            }} else {{
                // SF 물총 묘사
                ctx.fillRect(w.x - 8, w.y - 20, 16, 30);
                ctx.fillStyle = "#00bfff";
                ctx.fillRect(w.x - 3, w.y - 25, 6, 10);
            }}
            ctx.fillStyle = "#ffffff";
            ctx.font = "bold 11px sans-serif";
            ctx.textAlign = "center";
            ctx.fillText((i+1), w.x, w.y + 25);
        }});

        // 투사체 이동 및 충돌 체크
        for (let i = bullets.length - 1; i >= 0; i--) {{
            bullets[i].y -= 8; // 투사체 속도
            ctx.fillStyle = "{faction}" === "cat_mom" ? "#9e9e9e" : "#00ffea";
            ctx.shadowBlur = "{faction}" === "cat_mom" ? 0 : 8;
            ctx.shadowColor = "#00ffea";
            
            ctx.beginPath();
            ctx.arc(bullets[i].x, bullets[i].y, "{faction}" === "cat_mom" ? 6 : 4, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0;

            if (bullets[i].y < 0) {{ bullets.splice(i, 1); continue; }}
        }}

        // 적군 돌격 가속 및 렌더링
        for (let i = enemies.length - 1; i >= 0; i--) {{
            enemies[i].y += enemies[i].speed;
            enemies[i].pulse += 0.1;

            // 픽셀 스타일 캐릭터 외형 드로잉
            ctx.save();
            ctx.translate(enemies[i].x, enemies[i].y);
            if ("{faction}" === "cat_mom") {{
                // 적군: 상처 입은 새 (붉은 픽셀 날개짓)
                ctx.fillStyle = "#ff5555";
                ctx.fillRect(-12, -12, 24, 24);
                ctx.fillStyle = "#ff0000"; // 눈
                ctx.fillRect(4, -8, 4, 4);
                // 날개 구현
                let wingShift = Math.sin(enemies[i].pulse) * 8;
                ctx.fillStyle = "#cc4444";
                ctx.fillRect(-20, -6, 8, wingShift);
            }} else {{
                // 적군: 고양이를 안고 돌격하는 사람 실루엣
                ctx.fillStyle = "#e0aaff";
                ctx.beginPath(); ctx.arc(0, -10, 8, 0, Math.PI*2); ctx.fill(); // 머리
                ctx.fillRect(-10, -2, 20, 20); // 몸통
                ctx.fillStyle = "#ffb703"; // 품에 안긴 네온 고양이
                ctx.fillRect(-6, 2, 12, 10);
            }}
            ctx.restore();

            // 방어선 침투 판단 (패널티 스코어 유발)
            if (enemies[i].y >= 460) {{
                enemyScore += 10;
                enemies.splice(i, 1);
                triggerShake(8, 6); // 하방 돌파 시 화면 격렬히 흔들림
                continue;
            }}

            // 충돌 감지 로직
            for (let j = bullets.length - 1; j >= 0; j--) {{
                let dist = Math.hypot(enemies[i].x - bullets[j].x, enemies[i].y - bullets[j].y);
                if (dist < 20) {{
                    myScore += 5;
                    createParticles(enemies[i].x, enemies[i].y, "{theme_color}");
                    enemies.splice(i, 1);
                    bullets.splice(j, 1);
                    break;
                }}
            }}
        }}

        // 입자 파편(Particles) 업데이트 및 드로잉
        for (let i = particles.length - 1; i >= 0; i--) {{
            particles[i].x += particles[i].vx;
            particles[i].y += particles[i].vy;
            particles[i].alpha -= 0.04;
            if (particles[i].alpha <= 0) {{
                particles.splice(i, 1);
                continue;
            }}
            ctx.save();
            ctx.globalAlpha = particles[i].alpha;
            ctx.fillStyle = particles[i].color;
            ctx.beginPath();
            ctx.arc(particles[i].x, particles[i].y, particles[i].radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }}

        // 페이즈 3 (마지막 15초 남았을 때) 사이렌 경고 외곽 비네팅 광원 연출
        if (phase === 3 && Math.floor(Date.now() / 300) % 2 === 0) {{
            let gradient = ctx.createRadialGradient(canvas.width/2, canvas.height/2, 200, canvas.width/2, canvas.height/2, 350);
            gradient.addColorStop(0, 'rgba(255,0,0,0)');
            gradient.addColorStop(1, 'rgba(255,0,0,0.35)');
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }}

        // 필살기 가동 시 화면 번쩍임 흰색 오버레이
        if (ultActiveTimer > 0) {{
            ctx.fillStyle = "rgba(255, 255, 255, " + (ultActiveTimer/15) + ")";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ultActiveTimer--;
        }}

        ctx.restore();
        requestAnimationFrame(render);
    }}

    render();
    </script>
    """
    
    # 컴포넌트를 통해 Canvas 인터페이스 임베딩
    components.html(game_html, height=645)
    
    # 조작 안내 메시지 가이드 세팅
    st.markdown("""
        <div style="text-align:center; color:#888; font-size:14px; line-height:1.6;">
            💡 <b>조작 방법 안내</b><br>
            키보드 상단 숫자 패드 <b>[1], [2], [3], [4]</b>를 리드미컬하게 눌러 해당 라인의 무기를 발사하세요.<br>
            위기 상황 시 <b>[Spacebar]</b>를 누르면 <b>'효령대군의 가호'</b> 전체 전멸기가 발동합니다. (스테이지 당 단 1회)
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # 다시하기 버튼 터치 시 리셋 프로시저
    if st.button("🔄 다시 도전하기 (처음으로)", use_container_width=True):
        st.session_state.stage = 'intro'
        st.session_state.faction = None
        st.rerun()
