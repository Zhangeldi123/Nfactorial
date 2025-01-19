from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users", response_class=HTMLResponse)
def get_users(request: Request):

    return templates.TemplateResponse("users/index.html", {"request": request, "users": users})

@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user_by_id(request: Request, user_id: int):

    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        return Response("Not found", status_code=404, media_type="text/plain")
    return templates.TemplateResponse("users/user.html", {"request": request, "user": user})


print(users)
# (конец решения)
