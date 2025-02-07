from fastapi import APIRouter, Form, Response, Request, Cookie, File, UploadFile, HTTPException, Depends
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import os
import datetime
from fastapi.templating import Jinja2Templates
from repository.user import UserRepository
from exception.exception import UserNotFound
from models.user import User
from .schemas.user import (
    UserAuthRequest,
    UserAuthResponse,
    RefreshTokenRequest,
    RefreshTokenResponse,
)

users_router = APIRouter(prefix="/users", tags=["users"])
users_repo = UserRepository()
template = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def generate_access_token(user_id: int):
    secret = os.getenv("AUTH_SECRET", "secret")
    expiration = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=15)
    return jwt.encode({"user_id": user_id, "exp": expiration}, secret, algorithm="HS256")

def generate_refresh_token(user_id: int):
    secret = os.getenv("AUTH_SECRET", "secret")
    expiration = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=7)
    return jwt.encode({"user_id": user_id, "exp": expiration}, secret, algorithm="HS256")

def verify_refresh_token(token: str) -> str:
    secret = os.getenv("AUTH_SECRET", "secret")
    user_id = jwt.decode(token, secret, algorithms=["HS256"]) ["user_id"]
    user = users_repo.get_user_by_userid(user_id)
    if user is None:
        raise UserNotFound("user not found")
    return user_id

@users_router.get("/signup", response_class=HTMLResponse)
def sign_up_form(request: Request):
    return template.TemplateResponse("signup.html", {"request": request})

@users_router.post("/signup")
def register(
    email: str = Form(...),
    fullname: str = Form(...),
    password: str = Form(...),
):
    user = User(email=email, fullname=fullname, password=password)
    users_repo.add_user(user)
    return RedirectResponse(url="/users/login", status_code=303)

@users_router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return template.TemplateResponse("login.html", {"request": request})

@users_router.post("/login")
def verify_user(
    email: str = Form(...),
    password: str = Form(...)
):
    user = users_repo.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password != password:
        raise HTTPException(status_code=400, detail="Invalid password or email")

    access_token = generate_access_token(user.user_id)
    return RedirectResponse(url=f"/users/profile?token={access_token}", status_code=303)


@users_router.get("/profile", response_class=HTMLResponse)
def get_profile(request: Request, token: str):
    try:
        secret = os.getenv("AUTH_SECRET", "secret")
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        user_id = payload["user_id"]
        user = users_repo.get_user_by_userid(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return template.TemplateResponse("profile.html", {
        "request": request,
        "email": user.email,
        "fullname": user.fullname
    })

@users_router.post("/refresh", status_code=200)
def refresh(refresh_token: RefreshTokenRequest) -> RefreshTokenResponse:
    try:
        user_id = verify_refresh_token(refresh_token.refresh_token)
    except UserNotFound as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except JWTError as ex:
        raise HTTPException(status_code=400, detail="Invalid or expired refresh token")

    access_token = generate_access_token(user_id)
    return RefreshTokenResponse(access_token=access_token)

@users_router.get("/users")
def get_all_users():
    return users_repo.get_all_users()
