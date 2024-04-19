#!/usr/bin/python3
"""
    a class that gonna define the state table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    this is the satee class

    Attributes:
        id (int): identifier for each state.
        name (string): the name of each state.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
