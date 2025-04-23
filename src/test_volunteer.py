"""
Test script for the Volunteer model in the SMH application.

Initialises the database, inserts a sample volunteer,
and displays all volunteer records to verify model logic.
"""

from db.db_manager import initialize_database
from models.volunteer import Volunteer


def run_test():
    """Run a basic test to verify volunteer creation and listing."""
    print("[SMH TEST] Initialising database...")
    initialize_database()

    print("[SMH TEST] Adding volunteer...")
    Volunteer.create(
        first_name="Jenny",
        surname="Helpinghands",
        phone_number="0740000000"
    )

    print("[SMH TEST] All volunteers:")
    volunteers = Volunteer.read_all()
    for v in volunteers:
        print(dict(v))

    print("[SMH TEST] Test completed.")


if __name__ == "__main__":
    run_test()
