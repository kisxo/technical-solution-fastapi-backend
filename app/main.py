from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, products, services
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

@app.get("/", name= "Api Status")
async def root():
    return {"status":"true", "message": " Technical Solution Api server is running"}

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)

app.include_router(
    products.router,
    prefix="/products",
    tags=["products"],
)

app.include_router(
    services.router,
    prefix="/services",
    tags=["services"],
)