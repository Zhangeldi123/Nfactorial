from fastapi import APIRouter, Depends, Form, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from hw_back_8.app.database import get_db
from fastapi.templating import Jinja2Templates
from repository.user import UsersRepository
from schemas.user import UserResponse
from datetime import datetime, timedelta, timezone
from schemas.user import UserCreate
import jwt
import os

user_router = APIRouter(prefix="/users", tags=["user"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
template = Jinja2Templates(directory="templates")

def generate_access_token(user_id: int):
    secret = os.getenv("AUTH_SECRET", "secret")
    expiration = datetime.now(tz=timezone.utc) + timedelta(seconds=30)
    access_token = jwt.encode(
        {"user_id": user_id, "exp": expiration}, secret, algorithm="HS256"
    )
    return access_token


def generate_refresh_token(user_id: int):
    secret = os.getenv("AUTH_SECRET", "secret")
    expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=30)
    refresh_token = jwt.encode(
        {"user_id": user_id, "exp": expiration}, secret, algorithm="HS256"
    )
    return refresh_token



def verify_refresh_token(token: str) -> int:
    secret = os.getenv("AUTH_SECRET", "secret")
    try:
        user_id = jwt.decode(token, secret, algorithms=["HS256"])["user_id"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = UsersRepository.get_user_by_userid(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user_id



@user_router.get("/signup")
def signup_form(request: Request):
    return template.TemplateResponse("signup.html", {"request": request})

@user_router.post("/signup")
def signup(
    request: Request,
    email: str = Form(...),
    fullname: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_data = UserCreate(username=fullname, email=email, password=password)
    user = UsersRepository.create_user(db, user_data)
    return RedirectResponse(url="/users/login", status_code=303)

@user_router.get("/login")
def login_form(request: Request):
    return template.TemplateResponse("login.html", {"request": request})

@user_router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = UsersRepository.authenticate_user(db, email, password)
    
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    response = RedirectResponse(url="/users/profile", status_code=303)
    access_token = generate_access_token(user_id=user.id)  
    refresh_token = generate_refresh_token(user_id=user.id)  
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, max_age=7 * 24 * 60 * 60)
    return response


@user_router.post("/refresh")
def refresh_token(request: Request, response: Response):
    refresh_token = request.cookies.get("refresh_token")
    
    if not refresh_token:
        raise HTTPException(status_code=401, detail="No refresh token found")
    
    user_id = verify_refresh_token(refresh_token)  
    
    new_access_token = generate_access_token(user_id=user_id)  
    response.set_cookie(key="access_token", value=new_access_token, httponly=True)
    return {"access_token": new_access_token}


@user_router.get("/profile", response_class=HTMLResponse)
def profile_page(request: Request, current_user=Depends(UsersRepository.get_current_user)):
    """Serve the profile page with user details."""
    return template.TemplateResponse(
        "profile.html",
        {"request": request, "email": current_user.email, "fullname": current_user.username},
    )


@user_router.post("/logout")
def logout():
    """Logout user by clearing access and refresh tokens."""
    response = RedirectResponse(url="/users/login", status_code=303)
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response
