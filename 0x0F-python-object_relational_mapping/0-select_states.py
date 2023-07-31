#!/usr/bin/python3
"""Working with MySQLdb module to execute select statement."""
import sys
import MySQLdb


def list_states(username, password, database):
    """Lists all states from the database hbtn_0e_0_usa"""

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to retrieve all states from the states table
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Print the states
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list the states
    list_states(username, password, database)
