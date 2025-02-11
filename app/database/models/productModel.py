from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated, List, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]

class ProductCreate(BaseModel):
    name: str = Field(max_length=100)
    price: float
    buy_price: float
    description: str = Field(max_length=500, default=None)
    file_id: str | None = None
    bucket_id: str | None = None

class ProductUpdate(BaseModel):
    name: str | None = Field(max_length=100, default=None)
    price: float | None = None
    buy_price: float | None = None
    description: str | None = Field(max_length=500, default=None)
    file_id: str | None = None
    bucket_id: str | None = None
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None
