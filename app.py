# app.py
import streamlit as st
from agent import generate_prompt

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Prompt Engineering Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Custom CSS for Beautiful UI
# ---------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1e1f26, #2a2d37);
}
.big-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    color: #ffffff;
}
.sub {
    color: #d1d1d1;
    font-size: 18px;
    text-align: center;
    margin-bottom: 30px;
}
.card {
    background: #2d2f3a;
    padding: 25px;
    border-radius: 15px;
    box-shadow: rgba(255,255,255,0.08) 0px 4px 10px;
    color: white;
}
.output-box {
    background: #111216;
    border-radius: 15px;
    padding: 25px;
    color: #00eaff;
    font-size: 18px;
    white-space: pre-wrap;
    border: 1px solid #00eaff55;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# UI Layout
# ---------------------------

st.markdown('<div class="big-title">🤖 AI Prompt Engineering Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Multi-Agent Prompt Builder powered by CrewAI + Groq</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📝 Enter Your Prompt Requirement")
user_input = st.text_area(
    "Prompt Requirement",
    placeholder="Example: Create a professional prompt for generating a business proposal summary...",
    height=250
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

if st.button("🚀 Generate AI Prompt", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Please enter a requirement!")
    else:
        with st.spinner("Agents are generating your perfect prompt..."):
            output = generate_prompt(user_input)

        st.subheader("✅ Final Optimized Prompt")
        st.markdown(f'<div class="output-box">{output}</div>', unsafe_allow_html=True)
