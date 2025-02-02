from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, FastAPI, Response, Request
from api.user import users_router
from api.flower import flowers_router
from api.cart import cart_router

app = FastAPI()
app.include_router(users_router)
app.include_router(flowers_router)
app.include_router(cart_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}