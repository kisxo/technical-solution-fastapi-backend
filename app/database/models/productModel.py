from pydantic import BaseModel, BeforeValidator, Field
from typing import Annotated, List, Optional

PyObjectId = Annotated[str, BeforeValidator(str)]

class ProductBase(BaseModel):
    name: str = Field(max_length=100)
    price: float
    buy_price: float
    description: str = Field(max_length=500, default=None)

class Product(ProductBase):
    icon_url: str

class ProductCreate(ProductBase):
    file_id: str | None = None
    bucket_id: str | None = None

class ProductUpdate(ProductBase):
    name: str | None = Field(max_length=100, default=None)
    price: float | None = None
    buy_price: float | None = None
    icon_url: str | None = None

class ProductUpdateInput(ProductBase):
    name: str | None = Field(max_length=100, default=None)
    price: float | None = None
    buy_price: float | None = None
    file_id: str | None = None
    bucket_id: str | None = None
