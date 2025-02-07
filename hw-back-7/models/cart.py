from pydantic import BaseModel
from typing import List


class CartItem(BaseModel):
    flower_id: int
    name: str
    price: float
    quantity: int
