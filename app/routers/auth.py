from typing import Annotated
from fastapi import APIRouter, Response, status, Depends
from app.accounts.auth import create_email_password_session
from app.database.models import authModel
from app.accounts.utils import get_current_user, get_admin_user


router = APIRouter()

@router.post("/token")
async def generate_auth_token(
    data: authModel.CreateEmailPasswordSession,
    response: Response
):

    created_session = await create_email_password_session(data.email, data.password)

    response.status_code = status.HTTP_200_OK
    response.set_cookie("session_token", created_session["secret"])
    return {"status": "true", "message": "Login Successful"}

@router.delete("/token")
async def delete_session(
    response: Response
):

    response.status_code = status.HTTP_200_OK
    response.delete_cookie("session_token")
    return {"status": "true", "message": "Logout Successful"}

@router.get("/user")
async def check_auth_status_and_get_user(
    current_user: Annotated[str, Depends(get_current_user)]
):

    return {"status": "true", "message": "Authorized", 'data': current_user}