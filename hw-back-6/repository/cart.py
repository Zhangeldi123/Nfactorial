from pydantic import BaseModel
from typing import List
from models.cart import CartItem

class Cart(BaseModel):
    items: List[CartItem] = []
    
    def add_item(self, flower_id: int, name: str, price: float, quantity: int = 1):
        
        for item in self.items:
            if item.flower_id == flower_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(flower_id=flower_id, name=name, price=price, quantity=quantity))
    
    def get_total_price(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
    
    def to_dict(self):
        return [item.dict() for item in self.items]
    
    @staticmethod
    def from_dict(data: List[dict]):
        items = [CartItem(**item) for item in data]
        return Cart(items=items)