#!/usr/bin/python3
"""
This module creates a table named states
that has an id and a name field
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """
    This is a class that creates
    the schema of a table named
    states that will contain two columns
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
