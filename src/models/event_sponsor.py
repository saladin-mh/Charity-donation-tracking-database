from db.db_manager import get_connection

class EventSponsor:
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
