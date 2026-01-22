import streamlit as st
from backend.llm_client import get_chat_response

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Assistant",
    page_icon="page_icon.png",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    /* Gradient Title */
    .title-text {
        background: linear-gradient(45deg, #4285f4, #9b72cb, #d96570);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: bold;
        padding-bottom: 20px;
    }
    
    /* Chat Bubble Styling */
    .stChatMessage {
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    
    /* Main container padding */
    .main {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### About")
    st.info(
        "This AI assistant is powered by **Google Gemini**.\n\n"
        "It can help you with coding, writing, and general questions."
    )

# --- Main Interface ---

# Custom Title
st.markdown('<p class="title-text">AI Assistant</p>', unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant. How can I help you today? \U0001F44B"} # Waving Hand
    ]

# Display Chat History with Avatars
for message in st.session_state.messages:
    if message["role"] == "user":
        avatar = "\U0001F464"  # Silhouette
    else:
        avatar = "\U0001F916"  # Robot
    
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Chat Input & Response Logic
if prompt := st.chat_input("Ask me anything..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="\U0001F464"): # Silhouette
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant", avatar="\U0001F916"): # Robot
        try:
            # Use st.write_stream to automatically handle the generator
            stream = get_chat_response(prompt, stream=True)
            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error: {e}")
