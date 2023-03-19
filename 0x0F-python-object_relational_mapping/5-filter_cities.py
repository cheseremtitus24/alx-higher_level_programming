#!/usr/bin/python3
"""
This module prints all cities found in a queried state
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

        Raises
        ------
       MYSQLdb.Error
            If database connection or Query fails
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
        sql = "SELECT cities.name FROM cities INNER JOIN" +\
            " states on cities.state_id = states.id WHERE states.name = %s"
        cursor.execute(sql, (MY_STATE,))
        rows = cursor.fetchall()
    except (MySQLdb.Error, e):
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
    else:
        # Print results in comma delimited format
        counter = 0
        for row in rows:
            for col in row:
                if counter == 0:
                    print("%s" % col, end="")
                else:
                    print(", %s" % col, end="")
                counter += 1
        print("")
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
        MY_STATE = sys.argv[4]  # 'Nevada'
        select_query(MY_USER, MY_PASS, MY_DB, MY_STATE)
    else:
        print("Invalid num arguments")
