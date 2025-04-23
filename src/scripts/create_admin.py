import sys
import os

# Append the project root to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import bcrypt
from db.db_manager import get_connection

def create_admin_user(username, password):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO admin_users (username, password_hash) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        print("✅ Admin user created.")

if __name__ == "__main__":
    create_admin_user("admin", "1234")

