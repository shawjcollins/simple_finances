
import streamlit as st

def calculate_wealth_gap(goal, swr, net_worth):
    target_nest_egg = goal / swr
    gap = target_nest_egg - net_worth
    status = f"✅ You have achieved Financial Freedom!" if gap <= 0 else f"🚧 Wealth Gap: ${gap:,.0f}"
    return target_nest_egg, gap, status

st.title("💰 Wealth Gap Analysis")

# User inputs
goal = st.number_input("Annual Financial Freedom Goal ($)", min_value=10000, step=5000, value=250000)
swr = st.number_input("Safe Withdrawal Rate (%)", min_value=0.01, max_value=0.10, step=0.005, value=0.04, format="%.3f")
net_worth = st.number_input("Current Net Worth (Excludes Home) ($)", min_value=0, step=10000, value=2000000)

# Calculation
target, gap, status = calculate_wealth_gap(goal, swr, net_worth)

# Output
st.markdown(f"### 🧮 Capital Needed: ${target:,.0f}")
st.markdown(f"### {status}")

# Optional: Upload intake Excel file
uploaded_file = st.file_uploader("📤 Upload Client Intake Excel (optional)", type=["xlsx"])
if uploaded_file:
    st.success("File uploaded. Net worth auto-import feature coming in v0.2.")
