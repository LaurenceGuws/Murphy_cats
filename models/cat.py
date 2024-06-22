# models/cat.py
from utils.db_instance import db

class Cat(db.Model):
    __tablename__ = 'Cats'
    CatID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String, nullable=False)
    Sex = db.Column(db.String)
    Colour = db.Column(db.String)
    Condition = db.Column(db.String)
    Weight = db.Column(db.Float)
    BirthDate = db.Column(db.Date)
    FirstVax = db.Column(db.Date)
    SecondVax = db.Column(db.Date)
    SteriDue = db.Column(db.Date)
    AdoptedDate = db.Column(db.Date)
    ReceivedDate = db.Column(db.Date, nullable=False)
    CurrentLocation = db.Column(db.String, nullable=False)
    AdopterID = db.Column(db.Integer, db.ForeignKey('Adopters.AdopterID'))

    def to_dict(self):
        return {
            'CatID': self.CatID,
            'Name': self.Name,
            'Sex': self.Sex,
            'Colour': self.Colour,
            'Condition': self.Condition,
            'Weight': self.Weight,
            'BirthDate': self.BirthDate,
            'FirstVax': self.FirstVax,
            'SecondVax': self.SecondVax,
            'SteriDue': self.SteriDue,
            'AdoptedDate': self.AdoptedDate,
            'ReceivedDate': self.ReceivedDate,
            'CurrentLocation': self.CurrentLocation,
            'AdopterID': self.AdopterID
        }
