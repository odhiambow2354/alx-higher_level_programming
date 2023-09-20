#!/usr/bin/python3
"""
script that takes in argumments and displays all the values in the states table of the htbn_0e_0_usa where 
name matches the arguments
"""

import from MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    curso.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]]
            rows = cursor.fetchall()
            for row in rows:
            print(i)
            cursor.close()
            db.close()
