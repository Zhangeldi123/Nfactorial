from fastapi import FastAPI, Response

from .cars import create_cars

cars = create_cars(100)  
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)
@app.get("/cars")
async def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]

@app.get("/cars/{id}")
def find_car(id: int):
    for car in cars:
        if car["id"] == id:
            return car
    return Response("Not found", status_code=404, media_type="text/plain")






# (конец решения)
