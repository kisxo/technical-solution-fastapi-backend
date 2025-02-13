from fastapi import HTTPException
from appwrite.exception import AppwriteException
from appwrite.id import ID
from app.config.appwrite import account
from app.database.models import authModel

async def create_email_account(
    user: authModel.CreateEmailPasswordAccountModel
):
    try:
        result = account.create(
            user_id = ID.unique(),
            email = user.email,
            password = user.password,
        )
        return result
    except AppwriteException as e:
        raise HTTPException(status_code=e.code, detail=e.message)


