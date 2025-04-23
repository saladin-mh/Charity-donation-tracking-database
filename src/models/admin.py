import sqlite3
import bcrypt
from db.db_manager import get_connection

class AdminUser:

    @staticmethod
    def create(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        cursor.execute("INSERT INTO admin_users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()

    @staticmethod
    def authenticate(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM admin_users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.checkpw(password.encode(), result[0].encode()):
            return True
        return False
