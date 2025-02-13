from fastapi import APIRouter, Response, status
from app.database.models import authModel
from app.accounts.users import create_email_account

router = APIRouter()

@router.post("/")
async def create_user(
    user: authModel.CreateEmailPasswordAccountModel,
    response: Response
):
    created_user = await create_email_account(user)
    response.status_code = status.HTTP_201_CREATED
    return {"status": "true", "message": "users route", 'data': created_user}