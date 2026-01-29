# Project Report: AI Chatbot Assistant

**Submitted by:** Anirudha TH
**Date:** 2026-01-29

## 1. System Architecture

The project follows a modular Client-Server architecture, designed for flexibility and ease of deployment.

### Components:
*   **Frontend (User Interface):** Built with **Streamlit**. It handles user input (text), displays the chat history, and renders Markdown responses. It manages the session state for chat history.
*   **Backend (Logic Layer):**
    *   **Direct Integration (Default):** The Streamlit app communicates directly with the Google Gemini API using the \google-generativeai\ library.
    *   **FastAPI Service (Optional):** A separate backend service is provided in the \ackend/\ directory, exposing a REST API. This allows for decoupling the UI from the logic if scaling is required.
*   **External Service (LLM):** **Google Gemini API** (\gemini-flash-latest\ or compatible models) provides the generative AI capabilities.

### Data Flow:
1.  User inputs text in Streamlit.
2.  Input is sent to the LLM Client (either internal or via FastAPI).
3.  Client sends request to Google Gemini API.
4.  Gemini API streams the response back.
5.  Streamlit updates the UI in real-time as chunks of text arrive.

## 2. Design Decisions

### A. Tech Stack Selection
*   **Python:** Chosen for its rich ecosystem in AI and rapid prototyping capabilities.
*   **Streamlit:** Selected for the frontend to enable rapid development of a data-centric UI without complex Javascript frameworks.
*   **Google Gemini:** Chosen as the LLM provider for its high performance and generous free tier (Flash models).

### B. Implementation Details
*   **Streaming Responses:** To improve perceived latency, responses are streamed. The user sees text appearing immediately rather than waiting for the full generation to complete.
*   **Robust Error Handling:** The application includes specific handling for \429 Too Many Requests\ errors. It implements an exponential backoff strategy to retry requests when the API quota is temporarily exceeded.
*   **Model Fallback/Selection:** The code is designed to use \gemini-flash-latest\ but can be easily configured for other models.

## 3. Screenshots

1.  **Chat Interface:**
    ![Chat Interface](screenshot.png)

## 4. Steps to Run the Project

### Prerequisites
*   Python 3.8+ installed.
*   A Google Cloud API Key for Gemini.

### Installation

1.  **Clone the repository:**
    \\\ash
    git clone https://github.com/YOUR_USERNAME/Project-chatbot.git
    cd "Project chatbot"
    \\\

2.  **Install Dependencies:**
    \\\ash
    pip install -r requirements.txt
    \\\

3.  **Configuration:**
    *   Create a file named \.env\ in the root directory.
    *   Add your API key:
        \\\env
        GEMINI_API_KEY=your_actual_api_key_here
        \\\

### Execution

**Option 1: Run Streamlit App (Simplest)**
\\\ash
streamlit run streamlit_app.py
\\\
Access the app at \http://localhost:8501\.

**Option 2: Run FastAPI Backend (Advanced)**
\\\ash
# Terminal 1: Backend
python -m backend.main

# Terminal 2: Frontend (configured to use backend)
# (Requires modifying streamlit_app.py to point to backend URL if not default)
\\\

## 5. Conclusion
This project demonstrates a functional, modern AI assistant capable of maintaining context and handling real-world API constraints.
