"""
Donor model for the SMH Charity Donation Tracker.
Handles CRUD operations for donors, using sqlite3 for database access.
"""

import sqlite3
from db.db_manager import get_connection

class Donor:
    """Provides static methods for managing donor records in the database."""

    @staticmethod
    def create(first_name, surname, business_name, postcode, house_number, phone_number):
        """Insert a new donor into the database."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donors (
                    first_name, surname, business_name, postcode, house_number, phone_number
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (first_name, surname, business_name, postcode, house_number, phone_number))
            conn.commit()

    @staticmethod
    def read_all():
        """Fetch all donor records."""
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donors")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(donor_id):
        """Fetch a donor by their ID."""
        with get_connection() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donors WHERE donor_id = ?", (donor_id,))
            return cursor.fetchone()

    @staticmethod
    def update(donor_id, first_name, surname, business_name, postcode, house_number, phone_number):
        """Update donor details."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE donors
            SET first_name = ?, surname = ?, business_name = ?, postcode = ?,
                house_number = ?, phone_number = ?
            WHERE id = ?
        """, (first_name, surname, business_name, postcode, house_number, phone_number, donor_id))
        conn.commit()


    @staticmethod
    def delete(donor_id):
        """Delete a donor, if they have no associated donations."""
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM donors WHERE donor_id = ?", (donor_id,))
                conn.commit()
        except sqlite3.IntegrityError:
            print("⚠️ Unable to delete donor: existing donation references must be removed first.")
