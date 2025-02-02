from pydantic import BaseModel

class Flower(BaseModel):
    name: str
    quantity: int
    price: float
    flowers_id: int | None = None
