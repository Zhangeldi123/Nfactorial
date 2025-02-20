from fastapi import APIRouter, Depends, Form, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from hw_back_8.app.database import get_db
from fastapi.templating import Jinja2Templates
from repository.flower import FlowerRepository
from schemas.user import UserResponse
from datetime import datetime, timedelta, timezone
from schemas.user import UserCreate
from schemas.flower import FlowerRequest
from schemas.flower import FlowerResponse
import jwt
import os

flower_router = APIRouter(prefix="/flowers", tags=["flower"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
template = Jinja2Templates(directory="templates")

@flower_router.get("/")
def get_all_flowers(request: Request, db: Session = Depends(get_db), page: int = 1, per_page: int = 5):
    flowers = FlowerRepository.get_all_flowers(db, skip=(page - 1) * per_page, limit=per_page)

    next_page = page + 1 if len(flowers) == per_page else None
    previous_page = page - 1 if page > 1 else None

    return template.TemplateResponse(
        "flowers.html",
        {
            "request": request,
            "flowers": flowers,
            "next_page": next_page,
            "previous_page": previous_page,
            "per_page": per_page
        }
    )



@flower_router.post('/')
def create_flower(request: Request, db: Session = Depends(get_db), name: str = Form(...), price: int = Form(...), quantity: int = Form(...)):
    new_flower = FlowerRepository.create_flower(db, FlowerRequest(name=name, price=price, quantity=quantity))
    return RedirectResponse(url="/flowers", status_code=303)

