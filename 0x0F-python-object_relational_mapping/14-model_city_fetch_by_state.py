#!/usr/bin/python3
"""
This module Makes use of an ORM
that Retrieves rows from the table states
and orders them in ascending order based
on the primary key column
"""
import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_city import Base, City
from model_state import State

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

    query = session.query(
        City,
        State).join(
        State,
        City.state_id == State.id).order_by(
        City.id)
    for _row in query.all():
        print(
            "{:s}: ({:d}) {:s}".format(
                _row[1].name,
                _row[0].id,
                _row[0].name))
