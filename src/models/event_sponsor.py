from db.db_manager import get_connection

class EventSponsor:
    """
    A class to manage CRUD operations for event sponsors in the database.
    Methods:
        create(event_id, sponsor_name, contribution_type, contribution_value):
            Inserts a new sponsor record into the event_sponsors table.
        read_all():
            Retrieves all sponsor records from the event_sponsors table.
        update(sponsor_id, sponsor_name, contribution_type, contribution_value):
            Updates an existing sponsor record in the event_sponsors table.
        delete(sponsor_id):
            Deletes a sponsor record from the event_sponsors table.
    """
    @staticmethod
    def create(event_id, sponsor_name, contribution_type, contribution_value):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO event_sponsors (event_id, sponsor_name, contribution_type, contribution_value)
                VALUES (?, ?, ?, ?)
            """, (event_id, sponsor_name, contribution_type, contribution_value))
            conn.commit()

    @staticmethod
    def read_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM event_sponsors")
            return cursor.fetchall()

    @staticmethod
    def update(sponsor_id, sponsor_name, contribution_type, contribution_value):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE event_sponsors
                SET sponsor_name = ?, contribution_type = ?, contribution_value = ?
                WHERE sponsor_id = ?
            """, (sponsor_name, contribution_type, contribution_value, sponsor_id))
            conn.commit()

    @staticmethod
    def delete(sponsor_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM event_sponsors WHERE sponsor_id = ?", (sponsor_id,))
            conn.commit()
