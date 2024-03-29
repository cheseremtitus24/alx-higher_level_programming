#!/usr/bin/python3
"""
This module takes in commandline arguments and performs
a database query to retrieve all the rows from the table
named states by applying a filter to capture the names
of states that are passed in via commandline argument
# Prevent SQL injection by :

    not doing this:
        sql = "INSERT INTO TABLE_A (COL_A,COL_B) VALUES
        (%s, %s)" % (val1, val2) cursor.execute(sql)
    but doing this:
    sql = "INSERT INTO TABLE_A (COL_A,COL_B) VALUES (%s, %s)"
cursor.execute(sql, (val1, val2))
"""
import MySQLdb
import sys


def select_query(MY_USER, MY_PASS, MY_DB, MY_STATE):
    """ Prints table rows in a tuple format from the table states


        Parameters
        ----------
        MY_USER: str,
            The database username
        MY_PASS: str,
            The database password
        MY_DB: str,
            The database name to make queries to
        MY_STATE: str,
            The database column state to match

        Raises
        ------
       MYSQLdb.Error
            If database connection fails
    """
    MY_HOST = 'localhost'
    db = MySQLdb.connect(
        host=MY_HOST,
        user=MY_USER,
        port=3306,
        passwd=MY_PASS,
        db=MY_DB)
    cursor = db.cursor()

    # Get data from database
    try:
        sql = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        cursor.execute(sql, (MY_STATE,))
        rows = cursor.fetchall()
    except (MySQLdb.Error, e):
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
    else:
        # Print results in comma delimited format
        for row in rows:
            print(row)
    finally:
        # Close all cursors
        cursor.close()
        # Close all databases
        db.close()


if __name__ == '__main__':
    args_length = len(sys.argv)
    if args_length == 5:
        MY_USER = sys.argv[1]
        MY_PASS = sys.argv[2]
        MY_DB = sys.argv[3]  # 'hbtn_0e_0_usa'
        MY_STATE = sys.argv[4]  # 'hbtn_0e_0_usa'
        select_query(MY_USER, MY_PASS, MY_DB, MY_STATE)
    else:
        pass
