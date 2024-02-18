import sqlite3

def list_tables():
    conn = sqlite3.connect('Banklogin.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()

    # print the list of table names
    for table in tables:
        print(table[0])

list_tables()
