#!/usr/bin/python3
"""
    this script fetch the first object in the state table.
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

    first_object = session.query(State).first()
    if (first_object):
        print(f"{first_object.id}: {first_object.name}")
    else:
        print("Nothing")
