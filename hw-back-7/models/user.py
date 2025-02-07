
from pydantic import BaseModel

class User(BaseModel):
    email: str
    fullname: str
    password: str
    user_id: int | None = None

