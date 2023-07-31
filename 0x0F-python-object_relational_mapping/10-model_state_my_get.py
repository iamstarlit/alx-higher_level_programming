#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(argv) != 5:
        print(f"Usage: {argv[0]} <mysql_username> <mysql_password> "
              "<mysql_db_name> <state_name>")
        exit(1)

    # Get MySQL username, password, and database name from command-line args
    mysql_username, mysql_password, mysql_db_name, state_name = argv[1:5]

    # Create engine and session
    db_url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name)
              )
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first State object with the given state_name and print id
    state = session.query(State).filter(State.name == state_name).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
