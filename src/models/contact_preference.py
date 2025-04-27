from db.db_manager import get_connection

class ContactPreference:
    """
    Represents the contact preferences for a donor.

    Attributes:
        donor_id (int): ID of the donor.
        contact_method (str): Preferred method of contact (email, phone, post).
        newsletter_subscription (bool): Whether the donor subscribes to newsletters.
    """

    @staticmethod
    def create(donor_id, contact_method, newsletter_subscription):
        """Create a new contact preference entry."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO contact_preferences (donor_id, contact_method, newsletter_subscription)
                VALUES (?, ?, ?)
            """, (donor_id, contact_method, newsletter_subscription))
            conn.commit()

    @staticmethod
    def read_all():
        """Retrieve all contact preference records."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contact_preferences")
            return cursor.fetchall()

    @staticmethod
    def delete(preference_id):
        """Delete a contact preference record by ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contact_preferences WHERE preference_id = ?",
                            (preference_id,))
            conn.commit()

    @staticmethod
    def update(preference_id, contact_method, newsletter_subscription):
        """Update an existing contact preference."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE contact_preferences
                SET contact_method = ?, newsletter_subscription = ?
                WHERE preference_id = ?
            """, (contact_method, newsletter_subscription, preference_id))
            conn.commit()
