from models import db
from models.cat import Cat

class CatService:
    @staticmethod
    def get_all_cats():
        return Cat.query.all()

    @staticmethod
    def get_cat_by_id(cat_id):
        return Cat.query.get(cat_id)

    @staticmethod
    def create_cat(data):
        cat = Cat(**data)
        db.session.add(cat)
        db.session.commit()
        return cat

    @staticmethod
    def update_cat(cat_id, data):
        cat = Cat.query.get(cat_id)
        if cat:
            for key, value in data.items():
                setattr(cat, key, value)
            db.session.commit()
        return cat

    @staticmethod
    def delete_cat(cat_id):
        cat = Cat.query.get(cat_id)
        if cat:
            db.session.delete(cat)
            db.session.commit()
        return cat
