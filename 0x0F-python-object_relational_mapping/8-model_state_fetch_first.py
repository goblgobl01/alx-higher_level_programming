#!/usr/bin/python3
"""
    this script fetch the first object in the state table.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import text

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT id, name FROM states WHERE id = 1;"))
        for row in result:
            print(f"{row[0]}: {row[1]}")
