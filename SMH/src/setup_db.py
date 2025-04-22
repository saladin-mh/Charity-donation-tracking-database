# src/setup_db.py

"""
Setup script for SMH Charity Donation Tracker.

Initialises the SQLite database using a schema file.
This utility is intended for first-time setup or schema resets.
"""

import sqlite3
import os

# Define paths relative to this script
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "smh.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "smh_schema.sql")


def run_schema():
    """
    Reads the SQL schema and applies it to the SQLite database.

    This creates all tables and constraints required by the application.
    """
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()

    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        print(f"[✔] Schema created successfully at {DB_PATH}")


if __name__ == "__main__":
    run_schema()
    print("[✔] Database setup completed.")
    
