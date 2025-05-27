import google.generativeai as genai
from database import get_all_faces, get_last_registered
from datetime import datetime
import faiss
import numpy as np

genai.configure(api_key="AIzaSyBGNDmHMSy7eAZpazduEBF0nhXAX1sNugU")

def prepare_docs():
    docs = []
    faces = get_all_faces()
    for f in faces:
        text = f"{f['name']} was registered at {f['timestamp']}."
        docs.append(text)
    return docs

def ask_gemini(query):
    context = "\n".join(prepare_docs())
    prompt = f"Context: {context}\n\nUser Question: {query}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
