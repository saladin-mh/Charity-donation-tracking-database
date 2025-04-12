# src/test_imports.py

import sys
import os

# ✅ Add the root of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.donor import Donor
from db.db_manager import initialize_database

def run_test():
    print("[SMH TEST] Starting database initialization...")
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
        print(dict(d))  # Convert sqlite3.Row to dict

if __name__ == "__main__":
    run_test()
    print("[SMH TEST] Test completed.")
    # This script is for testing purposes only.