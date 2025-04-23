"""
Event model for the SMH Charity Donation Tracker.

Manages CRUD operations on event data using SQLite3.
"""

import sqlite3
from db.db_manager import get_connection

class Event:
    """
    Provides static methods for creating, reading, updating, and deleting events
    in the charity database.
    """

    @staticmethod
    def create(event_name, room_info, booking_datetime, cost):
        """Insert a new event into the database."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO events (
                    event_name, room_info, booking_datetime, cost
                )
                VALUES (?, ?, ?, ?)
            """, (event_name, room_info, booking_datetime, cost))
            conn.commit()

    @staticmethod
    def read_all():
        """Fetch all event records."""
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM events")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(event_id):
        """Fetch an event by its ID."""
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM events WHERE event_id = ?", (event_id,))
            return cursor.fetchone()

    @staticmethod
    def update(event_id, event_name, room_info, booking_datetime, cost):
        """Update event information."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE events
                SET event_name = ?, room_info = ?, booking_datetime = ?, cost = ?
                WHERE event_id = ?
            """, (event_name, room_info, booking_datetime, cost, event_id))
            conn.commit()

    @staticmethod
    def delete(event_id):
        """Delete an event unless it is referenced by existing donations."""
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM events WHERE event_id = ?", (event_id,))
                conn.commit()
        except sqlite3.IntegrityError:
            print("⚠️ Cannot delete: donations are linked to this event.")
