#!/usr/bin/python3
"""
    a class that gonna define the City table.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    this is the City class

    Attributes:
        id (int): identifier for each state.
        name (string): the name of each state.
        state_id (int): relatioship between id of a state and the city .
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
