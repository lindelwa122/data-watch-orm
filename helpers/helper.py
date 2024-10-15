import sqlite3

def delete(data):
    # todo
    pass

def contains(data):
    # todo
    pass

def count(data):
    # todo
    pass

def distinct(data):
    # todo
    pass

def exists(data):
    # todo
    pass

def earliest(data):
    # todo
    pass

def latest(data):
    # todo
    pass

def first(cursor, table_name):
    
    try:
        query = f"SELECT * FROM {table_name} LIMIT 1"
        cursor.execute(query)
        return cursor.fetchone()
    except sqlite3.OperationalError:
        # Return None if the table doesn't exist or any other SQLite operational error occurs
        return None

def last(cursor, table_name):
    # todo
    pass

def order_by(data):
    # todo
    pass

def reverse(data):
    # todo
    pass