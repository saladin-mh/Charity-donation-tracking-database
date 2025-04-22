# src/models/donor.py

"""
Donor model for SMH Charity Donation Tracker.

Provides database operations for creating, retrieving,
updating, and deleting donor records.
"""

from db.db_manager import get_connection


class Donor:
    @staticmethod
    def create(first_name, surname, business_name=None, postcode=None, house_number=None, phone_number=None):
        """
        Add a new donor to the database.

        All fields except first_name and surname are optional.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donors (first_name, surname, business_name, postcode, house_number, phone_number)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (first_name, surname, business_name, postcode, house_number, phone_number))
            conn.commit()
            print(f"[✔] Donor '{first_name} {surname}' added successfully.")

    @staticmethod
    def read_all():
        """
        Retrieve all donors from the database.

        Returns:
            list: All donor records as sqlite3.Row objects.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donors")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(donor_id):
        """
        Retrieve a specific donor by their unique ID.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donors WHERE donor_id = ?", (donor_id,))
            return cursor.fetchone()

    @staticmethod
    def update(donor_id, first_name=None, surname=None, business_name=None, postcode=None, house_number=None, phone_number=None):
        """
        Update donor information. Fields are optional.

        Existing values are preserved unless new data is provided.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE donors
                SET first_name = COALESCE(?, first_name),
                    surname = COALESCE(?, surname),
                    business_name = COALESCE(?, business_name),
                    postcode = COALESCE(?, postcode),
                    house_number = COALESCE(?, house_number),
                    phone_number = COALESCE(?, phone_number)
                WHERE donor_id = ?
            """, (first_name, surname, business_name, postcode, house_number, phone_number, donor_id))
            conn.commit()
            print(f"[✔] Donor ID {donor_id} updated.")

    @staticmethod
    def delete(donor_id):
        """
        Attempt to delete a donor record by ID.

        Will fail if the donor is linked to existing donations.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM donors WHERE donor_id = ?", (donor_id,))
                conn.commit()
                print(f"[✔] Donor ID {donor_id} deleted.")
            except Exception as e:
                print(f"[✖] Cannot delete Donor ID {donor_id}: {e}")
