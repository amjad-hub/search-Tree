from fastapi import FastAPI
#import router.users as u
#import router.items as it
#print(__name__)
#print(__package__)
from .router import users,authentication,tree
from . import models
from .database import engine

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users.",
    },
    {
        "name": "tree",
        "description": "Operations with **tree**.",
    },
    {
        "name": "authentication",
        "description": " The **login** logic ",
    },

]


app = FastAPI(openapi_tags=tags_metadata)
app.include_router(users.router)
app.include_router(tree.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(bind=engine)


