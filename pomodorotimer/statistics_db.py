import os
import time
import sqlite3
import datetime


def create_table_statistic():
    sql = """
    CREATE TABLE IF NOT EXISTS 
    statistic(
        date TEXT,
        work INT,
        relaxation INT
    )
    """
    try:
        cursor.execute(sql)  # We execute the SQL query
    except sqlite3.DatabaseError as err:
        print("Error:", err)


def read_today_entry() -> tuple:
    try:
        sql = f"SELECT work, relaxation FROM statistic WHERE date = '{DATE}'"
        cursor.execute(sql)
    except sqlite3.DatabaseError as err:
        print("Error: ", err)

    work = 0
    relaxation = 0
    rows = cursor.fetchall()
    if rows:
        work = rows[0][0]
        relaxation = rows[0][1]

    return [DATE], [work], [relaxation]


def insert_entry(work: int, relaxation: int) -> None:
    sql = """INSERT INTO statistic(date, work, relaxation) VALUES (?, ?, ?)"""
    params = (DATE, work, relaxation)
    try:
        cursor.execute(sql, params)
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn.commit()  # Save changes to the database


def update_entry(work: int, relaxation: int) -> None:
    sql = f"""
    UPDATE statistic SET work={work}, relaxation={relaxation} 
    WHERE date='{DATE}'
    """
    try:
        cursor.execute(sql)
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn.commit()


def today_entry(work: int, relaxation: int) -> None:
    """
    In this case, you cannot use:
    'INSERT OR REPLACE INTO User VALUES(?,?,?)'
    """
    # First, check if there is a log entry for today
    _, work_db, relaxation_db = read_today_entry()
    if work_db == [0] and relaxation_db == [0]:
        # If the record does not exist, then add it
        insert_entry(work, relaxation)
    else:
        # Otherwise, update the record by ADDING new data
        update_entry(int(*work_db) + work, int(*relaxation_db) + relaxation)


def read_all_entry() -> tuple:
    try:
        cursor.execute("SELECT date, work, relaxation FROM statistic")
    except sqlite3.DatabaseError as err:
        print("Error: ", err)

    dates = []
    work = []
    relaxation = []
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            dates.append(row[0])
            work.append(row[1])
            relaxation.append(row[2])

    return dates, work, relaxation


def delete_today_entry() -> None:
    try:
        cursor.execute(f"DELETE FROM statistic WHERE date='{DATE}'")
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn.commit()


def delete_all_entry() -> None:
    try:
        cursor.execute("DELETE FROM statistic")
    except sqlite3.DatabaseError as err:
        print("Error: ", err)
    else:
        conn.commit()


def close_db():
    cursor.close()
    conn.close()


# Create a connection object.
# If the database file is not found in the specified directory, then it will
# be created.
conn = sqlite3.connect(os.path.dirname(__file__) + '/statistics.db')

# According to the DB-API 2.0 specification, after creating a connection
# object, you must create a cursor object. All further requests must be
# made through this object. Creating a cursor object is done using the
# cursor() method.
# Create a cursor object (all database queries are executed through it).
cursor = conn.cursor()

# Today's date
DATE = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d'))

# Create table statistic if not exists
create_table_statistic()
