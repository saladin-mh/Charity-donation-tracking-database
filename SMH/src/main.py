# src/main.py

import getpass
from db.db_manager import initialize_database

ADMIN_PASSWORD = "1234"

def display_welcome():
    print("\n" + "*" * 47)
    print("*    Welcome to SMH Charity Tracker   *")
    print("*         ❤️ Making Change ❤️         *")
    print("*" * 47 + "\n")

def login():
    for attempt in range(3):
        password = getpass.getpass("Please log in:\nPassword: ")
        if password == ADMIN_PASSWORD:
            print("\n✅ Login successful!\n")
            return True
        else:
            print("❌ Incorrect password. Try again.\n")
    print("🔒 Too many failed attempts. Exiting...")
    return False

def main():
    display_welcome()
    if not login():
        return
    initialize_database()
    # Later, this will call CLI navigation to CRUD functions
    print("[SMH] Ready to manage donations, events, and more!")

if __name__ == "__main__":
    main()
    # This will be the entry point for the CLI application.
    # Future CLI navigation and CRUD operations will be implemented here.   
    # For now, it initializes the database and handles login.
    # The main function is the entry point for the application.
    # It displays a welcome message, handles login, and initializes the database