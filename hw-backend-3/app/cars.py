import random

from faker import Faker
from faker_vehicle import VehicleProvider
from pydantic import BaseModel

class Car(BaseModel):
    name: str
    year: int
    id: int | None = None





def create_cars(cars_total):
    fake = Faker()
    fake.add_provider(VehicleProvider)

    car_ids = list(range(cars_total))
    random.seed(0)
    random.shuffle(car_ids)

    cars = [Car(id=car_ids[i] + 1, name=fake.vehicle_make_model(), year=fake.machine_year()) for i in range(cars_total)]

    return cars
