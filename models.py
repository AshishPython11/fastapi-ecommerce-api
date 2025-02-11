from sqlmodel import SQLModel, Field
from typing import Optional, List

#Pydantic model for validaton
class ProductCreate(SQLModel):
    name: str
    description: str
    price: float

class ProductUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class OrderCreate(SQLModel):
    customer_id: int
    product_ids: List[int] 

class OrderUpdate(SQLModel):
    status: str

#ORM model
class Product(ProductCreate, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class Order(OrderCreate, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_ids: str 
    status: str = "pending"
