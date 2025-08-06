# 🧠 AI-Powered RAG Chrome Extension

A Chrome Extension integrated with a **FastAPI backend** and **LangChain RAG pipeline** that lets you **query any webpage’s content directly from your browser**.

Instead of manually reading through long articles or documentation, you can:
1. Load the webpage into the extension.
2. Ask a natural language question.
3. Get precise, webpage-specific answers instantly.

---

## 📌 Why This Project?
The internet is full of long-form content — technical documentation, research papers, news articles.  
While valuable, **finding exactly what you need can be time-consuming**.

This project bridges the gap between **raw web content** and **fast, context-aware question answering**.  
Using **Retrieval-Augmented Generation (RAG)**, it:
- Retrieves only the most relevant chunks of the page.
- Uses an **LLM (DeepSeek)** to generate concise answers.

---

## ⚙️ Tech Stack
**Backend:**
- FastAPI – API framework
- LangChain – RAG pipeline
- DeepSeek LLM – Answer generation
- ChromaDB – Vector storage
- Python – Backend logic

**Frontend:**
- HTML / CSS / JavaScript – Chrome Extension UI

---

## ✨ Features
- **Load & index any webpage** in one click
- **Ask natural language questions** about that page
- **Black-themed UI** similar to ChatGPT
- **Medium-sized popup** with chat history
- **Optimized retrieval** for faster, more relevant answers

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2️⃣ Install Dependencies
Make sure you have Python 3.10+ installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Environment Variables
Create a .env file in the root directory:

env
Copy
Edit
DEEPSEEK_API_KEY=your_api_key_here
4️⃣ Run the Backend
bash
Copy
Edit
uvicorn main:app --reload
The backend will run at:

cpp
Copy
Edit
http://127.0.0.1:8000
5️⃣ Load the Chrome Extension
Open Chrome and go to:

arduino
Copy
Edit
chrome://extensions/
Enable Developer mode (top right corner).

Click Load unpacked.

Select the extension/ folder from this project.

📷 Usage
Open any webpage.

Click the extension icon.

Wait for the message "You can now ask questions".

Type your question in the black input box.

View the AI-generated answer in the popup.

🛠 Possible Improvements
Add streaming responses for real-time answers.

Deploy backend to cloud hosting (Railway, Render) for public use.

Support multi-page context.

Improve response speed with model & retrieval optimizations.

Upgrade UI to Streamlit for richer interactions.
