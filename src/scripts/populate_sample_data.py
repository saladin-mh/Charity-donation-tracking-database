# src/scripts/populate_sample_data.py

import sys
import os
# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from db.db_manager import get_connection

# Sample data to insert
donors = [
    ("Alice", "Smith", "Alice Bakery", "M1 2AB", "15", "07123456789"),
    ("Bob", "Brown", "Bob Logistics", "M2 3CD", "22", "07234567890"),
    ("Charlie", "Davis", None, "M3 4EF", "8", "07345678901"),
    ("Diana", "Evans", "Diana Co.", "M4 5GH", "19", "07456789012"),
    ("Edward", "Green", None, "M5 6IJ", "2", "07567890123")
]

volunteers = [
    ("Fiona", "Hall", "07678901234"),
    ("George", "Ivy", "07789012345"),
    ("Hannah", "Jones", "07890123456"),
    ("Ian", "King", "07901234567"),
    ("Julia", "Lewis", "07012345678")
]

events = [
    ("Charity Gala", "Main Hall", "2025-06-10 19:00:00", 500.0),
    ("Bake Sale", "Community Room", "2025-05-15 09:00:00", 50.0),
    ("Fun Run", "Park", "2025-07-20 10:00:00", 100.0),
    ("Auction Night", "Hotel Venue", "2025-08-30 18:00:00", 250.0),
    ("Music Festival", "Open Grounds", "2025-09-25 15:00:00", 1000.0)
]

contact_preferences = [
    (1, "email", 1),
    (2, "phone", 0),
    (3, "post", 1),
    (4, "email", 0),
    (5, "phone", 1)
]

event_sponsors = [
    ("Global Corp", 1, 1000.0),
    ("Foodies Ltd", 2, 300.0),
    ("RunFast", 3, 500.0),
    ("Luxury Auctions", 4, 800.0),
    ("Festival World", 5, 1500.0)
]

donations = [
    (50.0, "2025-05-01", True, "First Donation", 1, 1, 1),
    (25.0, "2025-05-01", False, "Anonymous", 2, 2, 2),
    (100.0, "2025-05-02", True, "Big Support", 3, 3, None),
    (75.0, "2025-05-03", False, "", 4, 4, 4),
    (200.0, "2025-05-04", True, "Generous Donor", 5, 5, 5)
]

# Insert into database
def populate_database():
    with get_connection() as conn:
        cursor = conn.cursor()

        # Insert donors
        cursor.executemany("""
            INSERT INTO donors (first_name, surname, business_name, postcode, house_number, phone_number)
            VALUES (?, ?, ?, ?, ?, ?);
        """, donors)

        # Insert volunteers
        cursor.executemany("""
            INSERT INTO volunteers (first_name, surname, phone_number)
            VALUES (?, ?, ?);
        """, volunteers)

        # Insert events
        cursor.executemany("""
            INSERT INTO events (event_name, room_info, booking_datetime, cost)
            VALUES (?, ?, ?, ?);
        """, events)

        # Insert contact preferences
        cursor.executemany("""
            INSERT INTO contact_preferences (donor_id, preferred_contact_method, newsletter_subscription)
            VALUES (?, ?, ?);
        """, contact_preferences)

        # Insert event sponsors
        cursor.executemany("""
            INSERT INTO event_sponsors (sponsor_name, event_id, amount_contributed)
            VALUES (?, ?, ?);
        """, event_sponsors)

        # Insert donations
        cursor.executemany("""
            INSERT INTO donations (amount, donation_date, gift_aid, notes, donor_id, event_id, volunteer_id)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, donations)

        conn.commit()
        print("[SMH] Sample data inserted successfully.")

if __name__ == "__main__":
    populate_database()
    print("[SMH] Sample data population script executed directly.")
