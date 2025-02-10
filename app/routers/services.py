from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_services():
    return {"status": "true", "message": "services route"}