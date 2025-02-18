from fastapi import FastAPI
from api.user import user_router
from database import engine, Base
from api.flower import flower_router
from api.cart import cart_router


print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created!")


app = FastAPI()
app.include_router(user_router)
app.include_router(flower_router)
app.include_router(cart_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}