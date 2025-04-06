from typing import Dict, Any
from database import Database

class RoomModel:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor
        self.conn = db.conn

    def add(self, room_data: Dict[str, Any]) -> int:
        """Add a new room to the database"""
        sql = '''
            INSERT INTO rooms (room_name, capacity, hourly_rate)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(sql, (
            room_data['room_name'],
            room_data['capacity'],
            room_data['hourly_rate']
        ))
        self.conn.commit()
        return self.cursor.lastrowid