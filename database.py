from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["face_rag"]
faces = db["faces"]

def add_face(name, encoding):
    face_data = {
        "name": name,
        "encoding": encoding.tolist(),
        "timestamp": datetime.now()
    }
    faces.insert_one(face_data)

def get_all_faces():
    return list(faces.find())

def get_last_registered():
    return faces.find().sort("timestamp", -1).limit(1)[0]
