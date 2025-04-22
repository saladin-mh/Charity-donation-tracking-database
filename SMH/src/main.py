# src/main.py

import sys
import os
from services import search

# Add root project path to sys.path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import getpass
from models.donor import Donor
from models.volunteer import Volunteer
from models.event import Event
from models.donation import Donation
from db.db_manager import initialize_database

ADMIN_PASSWORD = "1234"

def display_banner():
    print("\n" + "*" * 47)
    print("*    Welcome to SMH Charity Tracker   *")
    print("*         ❤️  Making Change ❤️         *")
    print("*" * 47 + "\n")

def login():
    password = getpass.getpass("Please log in:\nPassword: ")
    if password == ADMIN_PASSWORD:
        print("\n✅ Login successful.\n")
        return True
    else:
        print("❌ Incorrect password. Access denied.")
        return False

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Donors")
        print("2. Manage Events")
        print("3. Manage Volunteers")
        print("4. Manage Donations")
        print("5. Search Donations")
        print("6. Exit")

        choice = input("Select an option (1-5): ")
        if choice == "1":
            donor_menu()
        elif choice == "2":
            event_menu()
        elif choice == "3":
            volunteer_menu()
        elif choice == "4":
            donation_menu()
        elif choice == "5":
            search_menu()
        elif choice == "6":
            print("👋 Exiting SMH. Goodbye!")
            break
        else:
            print("⚠️ Invalid selection. Please try again.")

# ----------- Submenus -----------

def donor_menu():
    while True:
        print("\n--- Donor Menu ---")
        print("1. Add Donor")
        print("2. View All Donors")
        print("3. Delete Donor")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Donor.create(
                input("First name: "),
                input("Surname: "),
                input("Business name: "),
                input("Postcode: "),
                input("House number: "),
                input("Phone number: ")
            )
        elif choice == "2":
            for d in Donor.read_all():
                print(dict(d))
        elif choice == "3":
            Donor.delete(int(input("Enter Donor ID to delete: ")))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def volunteer_menu():
    while True:
        print("\n--- Volunteer Menu ---")
        print("1. Add Volunteer")
        print("2. View All Volunteers")
        print("3. Delete Volunteer")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Volunteer.create(
                input("First name: "),
                input("Last name: "),
                input("Phone number: ")
            )
        elif choice == "2":
            for v in Volunteer.read_all():
                print(dict(v))
        elif choice == "3":
            Volunteer.delete(int(input("Enter Volunteer ID to delete: ")))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def event_menu():
    while True:
        print("\n--- Event Menu ---")
        print("1. Add Event")
        print("2. View All Events")
        print("3. Delete Event")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Event.create(
                input("Event name: "),
                input("Room info: "),
                input("Booking date/time (YYYY-MM-DD HH:MM:SS): "),
                float(input("Cost: "))
            )
        elif choice == "2":
            for e in Event.read_all():
                print(dict(e))
        elif choice == "3":
            Event.delete(int(input("Enter Event ID to delete: ")))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

def donation_menu():
    while True:
        print("\n--- Donation Menu ---")
        print("1. Add Donation")
        print("2. View All Donations")
        print("3. Delete Donation")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Donation.create(
                float(input("Amount: ")),
                input("Donation date (YYYY-MM-DD): "),
                input("Gift Aid (True/False): ").strip().lower() in ["true", "1", "yes"],
                input("Notes: "),
                int(input("Donor ID (or 0 to skip): ")) or None,
                int(input("Event ID (or 0 to skip): ")) or None,
                int(input("Volunteer ID (or 0 to skip): ")) or None
            )
        elif choice == "2":
            for d in Donation.read_all():
                print(dict(d))
        elif choice == "3":
            Donation.delete(int(input("Enter Donation ID to delete: ")))
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def search_menu():
    """CLI menu for searching donations by donor, volunteer, or event."""
    while True:
        print("\n--- Search Donations ---")
        print("1. By Donor Name")
        print("2. By Event Name")
        print("3. By Volunteer Name")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter donor name to search: ")
            results = search.search_donations_by_donor_name(name)
        elif choice == "2":
            name = input("Enter event name to search: ")
            results = search.search_donations_by_event_name(name)
        elif choice == "3":
            name = input("Enter volunteer name to search: ")
            results = search.search_donations_by_volunteer_name(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
            continue

        print(f"\nFound {len(results)} result(s):")
        for r in results:
            print(dict(r))


# ---------- Entry Point ----------

def main():
    display_banner()
    if login():
        initialize_database()
        main_menu()

if __name__ == "__main__":
    main()