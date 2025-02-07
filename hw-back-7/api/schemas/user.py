from pydantic import BaseModel


class UserAuthRequest(BaseModel):
    username: str 
    password: str


class UserAuthResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str