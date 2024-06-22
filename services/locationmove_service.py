from models import db
from models.locationmove import LocationMove

class LocationMoveService:
    @staticmethod
    def get_all_locationmoves():
        return LocationMove.query.all()

    @staticmethod
    def get_locationmove_by_id(move_id):
        return LocationMove.query.get(move_id)

    @staticmethod
    def create_locationmove(data):
        locationmove = LocationMove(**data)
        db.session.add(locationmove)
        db.session.commit()
        return locationmove

    @staticmethod
    def update_locationmove(move_id, data):
        locationmove = LocationMove.query.get(move_id)
        if locationmove:
            for key, value in data.items():
                setattr(locationmove, key, value)
            db.session.commit()
        return locationmove

    @staticmethod
    def delete_locationmove(move_id):
        locationmove = LocationMove.query.get(move_id)
        if locationmove:
            db.session.delete(locationmove)
            db.session.commit()
        return locationmove
