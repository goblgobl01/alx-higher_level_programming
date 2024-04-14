#!/usr/bin/python3
"""
   this python script selet all the cities within the hbtn databases.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        """
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([city[0] for city in rows]))
    cur.close()
    db.close()
