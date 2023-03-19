#!/usr/bin/python3
import MySQLdb
import sys

args_length = len(sys.argv)
if args_length == 4:
    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3] #'hbtn_0e_0_usa'
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    cursor = db.cursor()

    # Get data from database
    try:
        cursor.execute("SELECT * FROM states")
        rows = cursor.fetchall()
    except (MySQLdb.Error, e):
        try:
            print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print ("MySQL Error: %s" % str(e))
    else:
        # Print results in comma delimited format
        for row in rows:
            print (row)
    finally:
        # Close all cursors
        cursor.close()
        # Close all databases
        db.close()
else:
    print(f"Usage: {sys.argv[0]} <db_username> <db_password> <db_name> ", file=sys.stderr)



