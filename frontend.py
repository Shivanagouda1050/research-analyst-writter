import streamlit as st
import time
from langchain_core.messages import HumanMessage
from main import graph  # 👈 import your backend graph

# =============================================
# ⚙️ Streamlit Config
# =============================================
st.set_page_config(
    page_title="MindMesh 💫",
    page_icon="🧠",
    layout="wide",
)

# =============================================
# 🌈 Dark Futuristic Neon Theme
# =============================================
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #0A0A1F 0%, #101030 45%, #050515 100%);
        color: #EAEAEA;
        font-family: 'Poppins', sans-serif;
    }
    [data-testid="stSidebar"] {
        background: rgba(18, 18, 40, 0.9);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    h1 {
        color: #A29BFE;
        text-shadow: 0 0 10px rgba(162,155,254,0.4);
        font-size: 1.8rem !important;
    }
    h2, h3, h4 {
        color: #B8A9FF;
    }
    .stButton>button {
        background: linear-gradient(90deg, #8E2DE2, #4A00E0);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1.3rem;
        font-weight: 600;
        box-shadow: 0 0 14px rgba(138, 43, 226, 0.5);
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.07);
        box-shadow: 0 0 22px rgba(138, 43, 226, 0.9);
    }
    .output-box {
        background: rgba(255,255,255,0.06);
        padding: 1.2rem;
        border-radius: 15px;
        margin-top: 1.5rem;
        border-left: 3px solid #8E2DE2;
        font-size: 0.95rem;
        line-height: 1.6;
        color: #E0E0FF;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #7A7A9A;
        margin-top: 2rem;
    }
    .logo {
        font-weight: 700;
        font-size: 1.3rem;
        background: -webkit-linear-gradient(45deg, #8E2DE2, #4A00E0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .agent-box {
        background: rgba(255,255,255,0.05);
        padding: 0.8rem;
        border-radius: 10px;
        margin-top: 0.8rem;
        border-left: 3px solid #6C63FF;
        color: #C9C9FF;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# 🌟 Sidebar
# =============================================
with st.sidebar:
    st.markdown("<div class='logo'>🧠 MindMesh</div>", unsafe_allow_html=True)
    st.markdown("### ⚙️ Settings")
    st.info("Powered by LangGraph + Groq LLaMA-3.1", icon="🤖")
    st.markdown("🌐 *Research. Analyze. Write. Across any domain.*")
    st.caption("Made with ⚡ by Shiva")

# =============================================
# 🧠 Main Header
# =============================================
st.title("💫 MindMesh — Interlinked AI Minds for Every Domain")
st.write(
    "Ask *anything* — from technology and business to health or education. "
    "Let **MindMesh** research, analyze, and write your perfect report 🚀"
)

# =============================================
# 🧾 Input Section
# =============================================
user_input = st.text_area(
    "💬 What topic should MindMesh explore?",
    placeholder="e.g., The impact of AI on education systems",
    height=150,
)

run_btn = st.button("⚡ Launch MindMesh Workflow")

# =============================================
# 🚀 Run Multi-Agent Workflow
# =============================================
if run_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter a topic or question 😎")
    else:
        st.markdown("### 🤖 Activating MindMesh Agents...")
        progress = st.progress(0)

        initial_state = {
            "messages": [HumanMessage(content=user_input)],
            "next_agent": "supervisor",
            "research_data": "",
            "analysis": "",
            "final_report": "",
            "task_complete": False,
            "current_task": ""
        }

        with st.spinner("🧩 Agents are collaborating..."):
            agents = [
                ("📚 Researcher", "Gathering data and sources..."),
                ("📊 Analyst", "Finding insights and key trends..."),
                ("✍️ Writer", "Compiling and formatting the final report...")
            ]

            for i, (agent, msg) in enumerate(agents):
                time.sleep(1.2)
                st.markdown(f"<div class='agent-box'>{agent}: {msg}</div>", unsafe_allow_html=True)
                progress.progress((i + 1) * 30)

            response = graph.invoke(initial_state)
            progress.progress(100)

        st.balloons()
        st.success("✨ MindMesh has completed your task!")
        st.markdown("### 🪄 Final Report")
        st.markdown(f"<div class='output-box'>{response['final_report']}</div>", unsafe_allow_html=True)

# =============================================
# 🧡 Footer
# =============================================
st.markdown("<div class='footer'>Built with 💜 by Shiva • MindMesh Edition ⚡</div>", unsafe_allow_html=True)
