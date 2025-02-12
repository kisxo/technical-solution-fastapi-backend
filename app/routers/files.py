from fastapi import APIRouter, Response, status, File, UploadFile, Depends
from app.storage import fileUtils
from app.accounts.utils import get_admin_user
from typing import Annotated

router = APIRouter()

@router.post("/")
async def create_file(
    response: Response,
    current_admin_user: Annotated[str, Depends(get_admin_user)],
    file: UploadFile = File(),
):
    
    created_file_data = await fileUtils.create_file(file.file.read())

    response.status_code = status.HTTP_201_CREATED
    return {"status": "true", "message": "File created successfully", "data": created_file_data}