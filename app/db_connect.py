import pymysql
import pymysql.cursors
from flask import g

def get_db():
    # Check if the database connection is not in `g` or if it's closed
    if 'db' not in g or not is_connection_open(g.db):
        print("Re-establishing closed database connection.")
        g.db = pymysql.connect(
            # Updated Database Configuration
            host='vrk7xcrab1wsx4r1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  # Updated host
            user='hsd0p4mpaegonjkl',       # Updated user
            password='fm83hnwngpgij1j3',    # Updated password
            database='as9wdavrfnsianhl',    # Updated database name
            cursorclass=pymysql.cursors.DictCursor  # Use DictCursor for dictionary-based results
        )
    return g.db

def is_connection_open(conn):
    try:
        conn.ping(reconnect=True)  # Check connection health and reconnect if needed
        return True
    except:
        return False

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None and not db._closed:
        print("Closing database connection.")
        db.close()
