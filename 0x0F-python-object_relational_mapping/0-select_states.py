#!/usr/bin/python3
"""
   this module select all the states whithin the states table and order them.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost",
                                 port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cursor = connection.cursor()
    sql_query = "SELECT * FROM states"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
