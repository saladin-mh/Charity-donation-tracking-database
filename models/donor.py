from typing import Dict, Any, Optional
from database import Database

class DonorModel:
    def __init__(self, db: Database):
        self.db = db
        self.cursor = db.cursor
        self.conn = db.conn

    def add(self, donor_data: Dict[str, Any]) -> int:
        """Add a new donor to the database"""
        sql = '''
            INSERT INTO donors (
                first_name, surname, business_name, postcode,
                house_number, phone_number, donor_type
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (
            donor_data['first_name'],
            donor_data['surname'],
            donor_data.get('business_name'),
            donor_data['postcode'],
            donor_data['house_number'],
            donor_data['phone_number'],
            donor_data['donor_type']
        ))
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, donor_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a donor by ID"""
        self.cursor.execute('SELECT * FROM donors WHERE donor_id = ?', (donor_id,))
        result = self.cursor.fetchone()
        if result:
            return dict(zip([col[0] for col in self.cursor.description], result))
        return None

    def update(self, donor_id: int, donor_data: Dict[str, Any]) -> bool:
        """Update donor information"""
        current_donor = self.get(donor_id)
        if not current_donor:
            return False

        update_fields = []
        values = []
        for key, value in donor_data.items():
            if key in current_donor and value != current_donor[key]:
                update_fields.append(f"{key} = ?")
                values.append(value)

        if not update_fields:
            return True

        values.append(donor_id)
        sql = f"UPDATE donors SET {', '.join(update_fields)} WHERE donor_id = ?"
        self.cursor.execute(sql, values)
        self.conn.commit()
        return True

    def can_delete(self, donor_id: int) -> bool:
        """Check if a donor can be deleted (no associated donations)"""
        self.cursor.execute("SELECT COUNT(*) FROM donations WHERE donor_id = ?", (donor_id,))
        count = self.cursor.fetchone()[0]
        return count == 0

    def delete(self, donor_id: int) -> bool:
        """Delete a donor if they have no associated donations"""
        if not self.can_delete(donor_id):
            return False
        self.cursor.execute("DELETE FROM donors WHERE donor_id = ?", (donor_id,))
        self.conn.commit()
        return True