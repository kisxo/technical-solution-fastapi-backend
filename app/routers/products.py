from fastapi import APIRouter, HTTPException, Response, status, File, UploadFile, Depends
from app.database import products
from app.database.models import productModel
from typing import Annotated
from app.accounts.utils import get_admin_user
from app.config.config import settings

router = APIRouter()

@router.get("/")
async def list_products():
    return {"status": "true", "data": await products.list_products()}

@router.post("/")
async def create_product(
    input_data: productModel.ProductCreate,
    response: Response,
    current_admin_user: Annotated[str, Depends(get_admin_user)]
):
    product = productModel.Product(
        name= input_data.name,
        price= input_data.price,
        buy_price= input_data.buy_price,
        icon_url= f"{settings.Appwrite_API_ENDPOINT}/storage/buckets/{input_data.bucket_id}/files/{input_data.file_id}/view?project={settings.APPWRITE_PROJECT_ID}"
    )

    created_product = await products.create_product(product)

    response.status_code = status.HTTP_201_CREATED
    return {"status": "true", "message": "Product added successfully", "data": created_product}

@router.patch("/{id}")
async def update_product(
    product_id: str,
    current_admin_user: Annotated[str, Depends(get_admin_user)],
    input_data: productModel.ProductUpdate,
):

    return {"status": "true", "data": ''}

@router.delete("/{id}")
async def delete_product(
    product_id: str,
    current_admin_user: Annotated[str, Depends(get_admin_user)],

):
    return {"status": "true", "data": await products.list_products()}