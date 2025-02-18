from fastapi import Depends, HTTPException, Request
import logging
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from database import get_db
import jwt
from datetime import datetime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UsersRepository:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        user = User(username=user_data.username, email=user_data.email, password=user_data.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()


    @staticmethod
    def get_current_user(request: Request, db: Session = Depends(get_db)):
        """Получить текущего пользователя из токена (поддерживает куки)."""
        # Попробуем извлечь токен из куки
        token = request.cookies.get("access_token")
        
        if not token:
            logging.error("Токен не найден в куках")
            raise HTTPException(status_code=401, detail="Нет access token в запросе")
        
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            user_id = payload.get("user_id")
            
            if user_id is None:
                logging.error("ID пользователя не найдено в токене")
                raise HTTPException(status_code=401, detail="Неверные данные пользователя")
            
            # Ищем пользователя по ID
            user = db.query(User).filter(User.id == user_id).first()
            
            if user is None:
                logging.error(f"Пользователь не найден по ID {user_id}")
                raise HTTPException(status_code=401, detail="Пользователь не найден")
            
            return user
        except (jwt.ExpiredSignatureError, jwt.DecodeError) as e:
            logging.error(f"Ошибка при декодировании JWT: {str(e)}")
            raise HTTPException(status_code=401, detail="Неверный или просроченный токен")

    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        user = UsersRepository.get_user_by_email(db, email)
        if not user:
            return False
        if not user.password == password:
            return False
        return user

    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()