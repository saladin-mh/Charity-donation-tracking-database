import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import bcrypt
from db.db_manager import get_connection

class AdminUser:
    """
    AdminUser class provides methods for managing admin user authentication.
    Methods:
        create(username: str, password: str) -> None:
            Creates a new admin user with the given username and password.
            The password is securely hashed before being stored in the database.
        authenticate(username: str, password: str) -> bool:
            Authenticates an admin user by verifying the provided password
            against the stored hashed password in the database.
    Raises:
        Any database-related exceptions that may occur during the execution
        of the methods.
    """

    @staticmethod
    def create(username, password):
        with get_connection() as conn:
            cursor = conn.cursor()
            password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            cursor.execute("INSERT INTO admin_users (username, password_hash) VALUES (?, ?)",
                            (username, password_hash)
            )
            conn.commit()

    @staticmethod
    def authenticate(username, password):
        """Authenticate admin credentials using hashed password."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM admin_users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row and bcrypt.checkpw(password.encode(), row[0]):
                return True
        return False
