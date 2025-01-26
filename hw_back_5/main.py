from tempfile import template
from fastapi import FastAPI, Request
from pydantic import BaseModel
from tomlkit import aot
from .api.books import books_router
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import jinja2

templates = Jinja2Templates("hw_back_5/templates")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books_router)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request})
