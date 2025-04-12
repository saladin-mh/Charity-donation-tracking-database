# src/models/event.py

from db.db_manager import get_connection

class Event:
    @staticmethod
    def create(event_name, room_info, booking_datetime, cost):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO events (event_name, room_info, booking_datetime, cost)
                VALUES (?, ?, ?, ?)
            """, (event_name, room_info, booking_datetime, cost))
            conn.commit()
            print(f"[✔] Event '{event_name}' added.")

    @staticmethod
    def read_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM events")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(event_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM events WHERE event_id = ?", (event_id,))
            return cursor.fetchone()

    @staticmethod
    def update(event_id, event_name=None, room_info=None, booking_datetime=None, cost=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE events
                SET event_name = COALESCE(?, event_name),
                    room_info = COALESCE(?, room_info),
                    booking_datetime = COALESCE(?, booking_datetime),
                    cost = COALESCE(?, cost)
                WHERE event_id = ?
            """, (event_name, room_info, booking_datetime, cost, event_id))
            conn.commit()
            print(f"[✔] Event ID {event_id} updated.")

    @staticmethod
    def delete(event_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM events WHERE event_id = ?", (event_id,))
                conn.commit()
                print(f"[✔] Event ID {event_id} deleted.")
            except Exception as e:
                print(f"[✖] Cannot delete Event ID {event_id}: {e}")
                