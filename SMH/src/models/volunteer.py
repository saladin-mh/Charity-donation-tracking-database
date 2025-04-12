# src/models/volunteer.py

from db.db_manager import get_connection

class Volunteer:
    @staticmethod
    def create(first_name, last_name, phone_number=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO volunteers (first_name, last_name, phone_number)
                VALUES (?, ?, ?)
            """, (first_name, last_name, phone_number))
            conn.commit()
            print(f"[✔] Volunteer '{first_name} {last_name}' added.")

    @staticmethod
    def read_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM volunteers")
            return cursor.fetchall()

    @staticmethod
    def read_by_id(volunteer_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM volunteers WHERE volunteer_id = ?", (volunteer_id,))
            return cursor.fetchone()

    @staticmethod
    def update(volunteer_id, first_name=None, last_name=None, phone_number=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE volunteers
                SET first_name = COALESCE(?, first_name),
                    last_name = COALESCE(?, last_name),
                    phone_number = COALESCE(?, phone_number)
                WHERE volunteer_id = ?
            """, (first_name, last_name, phone_number, volunteer_id))
            conn.commit()
            print(f"[✔] Volunteer ID {volunteer_id} updated.")

    @staticmethod
    def delete(volunteer_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM volunteers WHERE volunteer_id = ?", (volunteer_id,))
                conn.commit()
                print(f"[✔] Volunteer ID {volunteer_id} deleted.")
            except Exception as e:
                print(f"[✖] Cannot delete Volunteer ID {volunteer_id}: {e}")
