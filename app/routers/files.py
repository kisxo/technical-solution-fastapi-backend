from fastapi import APIRouter, Response, status, File, UploadFile
from app.storage import fileUtils

router = APIRouter()

@router.post("/")
async def create_file(
    response: Response,
    file: UploadFile = File(),
):
    
    created_file_data = await fileUtils.create_file(file.file.read())

    response.status_code = status.HTTP_201_CREATED
    return {"status": "true", "message": "File created successfully", "data": created_file_data}