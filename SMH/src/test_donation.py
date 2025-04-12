# src/test_donation.py

import sys
import os
from datetime import date

# Allow imports from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.db_manager import initialize_database
from models.donation import Donation
from models.donor import Donor
from models.volunteer import Volunteer
from models.event import Event

def run_test():
    initialize_database()

    # Optional: Create dummy donor, event, volunteer for linking
    Donor.create("Alice", "Goodheart", "GiveBack Inc", "G1 2XY", "42", "0781111111")
    Volunteer.create("Bob", "Helper", "0772222222")
    Event.create("Charity Gala", "Main Hall", "2025-05-01 18:00:00", 500.00)

    donor = Donor.read_all()[-1]
    volunteer = Volunteer.read_all()[-1]
    event = Event.read_all()[-1]

    # Create donation linked to donor, event, and volunteer
    Donation.create(
        amount=100.00,
        donation_date=str(date.today()),
        gift_aid=True,
        notes="Test donation via event",
        donor_id=donor["donor_id"],
        event_id=event["event_id"],
        volunteer_id=volunteer["volunteer_id"]
    )

    # Show all donations
    print("\n[SMH TEST] All Donations:")
    for donation in Donation.read_all():
        print(dict(donation))

if __name__ == "__main__":
    run_test()
    print("[SMH TEST] Test completed.")
    # This script is for testing purposes only.
    # It initializes the database and adds a test donation.
    # It then fetches and prints all donations from the database. 