# controllers/cat_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.cat import Cat
from datetime import datetime

cat_bp = Blueprint('cats', __name__, url_prefix='/cats')

def convert_to_datetime(date_str):
    if date_str is not None:
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')
        except ValueError:
            return None
    return None

@cat_bp.route('/', methods=['GET'])
def list_cats():
    cats = Cat.query.all()
    return jsonify([cat.to_dict() for cat in cats])

@cat_bp.route('/<int:cat_id>', methods=['GET'])
def get_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    return jsonify(cat.to_dict())

@cat_bp.route('/', methods=['POST'])
def create_cat():
    data = request.json
    data['BirthDate'] = convert_to_datetime(data.get('BirthDate'))
    data['FirstVax'] = convert_to_datetime(data.get('FirstVax'))
    data['SecondVax'] = convert_to_datetime(data.get('SecondVax'))
    data['SteriDue'] = convert_to_datetime(data.get('SteriDue'))
    data['AdoptedDate'] = convert_to_datetime(data.get('AdoptedDate'))
    data['ReceivedDate'] = convert_to_datetime(data.get('ReceivedDate'))
    cat = Cat(**data)
    db.session.add(cat)
    db.session.commit()
    return jsonify(cat.to_dict()), 201

@cat_bp.route('/<int:cat_id>', methods=['PUT'])
def update_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    data = request.json
    data['BirthDate'] = convert_to_datetime(data.get('BirthDate'))
    data['FirstVax'] = convert_to_datetime(data.get('FirstVax'))
    data['SecondVax'] = convert_to_datetime(data.get('SecondVax'))
    data['SteriDue'] = convert_to_datetime(data.get('SteriDue'))
    data['AdoptedDate'] = convert_to_datetime(data.get('AdoptedDate'))
    data['ReceivedDate'] = convert_to_datetime(data.get('ReceivedDate'))
    for key, value in data.items():
        setattr(cat, key, value)
    db.session.commit()
    return jsonify(cat.to_dict())

@cat_bp.route('/<int:cat_id>', methods=['DELETE'])
def delete_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    return '', 204
