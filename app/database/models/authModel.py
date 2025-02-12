from pydantic import BaseModel, BeforeValidator, Field

class CreateEmailPasswordSession(BaseModel):
    email: str = Field()
    password: str = Field(min_length=8)