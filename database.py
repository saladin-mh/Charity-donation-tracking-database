import sqlite3
from typing import Optional

class Database:
    _instance: Optional['Database'] = None

    def __new__(cls, db_name: str = "charity.db"):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.db_name = db_name
            cls._instance.conn = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    def setup_database(self):
        """Create all necessary tables if they don't exist"""
        # Create Donor table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS donors (
                donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                surname TEXT NOT NULL,
                business_name TEXT,
                postcode TEXT NOT NULL,
                house_number TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                donor_type TEXT CHECK(donor_type IN ('Individual', 'Business')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create Volunteer table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS volunteers (
                volunteer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                surname TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone_number TEXT NOT NULL,
                join_date DATE NOT NULL,
                status TEXT CHECK(status IN ('Active', 'Inactive')) DEFAULT 'Active'
            )
        ''')

        # Create Room table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_name TEXT NOT NULL,
                capacity INTEGER NOT NULL,
                hourly_rate DECIMAL(10,2) NOT NULL
            )
        ''')

        # Create Event table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_name TEXT NOT NULL,
                room_id INTEGER,
                event_date DATE NOT NULL,
                start_time TIME NOT NULL,
                end_time TIME NOT NULL,
                cost DECIMAL(10,2) NOT NULL,
                coordinator_id INTEGER,
                FOREIGN KEY (room_id) REFERENCES rooms(room_id),
                FOREIGN KEY (coordinator_id) REFERENCES volunteers(volunteer_id)
            )
        ''')

        # Create Donation table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS donations (
                donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount DECIMAL(10,2) NOT NULL CHECK (amount > 0),
                donation_date DATE NOT NULL,
                source_type TEXT CHECK(source_type IN ('Event', 'Direct')) NOT NULL,
                donor_id INTEGER,
                event_id INTEGER,
                gift_aid BOOLEAN NOT NULL DEFAULT 0,
                notes TEXT,
                recorded_by INTEGER,
                FOREIGN KEY (donor_id) REFERENCES donors(donor_id),
                FOREIGN KEY (event_id) REFERENCES events(event_id),
                FOREIGN KEY (recorded_by) REFERENCES volunteers(volunteer_id)
            )
        ''')

        self.conn.commit()

    def __del__(self):
        """Close the database connection when the object is destroyed"""
        if hasattr(self, 'conn'):
            self.conn.close()