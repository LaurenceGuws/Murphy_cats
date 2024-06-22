# models/document.py
from utils.db_instance import db

class Document(db.Model):
    __tablename__ = 'Documents'
    DocID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Type = db.Column(db.String, nullable=False)
    File = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'DocID': self.DocID,
            'Type': self.Type,
            'File': self.File
        }
