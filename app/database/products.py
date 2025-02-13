from fastapi import HTTPException
from appwrite.exception import AppwriteException
from appwrite.id import ID
from app.config.appwrite import databases
from app.database.config import technical_solution_db_id, products_collection_id
from app.database.models import productModel

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