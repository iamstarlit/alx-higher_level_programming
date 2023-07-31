#!/usr/bin/python3
"""State class inherting from Base."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the Base class using declarative_base()
Base = declarative_base()

# Define the State class
class State(Base):
    """Defines the State class."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
