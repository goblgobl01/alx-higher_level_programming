#!/usr/bin/python3
"""
    this script gonna add a new object to the databases hbtn_0e_6dotdotdot.
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

    new_object = State(name="Louisiana")
    session.add(new_object)
    session.commit()
    print(new_object.id)
