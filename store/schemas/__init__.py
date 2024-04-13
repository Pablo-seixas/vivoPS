# schemas/__init__.py
from pydantic import BaseModel


# Definição do esquema de validação ProductSchema
class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
