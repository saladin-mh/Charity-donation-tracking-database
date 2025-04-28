# src/test_donation.py

"""
Test script for the SMH Charity Donation Tracker.

Initialises the database, inserts dummy donor, event, and volunteer,
and creates a test donation record for verification purposes.
"""

import sys
import os
from datetime import date

# Allow imports from the project root for modular testing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_manager import initialize_database
from models.donation import Donation
from models.donor import Donor
from models.volunteer import Volunteer
from models.event import Event


def run_test():
    """
    Executes a full donation workflow test:
    - Initialises the database
    - Adds linked donor, event, and volunteer
    - Creates and lists a donation entry
    """
    print("[SMH TEST] Starting donation test...")

    initialize_database()

    # Step 1: Create dummy data for relational linking
    Donor.create("Alice", "Goodheart", "GiveBack Inc", "G1 2XY", "42", "0781111111")
    Volunteer.create("Bob", "Helper", "0772222222")
    Event.create("Charity Gala", "Main Hall", "2025-05-01 18:00:00", 500.00)

    # Step 2: Retrieve last created records (simulate foreign key linkage)
    donor = Donor.read_all()[-1]
    volunteer = Volunteer.read_all()[-1]
    event = Event.read_all()[-1]

    # Step 3: Create a donation record linked to the above
    Donation.create(
        amount=100.00,
        donation_date=str(date.today()),
        gift_aid=True,
        notes="Test donation via event",
        donor_id=donor["donor_id"],
        event_id=event["event_id"],
        volunteer_id=volunteer["volunteer_id"]
    )

    # Step 4: Display all donations
    print("\n[SMH TEST] All Donations:")
    for donation in Donation.read_all():
        print(dict(donation))

    print("[SMH TEST] Test completed.")


if __name__ == "__main__":
    run_test()
    print("Test script executed directly.")
else:
    print("Test script imported as a module.")
    # This is useful for debugging or when running in an interactive environment.
