from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    root_path="/api",
)
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "https://magicminute.online",
    "https://www.magicminute.online"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status":"true", "message": " Technical Solution Api server is running"}