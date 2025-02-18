from sqlalchemy.orm import Session
from models.flower import Flower
from schemas.flower import FlowerRequest

class FlowerRepository:
    def create_flower(db: Session, flower_data: FlowerRequest) -> Flower:
        """Creates a new flower in the database."""
        new_flower = Flower(**flower_data.model_dump())
        db.add(new_flower)
        db.commit()
        db.refresh(new_flower)
        return new_flower

    def get_flower_by_id(db: Session, flower_id: int) -> Flower | None:
        """Retrieves a flower by its ID."""
        return db.query(Flower).filter(Flower.id == flower_id).first()

    def get_all_flowers(db: Session, skip: int = 0, limit: int = 10):
        """Retrieves a list of flowers with pagination."""
        return db.query(Flower).offset(skip).limit(limit).all()


    def update_flower(db: Session, flower_id: int, flower_data: FlowerRequest) -> Flower | None:
        """Updates an existing flower."""
        flower = db.query(Flower).filter(Flower.id == flower_id).first()
        if flower:
            for key, value in flower_data.model_dump().items():
                setattr(flower, key, value)
            db.commit()
            db.refresh(flower)
        return flower


    def delete_flower(db: Session, flower_id: int) -> bool:
        """Deletes a flower from the database."""
        flower = db.query(Flower).filter(Flower.id == flower_id).first()
        if flower:
            db.delete(flower)
            db.commit()
            return True
        return False
