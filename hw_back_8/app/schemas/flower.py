from pydantic import BaseModel
from typing import Optional


class FlowerRequest(BaseModel):
    name: str
    price: int 
    quantity: int

class FlowerResponse(BaseModel):
    id: int
    name: str
    price: int
    quantity: int

