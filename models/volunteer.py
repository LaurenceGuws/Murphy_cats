# models/volunteer.py
from utils.db_instance import db

class Volunteer(db.Model):
    __tablename__ = 'Volunteers'
    VolunteerID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String, unique=True, nullable=False)
    Password = db.Column(db.String, nullable=False)
    Location = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'VolunteerID': self.VolunteerID,
            'Username': self.Username,
            'Password': self.Password,
            'Location': self.Location
        }
