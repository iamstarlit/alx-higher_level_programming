#!/usr/bin/python3
"""
Script that takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv


def get_states_by_name(user, password, database, name):
    """Get states with a specific name from the database."""
    try:
        db_connect = db.connect(host="localhost", port=3306,
                                user=user, passwd=password, db=database)
        db_cursor = db_connect.cursor()

        db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' "
            "ORDER BY states.id ASC".format(name)
        )

        rows_selected = db_cursor.fetchall()
        return rows_selected

    except db.Error as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    if len(argv) != 5:
        print(f"Usage: {argv[0]} <USERNAME> <PASSWORD> <DATABASE> <NAME>")
        exit(1)

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name = argv[4]

    states = get_states_by_name(user, password, database, name)

    if states:
        for row in states:
            print(row)
