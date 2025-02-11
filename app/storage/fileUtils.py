from fastapi import HTTPException, File, UploadFile
from app.config.appwrite import storage
from app.storage.config import technical_solution_bucket_id
from appwrite.id import ID
from appwrite.exception import AppwriteException
from app.config.config import settings
from appwrite.input_file import InputFile

async def create_file(file):
    try:
        result = storage.create_file(
            bucket_id = technical_solution_bucket_id,
            file_id = ID.unique(),
            file = InputFile.from_bytes(file, ID.unique()),
            permissions = ['read("any")'] # optional
        )
        # generate file url and append it to result
        result['file_url'] = (f"{settings.Appwrite_API_ENDPOINT}/storage/buckets/{technical_solution_bucket_id}/files/{result['$id']}/view?project={settings.APPWRITE_PROJECT_ID}")

        return result
    except AppwriteException as e:
        print(e)
        raise HTTPException(status_code=404, detail=e.message)