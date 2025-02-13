from fastapi import APIRouter
from app.database.models import authModel
from app.accounts.users import create_email_account

router = APIRouter()

@router.post("/")
async def create_user(
    user: authModel.CreateEmailPasswordAccountModel
):
    created_user = await create_email_account(user)
    return {"status": "true", "message": "users route", 'data': created_user}