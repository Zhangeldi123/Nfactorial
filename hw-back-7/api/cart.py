from fastapi import APIRouter, Form, Request, Response, Cookie
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import json
from repository.flowers import FlowersRepository
from models.flowers import Flower

cart_router = APIRouter(prefix="/cart", tags=["cart"])
flowers_repo = FlowersRepository()
template = Jinja2Templates(directory="templates")


@cart_router.post("/items")
def add_to_cart(request: Request, flower_id: int = Form(...), cart: str = Cookie(default="[]")):
    cart_items = json.loads(cart)
    cart_items.append(flower_id)
    new_cart = json.dumps(cart_items)

    response = RedirectResponse(url="/flowers/", status_code=303)
    response.set_cookie(key="cart", value=new_cart)
    return response


@cart_router.get("/items")
def view_cart(request: Request, cart: str = Cookie(default="[]")):
    print(f"Cart cookie content: {cart}")
    cart_items = json.loads(cart)
    print(f"Parsed cart items: {cart_items}")

    flowers_in_cart = []
    for flower_id in cart_items:
        flower = flowers_repo.get_by_id(flower_id)
        print(f"Flower for ID {flower_id}: {flower}")  # Debug
        flowers_in_cart.append(flower)

    total_price = sum(flower.price for flower in flowers_in_cart if flower)

    return template.TemplateResponse(
        "/cart.html",
        {
            "request": request,
            "flowers": flowers_in_cart,
            "total_price": total_price
        }
    )

@cart_router.post("/clear")
def clear_cart():
    response = RedirectResponse(url="/cart/items", status_code=303)
    response.delete_cookie(key="cart")
    return response
