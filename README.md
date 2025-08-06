🖤 AI-Powered RAG Chrome Extension
📌 Overview
This project is a Chrome Extension integrated with a FastAPI backend and LangChain RAG pipeline that allows you to query any webpage’s content directly from the browser.

Instead of manually reading through long articles or documentation, you can:

Load the webpage into the extension.

Ask a natural language question.

Get precise, webpage-specific answers instantly.

💡 Why This Project?
In today’s world, the internet is full of long-form content — technical documentation, research papers, news articles. While the information is valuable, finding exactly what you need can be time-consuming.

We built this project to bridge the gap between raw web content and fast, context-aware question answering. Using Retrieval-Augmented Generation (RAG), the extension retrieves only relevant chunks of the page and uses an LLM (DeepSeek) to generate concise answers.

⚙️ Tech Stack
FastAPI → Backend API

LangChain → RAG pipeline

DeepSeek LLM → Answer generation

ChromaDB → Vector storage

Python → Backend logic

HTML/CSS/JavaScript → Chrome Extension frontend

✨ Features
✔ Load and index any webpage in one click
✔ Ask natural language questions based on that page
✔ Black-themed UI similar to ChatGPT
✔ Medium-sized popup with chat history space
✔ Fast API calls with optimized retrieval

🚀 How to Run Locally
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
2️⃣ Install Dependencies
Make sure you have Python 3.10+ installed. Then:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Environment Variables
Create a .env file in the root directory and add:

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
Open Chrome → Go to chrome://extensions/

Enable Developer mode (top right)

Click Load unpacked

Select the extension/ folder from this project

📷 Usage
Enter a webpage URL in the extension popup

Wait until it shows "You can now ask questions"

Type your question in the black input box

View the answer in the chat interface

🛠 Possible Improvements
Add streaming responses for real-time answer generation

Deploy the backend to cloud for public use

Support multi-page context

