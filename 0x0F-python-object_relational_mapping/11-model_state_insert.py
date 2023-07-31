#!/usr/bin/python3
"""
Script that adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
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
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the State object 'Louisiana' to the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Query the State object with the name 'Louisiana' and print its id
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)

    # Close the session
    session.close()
