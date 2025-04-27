# db/db_manager.py

import sqlite3
import os
from contextlib import contextmanager

# Define the database file location relative to this script
DB_NAME = os.path.join(os.path.dirname(__file__), "smh.db")

def initialize_database():
    """
    Initialises the SQLite database with the required settings.
    This function enforces foreign key constraints upon initial connection.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        print("[SMH] Database initialised with foreign key enforcement.")

@contextmanager
def get_connection():
    """
    Provides a context-managed connection to the SQLite database.

    Ensures:
    - Foreign key support is always enabled
    - Connections are properly closed
    - Results are returned as dictionary-style rows (sqlite3.Row)
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Allows access to columns by name
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        yield conn
    finally:
        conn.close()
        print("[SMH] Database connection closed.")
