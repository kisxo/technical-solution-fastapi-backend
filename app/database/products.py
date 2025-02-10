from app.config.appwrite import databases
from app.database.config import technical_solution_db_id, products_collection_id

async def list_products():
    result = databases.list_documents(
        database_id = technical_solution_db_id,
        collection_id = products_collection_id
    )

    return result['documents']

async def get_product(productId: str):
    result = databases.get_document(
        database_id = technical_solution_db_id,
        collection_id = products_collection_id,
        document_id= productId,
    )
    return result