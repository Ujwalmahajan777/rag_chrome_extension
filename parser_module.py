from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os, re
from langchain.schema import Document

os.environ["USER_AGENT"] = "my-url-bot/1.0"


def clean_text(docs):
    cleaned_docs = []
    for doc in docs:
        text = doc.page_content
        text = re.sub(r'\[\d+\]', '', text)  # remove citations
        text = re.sub(r'\s+', ' ', text)     # normalize spaces
        text = re.sub(r'(?i)edit section', '', text)  # remove edit prompts
        text = text.strip()
        cleaned_docs.append(Document(page_content=text, metadata=doc.metadata))
    return cleaned_docs

def web_loader(url: str):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return clean_text(docs)  # cleaned before splitting

def text_splitter(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=("\n\n", "\n", ".", " ")
    )
    return splitter.split_documents(docs)

def get_vector_store(texts,persist_directory):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    vector_store.add_documents(texts)
    return vector_store
