import sqlite3
import os

def verify():
    db_path = "app.db"
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found.")
        return
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables found in database:")
    for table in tables:
        print(f" - {table[0]}")
    conn.close()

if __name__ == "__main__":
    verify()
