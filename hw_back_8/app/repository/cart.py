import json
from fastapi import Request, Response

class CartRepository:
    COOKIE_NAME = "cart"

    @staticmethod
    def get_cart(request: Request):
        cart_cookie = request.cookies.get(CartRepository.COOKIE_NAME)
        return json.loads(cart_cookie) if cart_cookie else []

    @staticmethod
    def add_to_cart(request: Request, response: Response, flower_id: int):
        cart_items = CartRepository.get_cart(request)
        cart_items.append(flower_id)

        response.set_cookie(
            key=CartRepository.COOKIE_NAME,
            value=json.dumps(cart_items),
            httponly=True
        )
    
    @staticmethod
    def clear(request: Request, response: Response):
        response.delete_cookie(CartRepository.COOKIE_NAME)

