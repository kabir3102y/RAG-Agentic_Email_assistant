import streamlit as st
from email_generator import generate_email
from review_agent import review_email
from email_sender import send_email

st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

/* Main Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#312e81);
    color:white;
}

/* Hide Streamlit menu and footer */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:#7dd3fc;
    margin-bottom:10px;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

/* Text Inputs */
.stTextInput input,
.stTextArea textarea{
    background-color:#1e293b;
    color:white;
    border-radius:12px;
    border:2px solid #38bdf8;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"]{
    background-color:#1e293b;
    border-radius:12px;
}

/* Button */
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    padding:12px;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#3b82f6,#9333ea);
}

/* Success Box */
.stSuccess{
    border-radius:12px;
}

/* Text Area Output */
textarea{
    border-radius:12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- Heading ----------
st.markdown(
    "<div class='title'>🤖 AI Email Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Powered by Ollama • RAG • Multi-Agent AI</div>",
    unsafe_allow_html=True
)

# ---------- Inputs ----------
subject = st.text_input("📌 Email Subject")

purpose = st.text_area(
    "📝 Purpose of Email",
    height=150
)

tone = st.selectbox(
    "🎭 Select Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Casual"
    ]
)

receiver = st.text_input("📧 Receiver Email Address")

# ---------- Generate ----------
if st.button("🚀 Generate Email"):

    if subject and purpose:

        with st.spinner("🤖 AI Agents are working..."):

            email_type, email_body = generate_email(
                subject,
                purpose,
                tone
            )

            reviewed_email = review_email(email_body)

            st.session_state["email_type"] = email_type
            st.session_state["email_body"] = reviewed_email

    else:
        st.warning("Please enter Subject and Purpose.")

# ---------- Output ----------
if "email_body" in st.session_state:

    st.success(
        f"🤖 Agent Decision : {st.session_state['email_type']}"
    )

    st.text_area(
        "📨 Final Reviewed Email",
        st.session_state["email_body"],
        height=320
    )

    if st.button("📤 Send Email"):

        if receiver:

            result = send_email(
                receiver,
                subject,
                st.session_state["email_body"]
            )

            st.success(result)

        else:
            st.warning("Please enter the receiver email.")