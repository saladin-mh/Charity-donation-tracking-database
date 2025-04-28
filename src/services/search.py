"""
Search services for SMH Charity Donation Tracker.

Provides lookup functionality to retrieve donations by:
- Donor name (first or last)
- Event name
- Volunteer name (first or last)

Supports partial matches via SQL LIKE queries.
"""

from db.db_manager import get_connection

def search_donations_by_donor_name(name_query):
    """
    Search for donations made by donors matching the given name.

    Args:
        name_query (str): Part or full first/last name of the donor.

    Returns:
        list of sqlite3.Row: Matching donation records.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, dn.first_name, dn.surname
            FROM donations d
            JOIN donors dn ON d.donor_id = dn.donor_id
            WHERE dn.first_name LIKE ? OR dn.surname LIKE ?
        """, (f"%{name_query}%", f"%{name_query}%"))
        return cursor.fetchall()

def search_donations_by_event_name(event_query):
    """
    Search for donations associated with a specific event name.

    Args:
        event_query (str): Part or full name of the event.

    Returns:
        list of sqlite3.Row: Matching donation records.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, e.event_name
            FROM donations d
            JOIN events e ON d.event_id = e.event_id
            WHERE e.event_name LIKE ?
        """, (f"%{event_query}%",))
        return cursor.fetchall()

def search_donations_by_volunteer_name(vol_query):
    """
    Search for donations recorded by a volunteer.

    Args:
        vol_query (str): Part or full first/last name of the volunteer.

    Returns:
        list of sqlite3.Row: Matching donation records.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, v.first_name, v.surname
            FROM donations d
            JOIN volunteers v ON d.volunteer_id = v.volunteer_id
            WHERE v.first_name LIKE ? OR v.surname LIKE ?
        """, (f"%{vol_query}%", f"%{vol_query}%"))
        return cursor.fetchall()
