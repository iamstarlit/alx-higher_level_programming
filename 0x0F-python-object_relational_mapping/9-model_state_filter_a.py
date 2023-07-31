#!/usr/bin/python3
"""
Script that lists all State objects
that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <mysql_db_name>"
              .format(argv[0]))
        exit(1)

    # Get MySQL username, password, and database name from command-line args
    mysql_username, mysql_password, mysql_db_name = argv[1:4]

    # Create engine and session
    db_url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name)
              )
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing the letter 'a' and print their id and name
    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            print(f'{state.id}: {state.name}')
