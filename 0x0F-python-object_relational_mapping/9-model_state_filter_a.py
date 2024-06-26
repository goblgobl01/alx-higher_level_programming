#!/usr/bin/python3
"""
    this script fetch the all the states with "a" on the name.
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

    all_object = session.query(State).filter(State.name.like("%a%")).all()
    for row in all_object:
        print(f"{row.id}: {row.name}")
