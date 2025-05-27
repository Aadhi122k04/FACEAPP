from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import ask_gemini
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = ask_gemini(data)
        await websocket.send_text(response)

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)
