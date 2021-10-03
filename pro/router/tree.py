from fastapi import FastAPI,Depends,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemes, Oauth2
from ..schemes import Tree,ShowTree
from typing import List
from ..Oauth2 import get_current_user
from ..database import get_db

print(__name__)
print(__package__)

router = APIRouter(
    tags = ['tree'],
    prefix= '/tree'
)


def get_subTree(sub_tree,tree, nodes):
    for node in nodes:
        if node.parent_Id == tree.id:
            sub_tree.append(node)
            get_subTree(sub_tree, node, nodes)
    
    return sub_tree

@router.post('/',response_model= ShowTree)
def create_tree(request:Tree, db:Session = Depends(get_db),get_current_user:schemes.User = Depends(Oauth2.get_current_user)):
    tree = models.Tree(text = request.text, parent_Id = request.parent_Id)

    db.add(tree)
    db.commit()
    db.refresh(tree)
    return tree

@router.get('/text_search/{node_text}',response_model= List[ShowTree])
def get_tree(node_text:str, db:Session = Depends(get_db),get_current_user:schemes.User = Depends(Oauth2.get_current_user)):
    node = db.query(models.Tree).filter(models.Tree.text == node_text).first()
    if not node:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'The item with the ID {node_text} doesn\'t exist')

    nodes = db.query(models.Tree).all()
    sub_tree = ()
    get_subTree(sub_tree,node, nodes)

    return sub_tree

@router.get('/id_search/{node_id}',response_model= List[ShowTree])
def get_tree(node_id:int, db:Session = Depends(get_db),get_current_user:schemes.User = Depends(Oauth2.get_current_user)):

    tree = db.query(models.Tree).filter(models.Tree.id == node_id).first()
    if not tree:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f'The node with the ID {node_id} doesn\'t exist')

    nodes = db.query(models.Tree).all()
    sub_tree = ()

    get_subTree(sub_tree,tree, nodes)

    return sub_tree




