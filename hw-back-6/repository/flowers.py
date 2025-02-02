from models.flowers import Flower
from typing import List

class FlowersRepository:
    def __init__(self):
        self.flowers: List[Flower] = [Flower(name="Rose", quantity=10, price=5.0, flowers_id=1), Flower(name="Tulip", quantity=5, price=3.0, flowers_id=2)]
    
    def add_flower(self, name: str, quantity: int, price: float):
        self.flowers.append(Flower(name=name, quantity=quantity, price=price, flowers_id = len(self.flowers) + 1))

    def get_flower(self, name: str):
        for flower in self.flowers:
            if flower.name == name:
                return flower
        return None
    
    def get_all_flowers(self):
        return self.flowers
    
    def get_by_id(self, flowers_id: int):
        for flower in self.flowers:
            if flower.flowers_id == flowers_id:
                return flower
        return None