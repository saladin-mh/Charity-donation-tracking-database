from db.db_manager import get_connection

class EventSponsor:
    """
    Represents a sponsor associated with an event.

    Attributes:
        sponsor_name (str): Name of the sponsor.
        event_id (int): ID of the event sponsored.
        amount_contributed (float): Amount contributed by the sponsor.
    """

    @staticmethod
    def create(sponsor_name, event_id, amount_contributed):
        """Create a new event sponsor entry."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO event_sponsors (sponsor_name, event_id, amount_contributed)
                VALUES (?, ?, ?)
            """, (sponsor_name, event_id, amount_contributed))
            conn.commit()

    @staticmethod
    def read_all():
        """Retrieve all event sponsor records."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM event_sponsors")
            return cursor.fetchall()

    @staticmethod
    def delete(sponsor_id):
        """Delete an event sponsor record by ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM event_sponsors WHERE sponsor_id = ?",
                            (sponsor_id,))
            conn.commit()

    @staticmethod
    def update(sponsor_id, sponsor_name, amount_contributed):
        """Update an existing event sponsor's details."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE event_sponsors
                SET sponsor_name = ?, amount_contributed = ?
                WHERE sponsor_id = ?
            """, (sponsor_name, amount_contributed, sponsor_id))
            conn.commit()
