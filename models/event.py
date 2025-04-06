from typing import Dict, Any, Optional
from database import Database

class EventModel:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor
        self.conn = db.conn

    def add(self, event_data: Dict[str, Any]) -> int:
        """Add a new event to the database"""
        sql = '''
            INSERT INTO events (
                event_name, room_id, event_date, start_time,
                end_time, cost, coordinator_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (
            event_data['event_name'],
            event_data['room_id'],
            event_data['event_date'],
            event_data['start_time'],
            event_data['end_time'],
            event_data['cost'],
            event_data['coordinator_id']
        ))
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, event_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve an event by ID"""
        self.cursor.execute('''
            SELECT e.*, r.room_name, v.first_name || ' ' || v.surname as coordinator_name
            FROM events e
            LEFT JOIN rooms r ON e.room_id = r.room_id
            LEFT JOIN volunteers v ON e.coordinator_id = v.volunteer_id
            WHERE e.event_id = ?
        ''', (event_id,))
        result = self.cursor.fetchone()
        if result:
            return dict(zip([col[0] for col in self.cursor.description], result))
        return None

    def can_delete(self, event_id: int) -> bool:
        """Check if an event can be deleted (no associated donations)"""
        self.cursor.execute("SELECT COUNT(*) FROM donations WHERE event_id = ?", (event_id,))
        count = self.cursor.fetchone()[0]
        return count == 0

    def delete(self, event_id: int) -> bool:
        """Delete an event if it has no associated donations"""
        if not self.can_delete(event_id):
            return False
        self.cursor.execute("DELETE FROM events WHERE event_id = ?", (event_id,))
        self.conn.commit()
        return True