# models/adopter.py
from utils.db_instance import db

class Adopter(db.Model):
    __tablename__ = 'Adopters'
    AdopterID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String, nullable=False)
    Contact = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'AdopterID': self.AdopterID,
            'Name': self.Name,
            'Contact': self.Contact
        }
