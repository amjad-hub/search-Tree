from fastapi import APIRouter
from fastapi import FastAPI,Depends,HTTPException,status
from ..schemes import User,ShowUser,Login
from .. import models
from ..database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from ..authenticate import get_password_hash,verify_password
from datetime import datetime, timedelta
from typing import Optional
from ..token import create_access_token
from ..database import get_db

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter(
      tags=["authentication"]
)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'User with the email {request.username} isn\'t exit')
    if not verify_password(request.password,user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'The password isn\'t coorect')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
