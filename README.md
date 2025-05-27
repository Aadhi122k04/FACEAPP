# 1.🎭 Face Recognition Platform with Real-Time AI Q&A using RAG which was given by the company Katomaran as a hackathon task :url:  https://katomaran.com

This project is a full-stack application that combines:
- **Face Recognition** with a Python FastAPI backend
- **React** frontend interface
- **RAG-based AI chatbot** using LangChain, FAISS, and the Gemini API

## 2.🧱 Project Structure

<pre> ``` face-rag-app/ │ ├── backend/ # Python Face recognition + RAG │ ├── face_recognition.py │ ├── rag_engine.py │ ├── app.py # FastAPI for REST and WebSocket │ ├── database.py │ └── requirements.txt │ ├── frontend/ # React app │ ├── public/ │ ├── src/ │ │ ├── components/ │ │ │ ├── RegistrationTab.jsx │ │ │ ├── RecognitionTab.jsx │ │ │ └── ChatWidget.jsx │ │ ├── App.js │ │ └── index.js │ └── package.json │ └── README.md ``` </pre>

3.Make sure requirements.txt includes:
fastapi
uvicorn
python-multipart
face_recognition
pillow
sqlalchemy
google-generativeai
langchain
faiss-cpu

4.Start the FastAPI server
    uvicorn main:app --reload
5.💻 Frontend Setup (React)
     Commands:

       cd ../frontend
       npm install
       npm start
6.🔗 Connecting Frontend to Backend
     Commands:
          fetch('http://127.0.0.1:8000/api/hello')
         .then(res => res.json())
         .then(data => console.log(data));

7.🚀 Deployment Tips (Optional)
You can deploy FastAPI on Render, Vercel, or Railway

React frontend can be hosted on Netlify or Vercel

Use Docker for containerization (optional)         
         

    



