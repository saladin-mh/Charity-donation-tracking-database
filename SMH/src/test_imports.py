# src/test_imports.py

"""
Test script to validate database connectivity and Donor model functionality.

Creates a test donor entry, then fetches and displays all donor records.
This serves as a unit verification for initial model and database access setup.
"""

import sys
import os

# Add the root of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.donor import Donor
from db.db_manager import initialize_database


def run_test():
    """Run test routine to insert and read donor data."""
    print("[SMH TEST] Starting database initialisation...")
    initialize_database()

    print("[SMH TEST] Creating a test donor...")
    Donor.create(
        first_name="Testy",
        surname="McTester",
        business_name="Test Co.",
        postcode="T3ST1NG",
        house_number="101",
        phone_number="123456789"
    )

    print("[SMH TEST] Fetching all donors:")
    donors = Donor.read_all()
    for d in donors:
        print(dict(d))  # Convert sqlite3.Row to readable dict

    print("[SMH TEST] Test completed.")


if __name__ == "__main__":
    run_test()
