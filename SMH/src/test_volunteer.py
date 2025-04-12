# src/test_volunteer.py

import sys
import os

# Add the root path so imports work cleanly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.volunteer import Volunteer
from db.db_manager import initialize_database

def run_test():
    print("[SMH TEST] Initializing DB...")
    initialize_database()

    print("[SMH TEST] Adding volunteer...")
    Volunteer.create(
        first_name="Jenny",
        last_name="Helpinghands",
        phone_number="0740000000"
    )

    print("[SMH TEST] All volunteers:")
    volunteers = Volunteer.read_all()
    for v in volunteers:
        print(dict(v))

if __name__ == "__main__":
    run_test()
    print("[SMH TEST] Test completed.")
    # This script is for testing purposes only.
    # It initializes the database and adds a test volunteer.
    # It then fetches and prints all volunteers from the database.
    # The test is run when the script is executed directly.