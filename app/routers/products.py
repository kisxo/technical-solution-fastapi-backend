from fastapi import APIRouter
from app.database import products
router = APIRouter()

@router.get("/")
async def list_products():
    return {"status": "true", "data": await products.list_products()}