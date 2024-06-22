from models import db
from models.death import Death

class DeathService:
    @staticmethod
    def get_all_deaths():
        return Death.query.all()

    @staticmethod
    def get_death_by_id(death_id):
        return Death.query.get(death_id)

    @staticmethod
    def create_death(data):
        death = Death(**data)
        db.session.add(death)
        db.session.commit()
        return death

    @staticmethod
    def update_death(death_id, data):
        death = Death.query.get(death_id)
        if death:
            for key, value in data.items():
                setattr(death, key, value)
            db.session.commit()
        return death

    @staticmethod
    def delete_death(death_id):
        death = Death.query.get(death_id)
        if death:
            db.session.delete(death)
            db.session.commit()
        return death
