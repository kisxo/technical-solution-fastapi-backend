from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_products():
    return {"status": "true", "message": "products route"}