import streamlit as st

# 페이지 설정
st.set_page_config(page_title="베스킨라빈스 키오스크 🍨", page_icon="🍧", layout="centered")

st.title("🍨 베스킨라빈스 키오스크에 오신 걸 환영해요! 😊")

# -------------------------------
# 1. 식사 방식 선택
# -------------------------------
st.header("1️⃣ 매장에서 드시나요, 포장해 가시나요? 🛍️")
order_type = st.radio("원하는 옵션을 골라주세요!", ["매장 🍽️", "포장 🧁"])

# -------------------------------
# 2. 용기 선택
# -------------------------------
st.header("2️⃣ 용기를 선택해 주세요! 🥄")

container_info = {
    "싱글 레귤러(₩3,500)": {"scoops": 1, "price": 3500},
    "싱글 킨(₩4,300)": {"scoops": 2, "price": 4300},
    "더블 주니어(₩5,200)": {"scoops": 2, "price": 5200},
    "더블 레귤러(₩7,000)": {"scoops": 2, "price": 7000},
    "파인트(₩9,200)": {"scoops": 3, "price": 9200},
    "쿼터(₩15,500)": {"scoops": 4, "price": 15500},
    "패밀리(₩22,000)": {"scoops": 5, "price": 22000},
    "하프갤런(₩26,000)": {"scoops": 6, "price": 26000},
}

container_name = st.selectbox("용기를 골라주세요 🍧", list(container_info.keys()))
scoop_count = container_info[container_name]["scoops"]
price = container_info[container_name]["price"]

# -------------------------------
# 3. 아이스크림 맛 선택
# -------------------------------
st.header("3️⃣ 아이스크림 맛을 골라볼까요? 🍦")

flavors = [
    "바닐라", "초콜릿", "민트초코", "슈팅스타", "엄마는외계인",
    "레인보우샤베트", "쿠키앤크림", "베리베리스트로베리",
    "체리쥬빌레", "이상한나라의솜사탕"
]

selected_flavors = []
st.write(f"👉 총 **{scoop_count}가지 맛**을 선택할 수 있어요!")

for i in range(scoop_count):
    selected = st.selectbox(
        f"{i+1}번째 맛 선택 🍨",
        ["선택 안 함"] + flavors,
        key=f"flavor_{i}"
    )
    selected_flavors.append(selected)

# -------------------------------
# 4. 가격 및 결제 선택
# -------------------------------
st.header("4️⃣ 결제를 진행할게요! 💳")

if st.button("💰 주문 확인하기"):
    # 검증
    if any(flavor == "선택 안 함" for flavor in selected_flavors):
        st.error("⚠️ 아직 선택하지 않은 맛이 있어요. 모두 골라주세요!")
    else:
        st.success("주문이 완성되었습니다! 👏")

        st.subheader("🧾 주문 내역")
        st.write(f"• 이용 방식: **{order_type}**")
        st.write(f"• 용기: **{container_name}**")
        st.write("• 선택한 맛:")
        for idx, f in enumerate(selected_flavors, 1):
            st.write(f"   - {idx}. {f}")

        st.subheader("💵 최종 결제 금액")
        st.write(f"### 👉 **총 {price:,}원** 입니다!")

        payment = st.radio("결제 방법을 선택해 주세요 😊", ["현금 💵", "카드 💳"])
        st.success(f"🌟 {payment} 결제를 선택하셨어요! 감사합니다! 🍨")
