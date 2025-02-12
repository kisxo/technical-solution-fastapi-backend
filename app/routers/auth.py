from fastapi import APIRouter, Response, status
from app.accounts.auth import create_email_password_session
from app.database.models import authModel

router = APIRouter()

@router.post("/login")
async def login(
    data: authModel.CreateEmailPasswordSession,
    response: Response
):

    created_session = await create_email_password_session(data.email, data.password)

    response.status_code = status.HTTP_200_OK
    response.set_cookie("session", created_session["secret"])
    return {"status": "true", "message": "Login Successful"}