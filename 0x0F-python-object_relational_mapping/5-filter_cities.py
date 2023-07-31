#!/usr/bin/python3
"""
Script that takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv


def get_cities_by_state(user, password, database, state_name):
    """Get all cities of a state from the database."""
    try:
        db_connect = db.connect(host="localhost", port=3306,
                                user=user, passwd=password, db=database)

        with db_connect.cursor() as db_cursor:
            query = """
                SELECT cities.id, cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC
            """
            db_cursor.execute(query, {'state_name': state_name})
            rows_selected = db_cursor.fetchall()

        return rows_selected

    except db.Error as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <USERNAME> <PASSWORD> <DATABASE> <STATE_NAME>"
              .format(argv[0])
              )
        exit(1)

    user = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    cities = get_cities_by_state(user, password, database, state_name)

    if cities:
        print(", ".join(row[1] for row in cities))
