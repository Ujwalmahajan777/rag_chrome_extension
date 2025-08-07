# 🧠 AI-Powered Chrome Extension using RAG (Retrieval-Augmented Generation)

This project is a lightweight **Chrome Extension** powered by a custom **RAG-based assistant**. It enables users to **chat with any webpage** by extracting its content and querying a backend LLM pipeline built using **LangChain**, **FastAPI**, and **Chroma vector store**.

---

## 🚀 Key Features

- 🔍 Extracts content from the currently viewed webpage.
- 💬 Lets users ask questions based on the webpage.
- ⚡ RAG pipeline with HuggingFace embeddings, DeepSeek/Groq models, and Contextual Compression Retriever.
- 📤 Uploads content to backend and fetches LLM-powered answers in real time.
- 🧩 Frontend built using JavaScript & HTML/CSS (Chrome Extension).

---

## 📂 Tech Stack

| Layer     | Tech Used                                                                 |
|-----------|---------------------------------------------------------------------------|
| Frontend  | Chrome Extension (JavaScript, HTML, CSS)                                  |
| Backend   | Python, FastAPI                                                           |
| LLM Stack | LangChain, DeepSeek (or Groq), HuggingFace Embeddings, Chroma Vector DB  |

---

## 🔧 Installation

### 1. Clone the repository

git clone https://github.com/ujwalmahajan/rag-chrome-extension.git
cd rag-chrome-extension

2. Setup Python backend
cd backend  # Navigate to the FastAPI backend folder

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

3. Run FastAPI backend
uvicorn main:app --reload
Backend will run at http://localhost:8000.

🧠 How It Works
The Content Script extracts clean text from the current webpage.

On clicking the extension icon, the scraped content is sent to the backend (/upload_content).

User enters a question → sent to the backend's /chat endpoint.

The RAG chain processes the query and returns a contextual answer.

The response is displayed inside the popup chat window.

🔗 GitHub Repository
👉 https://github.com/ujwalmahajan/rag-chrome-extension

📌 Future Scope
 Add multi-website memory support

 Integrate LangGraph for multi-step agent flows

 Improve UI and add message history

 Optimize document chunking and compression further

🙌 Contribution
If you'd like to contribute or raise an issue, feel free to fork the repo or create a PR. Star the repo if you found it helpful!



