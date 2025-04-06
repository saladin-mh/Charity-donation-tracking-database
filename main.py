from database import Database
from models.donor import DonorModel
from models.volunteer import VolunteerModel
from models.room import RoomModel
from models.event import EventModel
from models.donation import DonationModel
from interface import Interface
from setup import initialize_database
from datetime import datetime

def main():
    """Main function to demonstrate the database functionality"""
    # Initialize database first
    if not initialize_database():
        return
    
    db = Database()
    ui = Interface()
    
    # Initialize models
    donor_model = DonorModel(db)
    volunteer_model = VolunteerModel(db)
    room_model = RoomModel(db)
    event_model = EventModel(db)
    donation_model = DonationModel(db)
    
    ui.clear_screen()
    ui.print_header("Charity Donation Management System")
    
    # Example usage with colored output
    ui.print_info("Creating test data...")
    
    # Add a volunteer
    volunteer_data = {
        'first_name': 'John',
        'surname': 'Doe',
        'email': 'john.doe@example.com',
        'phone_number': '07700900000',
        'join_date': '2023-01-01',
        'status': 'Active'
    }
    volunteer_id = volunteer_model.add(volunteer_data)
    ui.print_success(f"Added volunteer with ID: {volunteer_id}")
    
    # Add a donor
    donor_data = {
        'first_name': 'Jane',
        'surname': 'Smith',
        'business_name': None,
        'postcode': 'AB12 3CD',
        'house_number': '42',
        'phone_number': '07700900001',
        'donor_type': 'Individual'
    }
    donor_id = donor_model.add(donor_data)
    ui.print_success(f"Added donor with ID: {donor_id}")
    
    # Add a room
    room_data = {
        'room_name': 'Main Hall',
        'capacity': 100,
        'hourly_rate': 50.00
    }
    room_id = room_model.add(room_data)
    ui.print_success(f"Added room with ID: {room_id}")
    
    # Add an event
    event_data = {
        'event_name': 'Summer Fundraiser',
        'room_id': room_id,
        'event_date': '2023-07-01',
        'start_time': '14:00',
        'end_time': '17:00',
        'cost': 150.00,
        'coordinator_id': volunteer_id
    }
    event_id = event_model.add(event_data)
    ui.print_success(f"Added event with ID: {event_id}")
    
    # Add a donation
    donation_data = {
        'amount': 100.00,
        'donation_date': '2023-07-01',
        'source_type': 'Event',
        'donor_id': donor_id,
        'event_id': event_id,
        'gift_aid': True,
        'notes': 'First time donor',
        'recorded_by': volunteer_id
    }
    donation_id = donation_model.add(donation_data)
    ui.print_success(f"Added donation with ID: {donation_id}")
    
    # Search for donations
    ui.print_header("Searching for donations")
    donations = donation_model.search(donor_id=donor_id)
    
    # Display results in a table
    if donations:
        headers = ['ID', 'Amount', 'Date', 'Donor', 'Event']
        rows = [
            [d['donation_id'], f"£{d['amount']:.2f}", d['donation_date'], 
             d['donor_name'], d['event_name'] or 'Direct']
            for d in donations
        ]
        ui.print_table(headers, rows)
    else:
        ui.print_info("No donations found")
    
    # Try to delete a donor with donations (should fail)
    ui.print_header("Testing deletion rules")
    if not donor_model.delete(donor_id):
        ui.print_error("Cannot delete donor - they have associated donations")
    
    # Update donation
    ui.print_header("Updating donation")
    update_data = {
        'amount': 150.00,
        'notes': 'Updated donation amount'
    }
    if donation_model.update(donation_id, update_data):
        ui.print_success("Donation updated successfully")
    
    ui.print_success("\nDatabase operations completed successfully!")

if __name__ == "__main__":
    main()