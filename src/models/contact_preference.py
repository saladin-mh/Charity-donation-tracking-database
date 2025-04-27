from db.db_manager import get_connection

class ContactPreference:
    """
    A class to manage donor contact preferences in the database.
    Methods:
        create(donor_id, contact_method, consent_given):
            Inserts a new contact preference record into the database.
        read_all():
            Retrieves all contact preference records from the database.
        update(preference_id, contact_method, consent_given):
            Updates an existing contact preference record in the database.
        delete(preference_id):
            Deletes a contact preference record from the database.
    """
    @staticmethod
    def create(donor_id, contact_method, consent_given):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO donor_contact_preferences (donor_id, contact_method, consent_given)
                VALUES (?, ?, ?)
            """, (donor_id, contact_method, consent_given))
            conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM donor_contact_preferences")
            return cursor.fetchall()

    @staticmethod
    def update(preference_id, contact_method, consent_given):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE donor_contact_preferences
                SET contact_method = ?, consent_given = ?
                WHERE preference_id = ?
            """, (contact_method, consent_given, preference_id))
            conn.commit()

    @staticmethod
    def delete(preference_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM donor_contact_preferences WHERE preference_id = ?",
                            (preference_id,))
            conn.commit()
