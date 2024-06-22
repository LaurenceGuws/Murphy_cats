from models import db
from models.vetvisit import VetVisit

class VetVisitService:
    @staticmethod
    def get_all_vetvisits():
        return VetVisit.query.all()

    @staticmethod
    def get_vetvisit_by_id(visit_id):
        return VetVisit.query.get(visit_id)

    @staticmethod
    def create_vetvisit(data):
        vetvisit = VetVisit(**data)
        db.session.add(vetvisit)
        db.session.commit()
        return vetvisit

    @staticmethod
    def update_vetvisit(visit_id, data):
        vetvisit = VetVisit.query.get(visit_id)
        if vetvisit:
            for key, value in data.items():
                setattr(vetvisit, key, value)
            db.session.commit()
        return vetvisit

    @staticmethod
    def delete_vetvisit(visit_id):
        vetvisit = VetVisit.query.get(visit_id)
        if vetvisit:
            db.session.delete(vetvisit)
            db.session.commit()
        return vetvisit
