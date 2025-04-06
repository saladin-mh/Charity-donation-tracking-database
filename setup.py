from database import Database
from interface import Interface

def initialize_database():
    """Initialize the database and create all necessary tables"""
    db = Database()
    ui = Interface()
    
    ui.print_info("Initializing database...")
    
    try:
        db.setup_database()
        ui.print_success("Database initialized successfully!")
    except Exception as e:
        ui.print_error(f"Error initializing database: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    initialize_database()