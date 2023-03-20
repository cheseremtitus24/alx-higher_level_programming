#!/usr/bin/python3
"""
This module Makes use of an ORM
that adds a row entry to the table
states
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

    users = [
        State(name='Louisiana'),
    ]

    # add row entries all
    query = session.add_all(users)
    session.commit()
    print(users[0].id)
