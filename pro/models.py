from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base




class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    #items = relationship("Item", back_populates="owner")


class Tree(Base):

    __tablename__ = "tree"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=True, index=True)
    parent_Id = Column(Integer)

    #items = relationship("Item", back_populates="owner")
