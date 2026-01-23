# 🤖 AI Chatbot Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Gemini API](https://img.shields.io/badge/Google-Gemini-8E75B2)

A powerful and user-friendly AI Chatbot built with **Python** and **Streamlit**, powered by **Google's Gemini API**. This project demonstrates how to create a conversational AI interface with real-time streaming responses and robust error handling.

## ✨ Features

- **🗣️ Natural Language Processing**: Uses Google's `gemini-flash-latest` model for high-quality responses.
- **⚡ Real-time Streaming**: Responses are streamed in real-time for a smooth user experience.
- **🎨 Clean & Modern UI**: Custom styled chat interface with avatar support and a polished design.
- **🛡️ Robust Error Handling**: Automatically handles API rate limits (429 errors) with exponential backoff and jitter.
- **🔌 Dual Architecture**: 
  - Works as a standalone Streamlit app.
  - Includes an optional **FastAPI** backend for decoupled deployments.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM**: [Google Gemini (Generative AI)](https://ai.google.dev/)
- **Backend (Optional)**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python 3

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Google Cloud Project with Gemini API access enabled
- An API Key from [Google AI Studio](https://aistudio.google.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Project chatbot"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

### Usage

**Run the Streamlit App (Default)**
To start the chatbot interface directly:
```bash
streamlit run streamlit_app.py
```
The app will open in your default browser at `http://localhost:8501`.

**(Optional) Run the FastAPI Backend**
If you want to run the separate API server:
```bash
python -m backend.main
```
The API will be available at `http://localhost:8000/docs`.

## 📂 Project Structure

```
├── streamlit_app.py   # Main frontend application
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (API Key)
└── backend/
    ├── llm_client.py # Logic for interacting with Gemini API
    ├── main.py       # FastAPI server implementation
    └── models.py     # Pydantic models for API
```

## 📸 Screenshots

*(Add screenshots of your application here to make your LinkedIn post pop!)*

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
