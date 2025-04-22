# src/services/search.py

"""
Search services for SMH Charity Donation Tracker.
Provides lookup functionality by donor name, volunteer, or event.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from db.db_manager import get_connection



def search_donations_by_donor_name(name_query):
    """Search donations by donor's first or last name (partial match)."""
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
    """Search donations by associated event name (partial match)."""
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
    """Search donations by volunteer's first or last name (partial match)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, v.first_name, v.last_name
            FROM donations d
            JOIN volunteers v ON d.volunteer_id = v.volunteer_id
            WHERE v.first_name LIKE ? OR v.last_name LIKE ?
        """, (f"%{vol_query}%", f"%{vol_query}%"))
        return cursor.fetchall()
# src/services/search.py

"""
Search services for SMH Charity Donation Tracker.
Provides lookup functionality by donor name, volunteer, or event.
"""

from db.db_manager import get_connection


def search_donations_by_donor_name(name_query):
    """Search donations by donor's first or last name (partial match)."""
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
    """Search donations by associated event name (partial match)."""
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
    """Search donations by volunteer's first or last name (partial match)."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.*, v.first_name, v.last_name
            FROM donations d
            JOIN volunteers v ON d.volunteer_id = v.volunteer_id
            WHERE v.first_name LIKE ? OR v.last_name LIKE ?
        """, (f"%{vol_query}%", f"%{vol_query}%"))
        return cursor.fetchall()
