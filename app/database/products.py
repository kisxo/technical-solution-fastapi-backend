import json

from fastapi import HTTPException
from appwrite.exception import AppwriteException
from appwrite.id import ID
from app.config.appwrite import databases
from app.database.config import technical_solution_db_id, products_collection_id
from app.database.models import productModel
from app.config.config import settings

async def list_products():
    result = databases.list_documents(
        database_id = technical_solution_db_id,
        collection_id = products_collection_id
    )
    return result['documents']

async def get_product(product_id: str):
    try:
        result = databases.get_document(
            database_id=technical_solution_db_id,
            collection_id=products_collection_id,
            document_id=product_id,
        )
        return result
    except AppwriteException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

async def create_product(product: productModel.Product):
    try:
        result = databases.create_document(
            database_id = technical_solution_db_id,
            collection_id = products_collection_id,
            document_id = ID.unique(),
            data = product.model_dump_json()
        )
        return result
    except AppwriteException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

async def update_product(
        product_id: str,
        input_data: productModel.ProductUpdateInput
):
    try:
        old_product = await get_product(product_id)

        product = productModel.ProductUpdate()

        if input_data.name:
            product.name = input_data.name
        else:
            product.name = old_product['name']

        if input_data.price:
            product.price = input_data.price
        else:
            product.price = old_product['price']

        if input_data.buy_price:
            product.buy_price = input_data.buy_price
        else:
            product.buy_price = old_product['buy_price']

        if input_data.description:
            product.description = input_data.description
        else:
            product.description = old_product['description']

        if input_data.bucket_id and input_data.file_id:
            product.icon_url = f"{settings.Appwrite_API_ENDPOINT}/storage/buckets/{input_data.bucket_id}/files/{input_data.file_id}/view?project={settings.APPWRITE_PROJECT_ID}"
        else:
            product.icon_url = old_product['icon_url']

        result = databases.update_document(
            database_id = technical_solution_db_id,
            collection_id = products_collection_id,
            document_id = product_id,
            data=product.model_dump_json(),
        )
        return result
    except AppwriteException as e:
        raise HTTPException(status_code=e.code, detail=e.message)

async def delete_product(product_id: str):
    try:
        result = databases.delete_document(
            database_id = technical_solution_db_id,
            collection_id = products_collection_id,
            document_id = product_id
        )
        return result
    except AppwriteException as e:
        raise HTTPException(status_code=e.code, detail=e.message)