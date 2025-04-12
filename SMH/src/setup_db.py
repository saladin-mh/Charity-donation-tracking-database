# src/setup_db.py

import sqlite3
import os

# Use same location as db_manager
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "smh.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "smh_schema.sql")

def run_schema():
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        print(f"[✔] Schema created successfully at {DB_PATH}")

if __name__ == "__main__":
    run_schema()
    print("[✔] Database setup completed.")
    # This script creates the database schema for the SMH application.
    # It reads the schema from a SQL file and executes it against the SQLite database.
    # The database is located in the /db/ folder.
    # The script is run when executed directly.