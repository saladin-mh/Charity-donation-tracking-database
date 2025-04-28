import sqlite3
import os
from contextlib import contextmanager

# Define the database file location relative to this script
DB_NAME = os.path.join(os.path.dirname(__file__), "smh.db")

def initialize_database():
    """
    Initialises the SQLite database with the required settings.
    Enforces foreign key constraints and creates all necessary tables if they don't exist.
    """
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        # Create Donors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS donors (
                donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                surname TEXT NOT NULL,
                business_name TEXT,
                postcode TEXT,
                house_number TEXT,
                phone_number TEXT
            );
        """)

        # Create Events table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_name TEXT NOT NULL,
                room_info TEXT,
                booking_datetime DATETIME NOT NULL,
                cost REAL NOT NULL CHECK (cost >= 0)
            );
        """)

        # Create Volunteers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volunteers (
                volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                surname TEXT NOT NULL,
                phone_number TEXT
            );
        """)

        # Create Donations table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS donations (
                donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL CHECK (amount > 0),
                donation_date DATE NOT NULL,
                gift_aid BOOLEAN DEFAULT 0,
                notes TEXT,
                donor_id INTEGER,
                event_id INTEGER,
                volunteer_id INTEGER,
                FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE RESTRICT,
                FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE RESTRICT,
                FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE SET NULL
            );
        """)

        # Create Admin Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS admin_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            );
        """)

        # Create Contact Preferences table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contact_preferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                donor_id INTEGER NOT NULL,
                preferred_contact_method TEXT NOT NULL,
                newsletter_subscription INTEGER NOT NULL CHECK (newsletter_subscription IN (0,1)),
                FOREIGN KEY (donor_id) REFERENCES donors(donor_id) ON DELETE CASCADE
            );
        """)

        # Create Event Sponsors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS event_sponsors (
                sponsor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                sponsor_name TEXT NOT NULL,
                event_id INTEGER NOT NULL,
                amount_contributed REAL NOT NULL CHECK (amount_contributed >= 0),
                FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
            );
        """)

        print("[SMH] Database initialised with all tables created.")

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
