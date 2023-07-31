#!/usr/bin/python3
"""Prints the State object with the name passed as an argument from the db"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <mysql_username> "
              "<mysql_password> <mysql_db_name>")
        exit(1)

    # Get MySQL username, password, and database name from command-line args
    mysql_username, mysql_password, mysql_db_name = sys.argv[1:]

    # Create engine and session
    db_url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name))

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete all State objects with a name containing 'a'
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()

    # Close the session
    session.close()
