#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Check the number of command-line arguments"""
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <mysql_db_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    """Get MySQL username, password, and database name
    from command line arguments"""
    mysql_username, mysql_password, mysql_db_name = sys.argv[1:4]

    """Create engine and session"""
    DB_URL = ("mysql+mysqldb://{}:{}@localhost:3306/{}"
              .format(mysql_username, mysql_password, mysql_db_name)
              )
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query all State objects and sort by id"""
    states = session.query(State).order_by(State.id).all()

    """Print results"""
    for state in states:
        print(f'{state.id}: {state.name}')
