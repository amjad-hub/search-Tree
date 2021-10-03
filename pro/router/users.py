from fastapi import FastAPI,Depends,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemes, Oauth2
from ..schemes import ShowUser,User
from ..authenticate import get_password_hash
from typing import List
from ..Oauth2 import get_current_user
from ..database import get_db


router = APIRouter(
    tags = ['users'],
    prefix= '/users'
)


@router.post('/registeration')
def create_user(request:User, db:Session = Depends(get_db)):
    hashed_password = get_password_hash(request.password)
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'The user with the email {request.email} already exist')
    user = models.User(email = request.email, password = hashed_password)

    db.add(user)
    db.commit()
    db.refresh(user)
    return f'Congratulations {request.email}, You have successfully registered'


@router.get('/',response_model= List[ShowUser])
def get_users(db:Session = Depends(get_db),get_current_user:schemes.User = Depends(Oauth2.get_current_user)):

    users = db.query(models.User).all()
    return users

@router.get('/{user_id}',response_model= ShowUser)
def get_user(user_id:int, db:Session = Depends(get_db),get_current_user:schemes.User = Depends(Oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'The user with the ID {user_id} doesn\'t exist')
    return user

