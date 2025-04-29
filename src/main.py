"""
Main CLI interface for the SMH Charity Donation Tracker system.
Allows admin users to manage donors, volunteers, events, and donations.
Supports full CRUD operations and integrated search functionality.
"""
import sys # Removed redundant reimport of 'sys'
import time  # Required for time.sleep in slow_print
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
from models.contact_preference import ContactPreference
from models.event_sponsor import EventSponsor

ADMIN_PASSWORD = "1234"

def slow_print(text, delay=0.01):
    """Prints text slowly like a typewriter."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end

def display_banner():
    banner_lines = [
        "╔══════════════════════════════════════════╗",
        "║{:^42}║".format("SMH CHARITY TRACKER"),
        "║{:^42}║".format("Empowering Donations, Changing Lives"),
        "╚══════════════════════════════════════════╝",
        "",
        "Welcome to the SMH Charity Donation Tracker!",
        "This system allows you to manage donors, events, volunteers, and donations.",
        "Please log in to access the admin features.\n",
    ]
    for line in banner_lines:
        slow_print(line)

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
            print("Goodbye! Exiting the application...")
            slow_print("Exiting in 3 seconds...", 0.5)  # Added a delay before exit
            time.sleep(3)
            sys.exit(0)  # Exit the program cleanly
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
            donors = Donor.read_all()
            if donors:
                headers = donors[0].keys()
                rows = [tuple(d) for d in donors]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No donors found.")
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
        # Removed unreachable else block

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
            volunteers = Volunteer.read_all()
            if volunteers:
                headers = volunteers[0].keys()
                rows = [tuple(v) for v in volunteers]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No volunteers found.")
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
            events = Event.read_all()
            if events:
                headers = events[0].keys()
                rows = [tuple(e) for e in events]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No events found.")
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
            donations = Donation.read_all()
            if donations:
                headers = donations[0].keys()
                rows = [tuple(d) for d in donations]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No donations found.")
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
    """Submenu for managing contact preference records."""
    while True:
        print("\n--- Contact Preferences Menu ---")
        print("1. Add Contact Preference")
        print("2. View All Preferences")
        print("3. Update Preference")
        print("4. Delete Preference")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            ContactPreference.create(
                int(input("Donor ID: ")),
                input("Preferred contact method (email/phone/post): "),
                int(input("Newsletter subscription (1 = Yes, 0 = No): "))
            )
        elif choice == "2":
            preferences = ContactPreference.read_all()
            if preferences:
                headers = preferences[0].keys()
                rows = [tuple(p) for p in preferences]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No contact preferences found.")
        elif choice == "3":
            ContactPreference.update(
                int(input("Preference ID: ")),
                input("New preferred contact method: "),
                int(input("Newsletter subscription (1 = Yes, 0 = No): "))
            )
        elif choice == "4":
            ContactPreference.delete(int(input("Enter Preference ID to delete: ")))
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def event_sponsor_menu():
    """Submenu for managing event sponsor records."""
    while True:
        print("\n--- Event Sponsor Menu ---")
        print("1. Add Sponsor")
        print("2. View All Sponsors")
        print("3. Update Sponsor")
        print("4. Delete Sponsor")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            EventSponsor.create(
                input("Sponsor Name: "),
                int(input("Event ID: ")),
                float(input("Amount Contributed: "))
            )
        elif choice == "2":
            sponsors = EventSponsor.read_all()
            if sponsors:
                headers = sponsors[0].keys()
                rows = [tuple(s) for s in sponsors]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No sponsors found.")
        elif choice == "3":
            EventSponsor.update(
                int(input("Sponsor ID: ")),
                input("New Sponsor Name: "),
                float(input("New Amount Contributed: "))
            )
        elif choice == "4":
            EventSponsor.delete(int(input("Enter Sponsor ID to delete: ")))
        elif choice == "5":
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
