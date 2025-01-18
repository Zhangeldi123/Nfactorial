from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from .cars import create_cars
from .repository import CarRepository, Car

app = FastAPI()
repo = CarRepository()
templates = Jinja2Templates(directory="templates")




@app.get("/cars/search", response_class=HTMLResponse)
def search_car(request: Request, car_name: str = ""):
    filtered_cars = repo.filter_cars(car_name)
    return templates.TemplateResponse("search.html", {"request": request, "cars": filtered_cars, "query": car_name})


@app.get("/cars", response_class=HTMLResponse)
def get_comments(request: Request, page: int = 1, per_page: int = 10):
    cars = repo.get_cars()
    start = (page - 1) * per_page
    end = start + per_page
    paginated_cars = cars[start:end]
    

    next_page = page + 1 if end < len(cars) else None
    previous_page = page - 1 if start > 0 else None

    return templates.TemplateResponse(
        "/index.html", 
        {
            "request": request,
            "cars": [car.dict() for car in paginated_cars],
            "next_page": next_page,
            "previous_page": previous_page,
            "per_page": per_page
        }
    )


@app.get("/cars/new", response_class=HTMLResponse)
def show_add_comment_form(request: Request):
    return templates.TemplateResponse("new_car.html", {"request": request})

@app.post("/cars/new", response_class=HTMLResponse)
def add_car(request: Request, name: str = Form(...), year: int = Form(...)):
    new_car = Car(id=len(repo.cars) + 1, name=name, year=year)
    repo.save(new_car)

    return RedirectResponse(url="/cars", status_code=303)
