import sqlite3
import os

def reset_db():
    db_path = 'app.db'
    sql_path = 'app/models/football_schema.sql'
    
    if not os.path.exists(sql_path):
        print(f"Error: SQL file not found at {sql_path}")
        return

    try:
        print(f"Connecting to database at {db_path}...")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        print(f"Reading SQL script from {sql_path}...")
        with open(sql_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        print("Executing SQL script...")
        cursor.executescript(sql_script)
        
        conn.commit()
        print("Database reset and populated successfully.")
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Change to backend directory if not already there
    if os.path.basename(os.getcwd()) != 'backend':
        os.chdir('backend')
    reset_db()
