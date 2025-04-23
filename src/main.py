"""
Main CLI interface for the SMH Charity Donation Tracker system.

Allows admin users to manage donors, volunteers, events, and donations.
Supports full CRUD operations and integrated search functionality.
"""
import sys
import os
import getpass

from tabulate import tabulate

# Ensure the project root (one level above /src) is in the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Grouped imports by module structure
from db.db_manager import initialize_database
from services import search
from models.admin import AdminUser
from models.donor import Donor
from models.volunteer import Volunteer
from models.event import Event
from models.donation import Donation

ADMIN_PASSWORD = "1234"

def display_banner():
    print("***************************************")
    print("*    Welcome to SMH Charity Tracker   *")
    print("*          ❤️   Making Change ❤️        *")
    print("***************************************")

def login():
    """Handles admin user login."""
    print("🔒 Admin Login")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if AdminUser.authenticate(username, password):
        print("Login successful!")
        return True
    print("Invalid credentials. Access denied.")
    return False



def main_menu():
    """Displays and handles the main navigation menu."""
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Donors")
        print("2. Manage Events")
        print("3. Manage Volunteers")
        print("4. Manage Donations")
        print("5. Search Donations")
        print("6. Exit")

        choice = input("Select an option (1-6): ")
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
    """Submenu for managing donor records."""
    while True:
        print("\n--- Donor Menu ---")
        print("1. Add Donor")
        print("2. View All Donors")
        print("3. Delete Donor")
        print("4. Update Donor")
        print("5. Back to Main Menu")
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
            donor_id = int(input("Enter Donor ID to update: "))
            first_name = input("New first name: ")
            surname = input("New surname: ")
            business_name = input("New business name: ")
            postcode = input("New postcode: ")
            house_number = input("New house number: ")
            phone_number = input("New phone number: ")
            Donor.update(donor_id, first_name, surname, business_name, postcode,
                          house_number, phone_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def volunteer_menu():
    """Submenu for managing volunteer records."""
    while True:
        print("\n--- Volunteer Menu ---")
        print("1. Add Volunteer")
        print("2. View All Volunteers")
        print("3. Delete Volunteer")
        print("4. Update Volunteer")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Volunteer.create(
                input("First name: "),
                input("Surname: "),
                input("Phone number: ")
            )
        elif choice == "2":
            for v in Volunteer.read_all():
                print(dict(v))
        elif choice == "3":
            Volunteer.delete(int(input("Enter Volunteer ID to delete: ")))
        elif choice == "4":
            volunteer_id = int(input("Enter Volunteer ID to update: "))
            first_name = input("New first name: ")
            surname = input("New surname: ")
            phone_number = input("New phone number: ")
            Volunteer.update(volunteer_id, first_name, surname, phone_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



def event_menu():
    """Submenu for managing event records."""
    while True:
        print("\n--- Event Menu ---")
        print("1. Add Event")
        print("2. View All Events")
        print("3. Delete Event")
        print("4. Update Event")
        print("5. Back to Main Menu")
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
            event_id = int(input("Enter Event ID to update: "))
            event_name = input("New event name: ")
            room_info = input("New room info: ")
            booking_datetime = input("New booking date/time (YYYY-MM-DD HH:MM:SS): ")
            cost = float(input("New cost: "))
            Event.update(event_id, event_name, room_info, booking_datetime, cost)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



def donation_menu():
    """Submenu for managing donation records."""
    while True:
        print("\n--- Donation Menu ---")
        print("1. Add Donation")
        print("2. View All Donations")
        print("3. Delete Donation")
        print("4. Update Donation")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Donation.create(
                float(input("Amount: ")),
                input("Donation date (YYYY-MM-DD): "),
                input("Gift Aid (True/False): ").lower() == "true",
                input("Notes: "),
                int(input("Donor ID: ")),
                int(input("Event ID: ")),
                int(input("Volunteer ID: "))
            )
        elif choice == "2":
            for d in Donation.read_all():
                print(dict(d))
        elif choice == "3":
            Donation.delete(int(input("Enter Donation ID to delete: ")))
        elif choice == "4":
            donation_id = int(input("Enter Donation ID to update: "))
            amount = float(input("New amount: "))
            donation_date = input("New donation date (YYYY-MM-DD): ")
            gift_aid = input("Gift Aid (True/False): ").lower() == "true"
            notes = input("New notes: ")
            donor_id = int(input("New Donor ID: "))
            event_id = int(input("New Event ID: "))
            volunteer_id = int(input("New Volunteer ID: "))
            Donation.update(donation_id, amount, donation_date, gift_aid, notes,
                            donor_id, event_id, volunteer_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")



def search_menu():
    """Submenu to search donations by donor, volunteer, or event."""
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
        if results:
            headers = results[0].keys()
            rows = [tuple(r) for r in results]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        else:
            print("No results found.")


def main():
    """Initialises the database and launches the application."""
    display_banner()
    if login():
        initialize_database()
        main_menu()


if __name__ == "__main__":
    main()
