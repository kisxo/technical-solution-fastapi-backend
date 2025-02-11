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
    result = databases.get_document(
        database_id = technical_solution_db_id,
        collection_id = products_collection_id,
        document_id= product_id,
    )
    return result

async def create_product(product: productModel.ProductCreate):
    try:
        result = databases.create_document(
            database_id = technical_solution_db_id,
            collection_id = products_collection_id,
            document_id = ID.unique(),
            data = product.model_dump_json()
        )
        return result
    except AppwriteException as e:
        print(e)
        raise HTTPException(status_code=404, detail=e.message)