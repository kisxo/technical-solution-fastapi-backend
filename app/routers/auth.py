from fastapi import APIRouter
from app.accounts.auth import create_email_password_session

router = APIRouter()

@router.post("/login")
async def login(email: str, password: str):
    created_session = await create_email_password_session(email, password)
    return {"status": "true", "message": "users route", 'data': created_session}