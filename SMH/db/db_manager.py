# db/db_manager.py

import sqlite3
from contextlib import contextmanager

DB_NAME = "smh.db"

def initialize_database():
    """
    Initialize the SQLite database with required settings.
    Enforces foreign key constraints.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        print("[SMH] Database initialized with foreign key enforcement.")

@contextmanager
def get_connection():
    """
    Context manager to get a database connection.
    Automatically enables foreign keys and closes connection after use.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    try:
        yield conn
    finally:
        conn.close()
        print("[SMH] Database connection closed.")

