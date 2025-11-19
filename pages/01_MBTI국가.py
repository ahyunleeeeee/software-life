import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="국가별 MBTI 비율 시뮬레이터", layout="wide")

st.title("🌍 국가별 MBTI 비율 대시보드 (가상 데이터)")

# -------------------------
# 1. 가상 MBTI 비율 데이터 생성
# -------------------------

types = ["ISTJ","ISFJ","INFJ","INTJ",
         "ISTP","ISFP","INFP","INTP",
         "ESTP","ESFP","ENFP","ENTP",
         "ESTJ","ESFJ","ENFJ","ENTJ"]

countries = ["South Korea", "United States", "Japan", "Germany", "Brazil"]

np.random.seed(42)

data = {
    "country": [],
    "type": [],
    "proportion": []
}

for country in countries:
    r = np.random.rand(len(types))
    r = r / r.sum()
    for t, p in zip(types, r):
        data["country"].append(country)
        data["type"].append(t)
        data["proportion"].append(p)

df = pd.DataFrame(data)

# -------------------------
# 2. 국가 선택
# -------------------------
st.sidebar.header("국가 선택")
selected_country = st.sidebar.selectbox("국가를 선택하세요", countries)

country_df = df[df["country"] == selected_country].sort_values("proportion", ascending=False)

# -------------------------
# 3. Plotly 막대그래프 생성
#    - 1등 빨간색
#    - 나머지는 파란색 → 회색 그라데이션
# -------------------------

max_val = country_df["proportion"].max()

colors = []
for v in country_df["proportion"]:
    if v == max_val:
        colors.append("red")
    else:
        # 1등 제외 나머지는 밝은 파랑 → 회색 계열 색상으로 그라데이션
        ratio = v / max_val
        gray_val = int(200 - ratio * 120)
        colors.append(f"rgb({gray_val},{gray_val+20},{gray_val+40})")

fig = go.Figure(
    data=[
        go.Bar(
            x=country_df["type"],
            y=country_df["proportion"],
            marker_color=colors
        )
    ]
)

fig.update_layout(
    title=f"{selected_country} MBTI 비율 (가상 데이터)",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="simple_white"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# 4. 데이터 테이블 표시
# -------------------------
with st.expander("📊 데이터 테이블 보기"):
    st.dataframe(country_df.reset_index(drop=True))
