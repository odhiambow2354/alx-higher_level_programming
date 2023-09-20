#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

# Ensure that the code is not executed when imported
if __name__ == '__main__':
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Define the SQL query to retrieve matching rows
    name_query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])

    # Execute the SQL query
    cur.execute(name_query)

    # Fetch all the rows that match the query
    rows = cur.fetchall()

    # Print the retrieved rows
    for i in rows:
        print(i)

    # Clean up by closing the cursor and the database connection
    cur.close()
    db.close()
