#!/usr/bin/python3
"""
This module Makes use of an ORM
that Retrieves rows from the table states
and orders them in ascending order based
on the primary key column
"""
import sys

from sqlalchemy.orm import sessionmaker

from model_state import Base, State

from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    for _row in query.all():
        print("{:d}: {:s}".format(_row.id, _row.name))
