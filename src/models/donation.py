"""
Donation model for SMH Charity Donation Tracker.
Provides CRUD operations and maintains relationships
with donor, event, and volunteer records.
"""

from db.db_manager import get_connection

class Donation:
    """Handels donation records in the database."""
    @staticmethod
    def create(amount, donation_date, gift_aid, notes,
               donor_id=None, event_id=None, volunteer_id=None):
        """
        Insert a new donation record into the database.

        Parameters:
        - amount (float): Donation amount, must be > 0.
        - donation_date (str): Date of donation (YYYY-MM-DD).
        - gift_aid (bool): Whether the donation qualifies for Gift Aid.
        - notes (str): Any additional notes.
        - donor_id (int): FK reference to donor.
        - event_id (int): FK reference to event.
        - volunteer_id (int): FK reference to volunteer.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donations (
                    amount, donation_date, gift_aid, notes,
                    donor_id, event_id, volunteer_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (amount, donation_date, gift_aid, notes,
                  donor_id, event_id, volunteer_id))
            conn.commit()
            print(f"[✔] Donation of £{amount:.2f} added.")

    @staticmethod
    def read_all():
        """Fetch all donations from the database."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donations")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(donation_id):
        """Fetch a single donation by its ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donations WHERE donation_id = ?", (donation_id,))
            return cursor.fetchone()

    @staticmethod
    def update(donation_id, amount, donation_date, gift_aid, notes, donor_id,
               event_id, volunteer_id):
        """Update donation record."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE donations
                SET amount = ?, donation_date = ?, gift_aid = ?, notes = ?,
                    donor_id = ?, event_id = ?, volunteer_id = ?
                WHERE donation_id = ?
            """, (amount, donation_date, gift_aid, notes, donor_id, event_id,
                  volunteer_id, donation_id))
            conn.commit()

    @staticmethod
    def delete(donation_id):
        """Delete a donation by its ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM donations WHERE donation_id = ?", (donation_id,))
            conn.commit()
            print(f"[✔] Donation ID {donation_id} deleted.")
