import streamlit as st
import requests

ST_API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title="Intelligent AI", page_icon="??")

st.title("Intelligent AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        try:
            response = requests.post(ST_API_URL, json={"message": prompt})
            if response.status_code == 200:
                bot_response = response.json()["response"]
                st.chat_message("assistant").markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Connection error: {e}")
