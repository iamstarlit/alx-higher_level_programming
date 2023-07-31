#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <mysql_username> "
              "<mysql_password> <mysql_db_name>")
        exit(1)

    # Get MySQL username, password, and database name from command-line args
    mysql_username, mysql_password, mysql_db_name = argv[1:4]

    # Create engine and session
    db_url = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name)
              )
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Use a context manager for the session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Query for all City objects and their corresponding State names
        for city in session.query(City).order_by(City.id):
            print(f"{city.id}: {city.name} -> {city.state.name}")
