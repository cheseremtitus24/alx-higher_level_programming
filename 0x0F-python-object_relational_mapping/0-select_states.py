#!/usr/bin/python3
import MySQLdb
import sys

"""
This module takes in commandline arguments and performs
a database query to retrieve all the rows from the table
named states
"""


def select_query(MY_USER, MY_PASS, MY_DB):
    """ Prints table rows in a tuple format from the table states


        Parameters
        ----------
        MY_USER: str,
            The database username
        MY_PASS: str,
            The database password
        MY_DB: str,
            The database name to make queries to

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
        cursor.execute("SELECT * FROM states")
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
    if args_length == 4:
        MY_USER = sys.argv[1]
        MY_PASS = sys.argv[2]
        MY_DB = sys.argv[3]  # 'hbtn_0e_0_usa'
        select_query(MY_USER, MY_PASS, MY_DB)
    else:
        print(
            f"Usage: {sys.argv[0]} <db_username> <db_password> <db_name> ",
            file=sys.stderr)
