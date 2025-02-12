from app.config.appwrite import account
from appwrite.exception import AppwriteException
from fastapi import HTTPException

async def create_email_password_session(email: str, password: str):
    try:
        result = account.create_email_password_session(
            email=email,
            password=password
        )
        return result
    except AppwriteException as e:
        print(e)
        raise HTTPException(status_code=404, detail=e.message)