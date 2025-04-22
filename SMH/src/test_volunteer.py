# src/test_volunteer.py

"""
Test script for the Volunteer model in the SMH application.

Initialises the database, inserts a sample volunteer,
and displays all volunteer records to verify model logic.
"""

import sys
import os

# Add the root path so imports work cleanly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.volunteer import Volunteer
from db.db_manager import initialize_database


def run_test():
    """Run a basic test to verify volunteer creation and listing."""
    print("[SMH TEST] Initialising DB...")
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
