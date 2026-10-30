import sqlite3
import os

DB_Path = os.path.join("data","documents.db")


def connection():
    return sqlite3.connect(DB_Path)


def init_db():

    conn = connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Filename TEXT,
        Path TEXT,
        Thumbnail_path TEXT,
        Tags Text,
        Description Text,
        Upload_date Text,
        Lecture_Date Text,
        Total_Pages Text
        
    )
    """)

    conn.commit()
    print("Db initialized")
    conn.close()



    





