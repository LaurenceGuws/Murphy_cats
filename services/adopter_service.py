from models import db
from models.adopter import Adopter

class AdopterService:
    @staticmethod
    def get_all_adopters():
        return Adopter.query.all()

    @staticmethod
    def get_adopter_by_id(adopter_id):
        return Adopter.query.get(adopter_id)

    @staticmethod
    def create_adopter(data):
        adopter = Adopter(**data)
        db.session.add(adopter)
        db.session.commit()
        return adopter

    @staticmethod
    def update_adopter(adopter_id, data):
        adopter = Adopter.query.get(adopter_id)
        if adopter:
            for key, value in data.items():
                setattr(adopter, key, value)
            db.session.commit()
        return adopter

    @staticmethod
    def delete_adopter(adopter_id):
        adopter = Adopter.query.get(adopter_id)
        if adopter:
            db.session.delete(adopter)
            db.session.commit()
        return adopter
