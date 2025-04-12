# src/models/donation.py

from db.db_manager import get_connection

class Donation:
    @staticmethod
    def create(amount, donation_date, gift_aid, notes,
               donor_id=None, event_id=None, volunteer_id=None):
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
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donations")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(donation_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donations WHERE donation_id = ?", (donation_id,))
            return cursor.fetchone()

    @staticmethod
    def update(donation_id, amount=None, donation_date=None, gift_aid=None, notes=None,
               donor_id=None, event_id=None, volunteer_id=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE donations
                SET amount = COALESCE(?, amount),
                    donation_date = COALESCE(?, donation_date),
                    gift_aid = COALESCE(?, gift_aid),
                    notes = COALESCE(?, notes),
                    donor_id = COALESCE(?, donor_id),
                    event_id = COALESCE(?, event_id),
                    volunteer_id = COALESCE(?, volunteer_id)
                WHERE donation_id = ?
            """, (amount, donation_date, gift_aid, notes,
                  donor_id, event_id, volunteer_id, donation_id))
            conn.commit()
            print(f"[✔] Donation ID {donation_id} updated.")

    @staticmethod
    def delete(donation_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM donations WHERE donation_id = ?", (donation_id,))
            conn.commit()
            print(f"[✔] Donation ID {donation_id} deleted.")