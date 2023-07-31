#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    # Get MySQL username, password, and database name from command line args
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db_name = sys.argv[3]

    # Create engine and session
    db_url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name)
              )

    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Use a context manager for the session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        newState = State(name='California')
        newCity = City(name='San Francisco')
        newState.cities.append(newCity)

        session.add(newState)
        session.add(newCity)
        session.commit()
