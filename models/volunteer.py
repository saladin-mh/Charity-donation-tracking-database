from typing import Dict, Any, Optional
from database import Database

class VolunteerModel:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor
        self.conn = db.conn

    def add(self, volunteer_data: Dict[str, Any]) -> int:
        """Add a new volunteer to the database"""
        sql = '''
            INSERT INTO volunteers (
                first_name, surname, email, phone_number, join_date, status
            ) VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (
            volunteer_data['first_name'],
            volunteer_data['surname'],
            volunteer_data['email'],
            volunteer_data['phone_number'],
            volunteer_data['join_date'],
            volunteer_data.get('status', 'Active')
        ))
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, volunteer_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a volunteer by ID"""
        self.cursor.execute('SELECT * FROM volunteers WHERE volunteer_id = ?', (volunteer_id,))
        result = self.cursor.fetchone()
        if result:
            return dict(zip([col[0] for col in self.cursor.description], result))
        return None