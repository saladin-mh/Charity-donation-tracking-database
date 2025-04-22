"""
Volunteer model for the SMH Charity Donation Tracker.

Manages volunteer records, enabling creation, listing, updating, and deletion.
"""

import sqlite3
from db.db_manager import get_connection


class Volunteer:
    """
    Provides static methods to manage volunteer records
    within the charity database.
    """

    @staticmethod
    def create(first_name, last_name, phone_number):
        """Insert a new volunteer into the database."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO volunteers (
                    first_name, last_name, phone_number
                )
                VALUES (?, ?, ?)
            """, (first_name, last_name, phone_number))
            conn.commit()

    @staticmethod
    def read_all():
        """Return all volunteer records."""
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM volunteers")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(volunteer_id):
        """Fetch a volunteer by ID."""
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM volunteers WHERE volunteer_id = ?",
                (volunteer_id,)
            )
            return cursor.fetchone()

    @staticmethod
    def update(volunteer_id, first_name, last_name, phone_number):
        """Update volunteer information."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE volunteers
                SET first_name = ?, last_name = ?, phone_number = ?
                WHERE volunteer_id = ?
            """, (first_name, last_name, phone_number, volunteer_id))
            conn.commit()

    @staticmethod
    def delete(volunteer_id):
        """Delete a volunteer if not associated with donations."""
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM volunteers WHERE volunteer_id = ?", (volunteer_id,))
                conn.commit()
        except sqlite3.IntegrityError:
            print("⚠️ Cannot delete: donations reference this volunteer.")