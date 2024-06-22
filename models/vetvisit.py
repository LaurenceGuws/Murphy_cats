# models/vet_visit.py
from utils.db_instance import db

class VetVisit(db.Model):
    __tablename__ = 'VetVisits'
    VisitID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CatID = db.Column(db.Integer, db.ForeignKey('Cats.CatID'), nullable=False)
    Diagnosis = db.Column(db.String)
    MedsPrescribed = db.Column(db.String)
    Date = db.Column(db.DateTime, nullable=False)  # Changed to DateTime

    def to_dict(self):
        return {
            'VisitID': self.VisitID,
            'CatID': self.CatID,
            'Diagnosis': self.Diagnosis,
            'MedsPrescribed': self.MedsPrescribed,
            'Date': self.Date.isoformat()
        }
