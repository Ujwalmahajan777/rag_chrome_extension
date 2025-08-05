import os
import shutil
import hashlib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from parser_module import web_loader, text_splitter, get_vector_store
from rag_chain import get_rag_chain

last_loaded_url = None  
CHROMA_BASE_DIR = "chroma_dbs"  # New base folder for all URLs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

class ChatRequest(BaseModel):
    query: str

def url_to_folder(url: str) -> str:
    """Generate a unique folder path for each URL."""
    hashed = hashlib.md5(url.encode()).hexdigest()
    return os.path.join(CHROMA_BASE_DIR, hashed)

@app.get("/")
def root():
    return {"message": "RAG API is running"}

@app.post("/set_url")
def set_url(request: URLRequest):
    global last_loaded_url

    folder = url_to_folder(request.url)

    if request.url != last_loaded_url:
        # Create base dir if not exists
        os.makedirs(CHROMA_BASE_DIR, exist_ok=True)

        # Remove old data for this URL only
        if os.path.exists(folder):
            shutil.rmtree(folder)

        print(f"Loading content from: {request.url} ...")
        docs = web_loader(request.url)
        chunks = text_splitter(docs)
        get_vector_store(chunks, persist_directory=folder)  # Pass folder

        last_loaded_url = request.url
        return {"message": f"Content loaded for: {request.url}"}

    return {"message": "URL already loaded, skipping reload"}

@app.post("/chat")
def chat(request: ChatRequest):
    if not last_loaded_url:
        raise HTTPException(status_code=400, detail="No webpage loaded yet. Please set a URL first.")

    folder = url_to_folder(last_loaded_url)
    if not os.path.exists(folder):
        raise HTTPException(status_code=400, detail="Vector store not found for the loaded URL.")

    rag_chain = get_rag_chain(persist_directory=folder)
    answer = rag_chain.invoke(request.query)
    return {"response": answer}
