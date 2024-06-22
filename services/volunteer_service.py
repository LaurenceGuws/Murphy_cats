from models import db
from models.volunteer import Volunteer

class VolunteerService:
    @staticmethod
    def get_all_volunteers():
        return Volunteer.query.all()

    @staticmethod
    def get_volunteer_by_id(volunteer_id):
        return Volunteer.query.get(volunteer_id)

    @staticmethod
    def create_volunteer(data):
        volunteer = Volunteer(**data)
        db.session.add(volunteer)
        db.session.commit()
        return volunteer

    @staticmethod
    def update_volunteer(volunteer_id, data):
        volunteer = Volunteer.query.get(volunteer_id)
        if volunteer:
            for key, value in data.items():
                setattr(volunteer, key, value)
            db.session.commit()
        return volunteer

    @staticmethod
    def delete_volunteer(volunteer_id):
        volunteer = Volunteer.query.get(volunteer_id)
        if volunteer:
            db.session.delete(volunteer)
            db.session.commit()
        return volunteer
