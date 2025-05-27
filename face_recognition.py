import cv2
import face_recognition
from database import add_face, get_all_faces
import numpy as np

def register_face(name):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            encoding = face_recognition.face_encodings(frame, face_locations)[0]
            add_face(name, encoding)
            break
        cv2.imshow("Register Face", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

def recognize_faces():
    known_faces = get_all_faces()
    known_encodings = [np.array(f['encoding']) for f in known_faces]
    known_names = [f['name'] for f in known_faces]

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, locations)

        for loc, enc in zip(locations, encodings):
            matches = face_recognition.compare_faces(known_encodings, enc)
            name = "Unknown"
            if True in matches:
                name = known_names[matches.index(True)]
            top, right, bottom, left = loc
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

        cv2.imshow("Live Recognition", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
