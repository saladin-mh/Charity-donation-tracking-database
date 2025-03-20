from db_connection import connect_db

def create_donors_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Donors(
                   donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NUL,
                   business_name TEXT,
                   postcode TEXT,
                   house_number TEXT,
                   phone_number TEXT
                   )''')
    conn.commit()
    conn.close()