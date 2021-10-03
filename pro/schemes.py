from pydantic import BaseModel
from typing import List 
from typing import Optional




class User(BaseModel):
    email :str
    password : str

class BaseItem(BaseModel):
    name :str
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    email:str
    class Config:
        orm_mode = True


class Login(BaseModel):
    username :str
    password : str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class Tree(BaseModel):
    text:str
    parent_Id: int


class ShowTree(BaseModel):
    text:str
    parent_Id: int
    class Config:
        orm_mode = True
