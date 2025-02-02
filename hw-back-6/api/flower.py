from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from jose import JWTError, jwt
from fastapi import APIRouter, Form, Response, Request, Cookie  
from repository.flowers import FlowersRepository

flowers_router = APIRouter(prefix="/flowers", tags=["flowers"])
flowers_repo = FlowersRepository()
template = Jinja2Templates(directory="templates")


@flowers_router.get("/")
def get_all_flowers(request: Request, page: int = 1, per_page: int = 10):
    flowers = flowers_repo.get_all_flowers()
    start = (page - 1) * per_page
    end = start + per_page
    paginated_flowers = flowers[start:end]
    
    next_page = page + 1 if end < len(flowers) else None
    previous_page = page - 1 if start > 0 else None

    return template.TemplateResponse(
        "/flowers.html", 
        {
            "request": request,
            "flowers": [flower for flower in paginated_flowers],
            "next_page": next_page,
            "previous_page": previous_page,
            "per_page": per_page
        }
    )

@flowers_router.post("/")
def add_flower(request: Request, name: str = Form(...), quantity: int = Form(...), price: float = Form(...)):
    flowers_repo.add_flower(name, quantity, price)
    return RedirectResponse(url="/flowers", status_code=303)

