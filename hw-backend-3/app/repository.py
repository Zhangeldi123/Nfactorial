from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .cars import create_cars, Car

cars = create_cars(100)

class CarRepository:
    def __init__(self):
        self.cars = cars
    
    def get_cars(self):
        return self.cars
    
    def filter_cars(self, car_name: str):
        filtered_cars = [car for car in self.cars if car_name.lower() in car.name.lower()]
        return filtered_cars
    
    def save(self, car: Car):
        self.cars.append(car)

    