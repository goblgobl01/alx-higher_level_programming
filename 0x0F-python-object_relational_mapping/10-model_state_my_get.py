#!/usr/bin/python3
"""
    this script fetch the all the states with "sys.argv[4]" on the name.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    object = session.query(State).filter(State.name == sys.argv[4]).first()
    if object:
        print(object.id)
    else:
        print("Not found")
