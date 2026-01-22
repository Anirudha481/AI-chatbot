import os
import time
import random
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_api_key():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except:
        pass
    return os.getenv("GEMINI_API_KEY")

API_KEY = get_api_key()
if API_KEY:
    genai.configure(api_key=API_KEY)

def get_chat_response(message: str, stream: bool = False):
    if not API_KEY:
        err = "Error: GEMINI_API_KEY not found."
        if stream: yield err
        else: return err
        return

    # Reverting to the only model that worked (even if low quota)
    model_name = "gemini-flash-latest"
    
    max_retries = 3
    base_delay = 1
    
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel(model_name)
            if stream:
                response = model.generate_content(message, stream=True)
                for chunk in response:
                     if chunk.text:
                        yield chunk.text
                return
            else:
                response = model.generate_content(message)
                return response.text
        except Exception as e:
            error_str = str(e)
            if ("429" in error_str or "Quota" in error_str) and attempt < max_retries - 1:
                # Calculate delay with exponential backoff and jitter
                delay = (base_delay * (2 ** attempt)) + (random.randint(0, 1000) / 1000)
                time.sleep(delay)
                continue
            elif "429" in error_str or "Quota" in error_str:
                 friendly_msg = "?? **Daily Quota Exceeded**\n\nYou have used your free usage limit for today. We retried a few times but the API is still busy. Please try again later."
                 if stream: yield friendly_msg
                 else: return friendly_msg
                 return
            else:
                err_msg = f"Error ({model_name}): {error_str}"
                if stream: yield err_msg
                else: return err_msg
                return
