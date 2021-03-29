#!/usr/bin/python3
"""
list all the cities in the datase
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
	        WHERE states.name = %(c_name)s \
                INNER JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id ASC;", {'c_name': argv[4]})
    states = cur.fetchall()
    a_list = []

    for x in states:
        a_list.append(x[0])
    lista = ", ".join(a_list)
    print(lista)

    cur.close()
    db.close()
