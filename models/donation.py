from typing import Dict, Any, List
from database import Database

class DonationModel:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor
        self.conn = db.conn

    def add(self, donation_data: Dict[str, Any]) -> int:
        """Add a new donation to the database"""
        sql = '''
            INSERT INTO donations (
                amount, donation_date, source_type, donor_id,
                event_id, gift_aid, notes, recorded_by
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (
            donation_data['amount'],
            donation_data['donation_date'],
            donation_data['source_type'],
            donation_data['donor_id'],
            donation_data.get('event_id'),
            donation_data['gift_aid'],
            donation_data.get('notes'),
            donation_data['recorded_by']
        ))
        self.conn.commit()
        return self.cursor.lastrowid

    def search(self, **kwargs) -> List[Dict[str, Any]]:
        """Search donations based on various criteria"""
        base_query = '''
            SELECT d.*, 
                   dn.first_name || ' ' || dn.surname as donor_name,
                   e.event_name,
                   v.first_name || ' ' || v.surname as recorded_by_name
            FROM donations d
            LEFT JOIN donors dn ON d.donor_id = dn.donor_id
            LEFT JOIN events e ON d.event_id = e.event_id
            LEFT JOIN volunteers v ON d.recorded_by = v.volunteer_id
            WHERE 1=1
        '''
        conditions = []
        params = []

        if 'donor_id' in kwargs:
            conditions.append('d.donor_id = ?')
            params.append(kwargs['donor_id'])
        if 'event_id' in kwargs:
            conditions.append('d.event_id = ?')
            params.append(kwargs['event_id'])
        if 'volunteer_id' in kwargs:
            conditions.append('d.recorded_by = ?')
            params.append(kwargs['volunteer_id'])
        if 'min_amount' in kwargs:
            conditions.append('d.amount >= ?')
            params.append(kwargs['min_amount'])
        if 'max_amount' in kwargs:
            conditions.append('d.amount <= ?')
            params.append(kwargs['max_amount'])
        if 'start_date' in kwargs:
            conditions.append('d.donation_date >= ?')
            params.append(kwargs['start_date'])
        if 'end_date' in kwargs:
            conditions.append('d.donation_date <= ?')
            params.append(kwargs['end_date'])

        if conditions:
            base_query += ' AND ' + ' AND '.join(conditions)

        self.cursor.execute(base_query, params)
        results = self.cursor.fetchall()
        return [dict(zip([col[0] for col in self.cursor.description], row)) for row in results]

    def update(self, donation_id: int, donation_data: Dict[str, Any]) -> bool:
        """Update donation information"""
        allowed_fields = ['amount', 'donation_date', 'gift_aid', 'notes']
        update_fields = []
        values = []

        for key, value in donation_data.items():
            if key in allowed_fields:
                update_fields.append(f"{key} = ?")
                values.append(value)

        if not update_fields:
            return True

        values.append(donation_id)
        sql = f"UPDATE donations SET {', '.join(update_fields)} WHERE donation_id = ?"
        self.cursor.execute(sql, values)
        self.conn.commit()
        return True

    def delete(self, donation_id: int) -> bool:
        """Delete a donation"""
        self.cursor.execute("DELETE FROM donations WHERE donation_id = ?", (donation_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0