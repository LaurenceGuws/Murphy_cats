# models/location_move.py
from utils.db_instance import db

class LocationMove(db.Model):
    __tablename__ = 'LocationMoves'
    MoveID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CatID = db.Column(db.Integer, db.ForeignKey('Cats.CatID'), nullable=False)
    FromLocation = db.Column(db.String)
    ToLocation = db.Column(db.String, nullable=False)
    Date = db.Column(db.DateTime, nullable=False)  # Changed to DateTime

    def to_dict(self):
        return {
            'MoveID': self.MoveID,
            'CatID': self.CatID,
            'FromLocation': self.FromLocation,
            'ToLocation': self.ToLocation,
            'Date': self.Date.isoformat()
        }
