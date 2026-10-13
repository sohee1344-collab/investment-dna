import streamlit as st

st.set_page_config(page_title="나의 투자 DNA는?", page_icon="💰", layout="centered")

QUESTIONS = [
    ("여윳돈 100만 원이 생겼다면?", ["원금이 안전한 곳에 보관한다", "안전한 자산과 투자에 나눠 둔다", "수익 기회를 찾아 적극 투자한다"]),
    ("투자금이 한 달 만에 10% 하락했다면?", ["손실이 더 커지기 전에 정리하고 싶다", "원인을 확인하고 기다릴지 결정한다", "여유자금이 있다면 추가 투자도 검토한다"]),
    ("투자할 돈은 언제쯤 필요할까?", ["1년 이내", "1~3년 후", "3년 이상 뒤"]),
    ("투자 경험에 가장 가까운 것은?", ["예금·적금 위주로 이용했다", "펀드나 ETF에 소액 투자해 봤다", "주식 등 가격 변동이 큰 상품도 경험했다"]),
    ("친구가 고수익 투자 이야기를 한다면?", ["원금 손실이 걱정돼 참여하지 않는다", "상품과 위험을 먼저 공부한다", "위험을 확인한 뒤 기회를 적극 검토한다"]),
    ("1년 동안 기대하는 투자 결과는?", ["수익이 적더라도 손실을 최소화하고 싶다", "적절한 수익과 위험의 균형이 좋다", "손실 가능성을 감수하고 높은 수익을 추구한다"]),
    ("예상치 못한 지출이 생겼을 때?", ["투자금을 바로 사용해야 할 수 있다", "일부 비상자금은 따로 준비돼 있다", "충분한 비상자금이 있어 투자금을 유지할 수 있다"]),
    ("투자상품을 고를 때 가장 먼저 보는 것은?", ["원금 손실 가능성", "위험 대비 기대수익과 분산 효과", "성장 가능성과 기대수익"]),
    ("투자자산 가격이 크게 오르내린다면?", ["가격 변동 자체가 스트레스다", "계획한 범위라면 견딜 수 있다", "장기 목표를 위해 큰 변동도 감수할 수 있다"]),
    ("투자에 관해 가장 공감하는 생각은?", ["잃지 않는 것이 가장 중요하다", "위험을 관리하며 꾸준히 투자하고 싶다", "충분히 이해한 위험이라면 적극 감수할 수 있다"]),
]

TYPES = [
    ("🐢", "안전제일 거북이", "원금 보존과 안정성을 가장 중요하게 생각하는 편이에요.", "예상 손실 규모와 자금 사용 시점을 먼저 확인해 보세요."),
    ("🦫", "신중한 저축왕", "안정성을 선호하지만 작은 투자 기회도 살펴보는 편이에요.", "비상자금과 투자금을 구분하고 상품의 위험을 확인해 보세요."),
    ("🦊", "균형 잡힌 전략가", "위험과 기대수익 사이에서 균형을 찾는 편이에요.", "분산투자와 정기적인 투자계획 점검을 고려해 보세요."),
    ("🐆", "기회를 찾는 탐험가", "변동성을 어느 정도 감수하며 성장 기회를 찾는 편이에요.", "손실 허용 범위를 미리 정하고 과도한 집중투자를 경계해 보세요."),
    ("🦁", "과감한 도전자", "높은 변동성도 감수하며 적극적인 수익 기회를 추구하는 편이에요.", "높은 위험 선호와 실제 손실 감내 능력은 다를 수 있다는 점을 기억하세요."),
]

if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

st.title("💰 나의 투자 DNA는?")
st.write("10가지 상황으로 가볍게 알아보는 나의 투자 성향")
st.caption("약 3분 · 10문항 · 5가지 결과 유형")
st.divider()

step = st.session_state.step
if step < len(QUESTIONS):
    st.write(f"**질문 {step + 1} / {len(QUESTIONS)}**")
    st.progress(step / len(QUESTIONS))
    question, options = QUESTIONS[step]
    st.subheader(question)
    choice = st.radio("나와 가장 가까운 선택지를 골라주세요.", options, index=st.session_state.answers.get(step), key=f"question_{step}")
    left, right = st.columns(2)
    with left:
        if st.button("← 이전", disabled=step == 0, use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
    with right:
        if st.button("결과 보기 →" if step == len(QUESTIONS) - 1 else "다음 →", disabled=choice is None, type="primary", use_container_width=True):
            st.session_state.answers[step] = options.index(choice)
            st.session_state.step += 1
            st.rerun()
else:
    score = sum(st.session_state.answers.values())
    # 10문항 × 0~2점 = 0~20점. 교육용 임의 구간이며 검증된 금융기관 분류 기준이 아닙니다.
    tier = min(score // 4, 4) if score < 20 else 4
    emoji, name, description, tip = TYPES[tier]
    st.progress(1.0)
    st.markdown(f"# {emoji} {name}")
    st.metric("나의 탐색 점수", f"{score} / 20점")
    st.write(description)
    st.info(f"💡 **투자할 때 기억할 점**: {tip}")
    st.caption("이 점수는 성향을 재미로 탐색하기 위한 값이며, 투자 적합성이나 실제 손실 감내 능력을 인증하지 않습니다.")
    if st.button("🔄 다시 테스트하기", use_container_width=True):
        st.session_state.step = 0
        st.session_state.answers = {}
        for i in range(len(QUESTIONS)):
            st.session_state.pop(f"question_{i}", None)
        st.rerun()

st.divider()
st.caption("⚠️ 본 서비스는 금융교육용 간이 테스트입니다. 금융기관의 공식 투자자정보 확인·투자성향 분석이나 개인별 투자 권유를 대체하지 않습니다. 투자에는 원금 손실 위험이 있습니다.")
