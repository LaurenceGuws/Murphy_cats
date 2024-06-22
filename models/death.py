# models/death.py
from utils.db_instance import db

class Death(db.Model):
    __tablename__ = 'Deaths'
    DeathID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CatID = db.Column(db.Integer, db.ForeignKey('Cats.CatID'), nullable=False)
    CauseOfDeath = db.Column(db.String)
    VetName = db.Column(db.String)
    Date = db.Column(db.DateTime, nullable=False)  # Changed to DateTime
    Location = db.Column(db.String)

    def to_dict(self):
        return {
            'DeathID': self.DeathID,
            'CatID': self.CatID,
            'CauseOfDeath': self.CauseOfDeath,
            'VetName': self.VetName,
            'Date': self.Date.isoformat(),
            'Location': self.Location
        }
