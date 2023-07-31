#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv


def get_states_with_name_starting_with_N(user, password, database):
    """Get states with names starting with 'N' from the database."""

    try:
        db_connect = db.connect(host="localhost", port=3306,
                                user=user, passwd=password, db=database)
        db_cursor = db_connect.cursor()

        db_cursor.execute(
                "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                        ORDER BY states.id ASC")

        rows_selected = db_cursor.fetchall()

        return rows_selected

    except db.Error as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <USERNAME> <PASSWORD> <DATABASE>")
        exit(1)

    user = argv[1]
    password = argv[2]
    database = argv[3]

    states = get_states_with_name_starting_with_N(user, password, database)

    if states:
        for row in states:
            print(row)
