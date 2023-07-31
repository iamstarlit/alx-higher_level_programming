#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv


def get_all_cities(user, password, database):
    """Get all cities from the database."""
    try:
        db_connect = db.connect(host="localhost", port=3306,
                                user=user, passwd=password, db=database)

        with db_connect.cursor() as db_cursor:
            query = (
                    "SELECT cities.id, cities.name, states.name FROM "
                    "cities JOIN states ON cities.state_id = states.id "
                    "ORDER BY cities.id ASC"
                    )
            db_cursor.execute(query)
            rows_selected = db_cursor.fetchall()

        return rows_selected

    except db.Error as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <USERNAME> <PASSWORD> <DATABASE>")
        exit(1)

    user = argv[1]
    password = argv[2]
    database = argv[3]

    cities = get_all_cities(user, password, database)

    if cities:
        for row in cities:
            print(row)
