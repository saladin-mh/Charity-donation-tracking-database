# src/models/event.py

"""
Event model for SMH Charity Donation Tracker.

Supports operations to manage events including creation,
retrieval, updating and deletion. Each event may be
linked to donations via foreign key constraints.
"""

from db.db_manager import get_connection


class Event:
    @staticmethod
    def create(event_name, room_info, booking_datetime, cost):
        """
        Add a new event to the database.

        Parameters:
        - event_name (str): The name or title of the event.
        - room_info (str): Location or room details.
        - booking_datetime (str): Date and time in 'YYYY-MM-DD HH:MM:SS' format.
        - cost (float): The financial cost to host the event.
        """
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
        """
        Retrieve all events from the database.

        Returns:
            list of sqlite3.Row: Each row represents an event.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM events")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(event_id):
        """
        Fetch a specific event using its ID.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM events WHERE event_id = ?", (event_id,))
            return cursor.fetchone()

    @staticmethod
    def update(event_id, event_name=None, room_info=None, booking_datetime=None, cost=None):
        """
        Update details of an existing event.

        Uses COALESCE to preserve original values if no new data is provided.
        """
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
        """
        Attempt to delete an event by ID.

        Will fail if the event is referenced by any donation.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM events WHERE event_id = ?", (event_id,))
                conn.commit()
                print(f"[✔] Event ID {event_id} deleted.")
            except Exception as e:
                print(f"[✖] Cannot delete Event ID {event_id}: {e}")
