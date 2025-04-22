# src/models/volunteer.py

"""
Volunteer model for SMH Charity Donation Tracker.

Supports full CRUD operations for managing volunteers,
who may be linked to donation records via foreign keys.
"""

from db.db_manager import get_connection


class Volunteer:
    @staticmethod
    def create(first_name, last_name, phone_number=None):
        """
        Insert a new volunteer record into the database.

        Parameters:
        - first_name (str): The volunteer's given name.
        - last_name (str): The volunteer's surname.
        - phone_number (str): Optional contact number.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO volunteers (first_name, last_name, phone_number)
                VALUES (?, ?, ?)
            """, (first_name, last_name, phone_number))
            conn.commit()
            print(f"[✔] Volunteer '{first_name} {last_name}' added.")

    @staticmethod
    def read_all():
        """
        Fetch all volunteer records from the database.

        Returns:
            list: Rows as sqlite3.Row objects.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM volunteers")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(volunteer_id):
        """
        Retrieve a single volunteer record by their unique ID.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM volunteers WHERE volunteer_id = ?", (volunteer_id,))
            return cursor.fetchone()

    @staticmethod
    def update(volunteer_id, first_name=None, last_name=None, phone_number=None):
        """
        Update an existing volunteer's details.

        Fields left as None will retain existing values using COALESCE.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE volunteers
                SET first_name = COALESCE(?, first_name),
                    last_name = COALESCE(?, last_name),
                    phone_number = COALESCE(?, phone_number)
                WHERE volunteer_id = ?
            """, (first_name, last_name, phone_number, volunteer_id))
            conn.commit()
            print(f"[✔] Volunteer ID {volunteer_id} updated.")

    @staticmethod
    def delete(volunteer_id):
        """
        Attempt to delete a volunteer record.

        Will fail if the volunteer is referenced in the donations table.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM volunteers WHERE volunteer_id = ?", (volunteer_id,))
                conn.commit()
                print(f"[✔] Volunteer ID {volunteer_id} deleted.")
            except Exception as e:
                print(f"[✖] Cannot delete Volunteer ID {volunteer_id}: {e}")