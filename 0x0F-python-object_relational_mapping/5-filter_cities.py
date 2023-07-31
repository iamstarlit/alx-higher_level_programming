#!/usr/bin/python3
"""Lists all cities of a specific state from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def list_cities_by_state(username, password, db_name, state_name):
    """
    Connects to the database and prints all cities of the given state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): Name of the state.
    """
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=db_name, port=3306)
        with db.cursor() as cur:
            cur.execute("""
            SELECT cities.name FROM
            cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s""", (state_name,)
                        )
            rows = cur.fetchall()
            cities_list = [row[0] for row in rows]
            print(", ".join(cities_list))
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0])
              )
    else:
        username, password, db_name, state_name = sys.argv[1:5]
        list_cities_by_state(username, password, db_name, state_name)
