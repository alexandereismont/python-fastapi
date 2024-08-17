from pydantic import BaseModel


class ShopDto(BaseModel):
    id: int
    name: str
    description: str
    price: int
    stock: int
