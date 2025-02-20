from fastapi import APIRouter, Request, Response, Form, Depends, Cookie
from fastapi.templating import Jinja2Templates
from repository.flower import FlowerRepository
from repository.cart import CartRepository
from hw_back_8.app.database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
import json


cart_router = APIRouter(prefix="/cart", tags=["cart"])
templates = Jinja2Templates(directory="templates")

@cart_router.post("/items")
def add_to_cart(request: Request, flower_id: int = Form(...), cart: str = Cookie(default="[]")):
    cart_items = json.loads(cart)
    cart_items.append(flower_id)
    new_cart = json.dumps(cart_items)

    response = RedirectResponse(url="/cart/items", status_code=303)
    response.set_cookie(key="cart", value=new_cart)
    return response

@cart_router.get("/items")
def get_cart_items(request: Request, db: Session = Depends(get_db)):
    cart_item_ids = CartRepository.get_cart(request)
    
    # Retrieve flower details from DB
    flowers = [FlowerRepository.get_flower_by_id(db, fid) for fid in cart_item_ids if fid]
    total_price = sum(flower.price for flower in flowers if flower)

    return templates.TemplateResponse(
        "cart.html",
        {"request": request, "flowers": flowers, "total_price": total_price}
    )

