#!/usr/bin/python3
"""
Lists all states with name startinf with N
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute('SELECT *FROM states\
                WHERE name LIKE "N%"\
                ORDER BY states.id ASC;')
    states = cur.fetchall()

    for x in states:
        print(x)

    cur.close()
    db.close()
