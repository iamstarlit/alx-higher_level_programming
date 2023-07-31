#!/usr/bin/python3
"""Prints the State object with the name passed as an argument from the db."""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line args
    mysql_username, mysql_password, mysql_db_name = sys.argv[1:4]

    # Create engine and session
    db_url = (
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(mysql_username, mysql_password, mysql_db_name)
    )
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object and print its information
    for instance in (
        session.query(State.name, City.id, City.name)
        .filter(State.id == City.state_id)
    ):
        print(f"{instance[0]}: ({instance[1]}) {instance[2]}")
