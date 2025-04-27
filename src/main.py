"""
Main CLI interface for the SMH Charity Donation Tracker system.
Allows admin users to manage donors, volunteers, events, and donations.
Supports full CRUD operations and integrated search functionality.
"""
import sys
import os
import getpass
from tabulate import tabulate
from db.db_manager import get_connection

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
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Donors")
        print("2. Manage Events")
        print("3. Manage Volunteers")
        print("4. Manage Donations")
        print("5. Search Donations")
        print("6. Manage Contact Preferences")
        print("7. Manage Event Sponsors")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

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
            contact_preference_menu()
        elif choice == "7":
            event_sponsor_menu()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

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
        print("3. Update Volunteer")
        print("4. Delete Volunteer")
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
            Volunteer.update(
                int(input("Volunteer ID to update: ")),
                input("Updated First name: "),
                input("Updated Surname: "),
                input("Updated Phone number: ")
            )
        elif choice == "4":
            Volunteer.delete(int(input("Enter Volunteer ID to delete: ")))
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
        print("3. Update Event")
        print("4. Delete Event")
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
            Event.update(
                int(input("Enter Event ID to update: ")),
                input("New Event name: "),
                input("New Room info: "),
                input("New Booking date/time (YYYY-MM-DD HH:MM:SS): "),
                float(input("New Cost: "))
            )
        elif choice == "4":
            Event.delete(int(input("Enter Event ID to delete: ")))
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
        print("3. Update Donation")
        print("4. Delete Donation")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            Donation.create(
                float(input("Amount: ")),
                input("Donation date (YYYY-MM-DD): "),
                input("Gift Aid (yes/no): ").lower() == "yes",
                input("Notes: "),
                int(input("Donor ID: ")),
                int(input("Event ID: ")),
                int(input("Volunteer ID (or 0 if none): ")) or None
            )
        elif choice == "2":
            for d in Donation.read_all():
                print(dict(d))
        elif choice == "3":
            Donation.update(
                int(input("Donation ID to update: ")),
                float(input("New Amount: ")),
                input("New Donation date (YYYY-MM-DD): "),
                input("Gift Aid (yes/no): ").lower() == "yes",
                input("New Notes: "),
                int(input("New Donor ID: ")),
                int(input("New Event ID: ")),
                int(input("New Volunteer ID (or 0 if none): ")) or None
            )
        elif choice == "4":
            Donation.delete(int(input("Enter Donation ID to delete: ")))
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

def contact_preference_menu():
    """Submenu for managing donor contact preferences."""
    while True:
        print("\n--- Contact Preference Menu ---")
        print("1. Add Contact Preference")
        print("2. View All Contact Preferences")
        print("3. Delete Contact Preference")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            donor_id = int(input("Donor ID: "))
            method = input("Preferred Contact Method (Email/Phone/Post): ")
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO contact_preferences (donor_id, method)
                    VALUES (?, ?)
                """, (donor_id, method))
                conn.commit()
                print("Contact preference added successfully.")

        elif choice == "2":
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM contact_preferences")
                results = cursor.fetchall()
                for row in results:
                    print(dict(row))

        elif choice == "3":
            preference_id = int(input("Enter Contact Preference ID to delete: "))
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM contact_preferences WHERE preference_id = ?",
                               (preference_id,))
                conn.commit()
                print("Contact preference deleted successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

def event_sponsor_menu():
    """Submenu for managing event sponsors."""
    while True:
        print("\n--- Event Sponsor Menu ---")
        print("1. Add Event Sponsor")
        print("2. View All Event Sponsors")
        print("3. Delete Event Sponsor")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            event_id = int(input("Event ID: "))
            sponsor_name = input("Sponsor Name: ")
            contribution_amount = float(input("Contribution Amount: "))
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO event_sponsors (event_id, sponsor_name, contribution_amount)
                    VALUES (?, ?, ?)
                """, (event_id, sponsor_name, contribution_amount))
                conn.commit()
                print("Event sponsor added successfully.")

        elif choice == "2":
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM event_sponsors")
                results = cursor.fetchall()
                for row in results:
                    print(dict(row))

        elif choice == "3":
            sponsor_id = int(input("Enter Sponsor ID to delete: "))
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM event_sponsors WHERE sponsor_id = ?", (sponsor_id,))
                conn.commit()
                print("Event sponsor deleted successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")

def main():
    """Initialises the database and launches the application."""
    display_banner()
    if login():
        initialize_database()
        main_menu()

if __name__ == "__main__":
    main()
