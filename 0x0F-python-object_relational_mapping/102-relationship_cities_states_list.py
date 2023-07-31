#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa along with their
corresponding State names.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # Connect to the MySQL server and database using provided credentials
    mysql_username, mysql_password, mysql_db_name = sys.argv[1:4]

    # Create engine and session
    db_url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name),
              pool_pre_ping=True
              )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all City objects along with their corresponding State objects,
    # ordered by City id
    states = session.query(State).join(City).order_by(City.id).all()

    # Print City objects and their corresponding State names
    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
