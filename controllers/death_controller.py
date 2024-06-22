# controllers/death_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.death import Death
from datetime import datetime
from sqlalchemy.exc import IntegrityError

death_bp = Blueprint('deaths', __name__, url_prefix='/deaths')

def convert_to_datetime(date_str):
    if date_str is not None:
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')
        except ValueError:
            return None
    return None

@death_bp.route('/', methods=['GET'])
def list_deaths():
    deaths = Death.query.all()
    return jsonify([death.to_dict() for death in deaths])

@death_bp.route('/<int:death_id>', methods=['GET'])
def get_death(death_id):
    death = Death.query.get_or_404(death_id)
    return jsonify(death.to_dict())

@death_bp.route('/', methods=['POST'])
def create_death():
    data = request.json
    if 'CatID' not in data or data['CatID'] is None:
        return jsonify({'error': 'CatID is required.'}), 400
    data['Date'] = convert_to_datetime(data.get('Date'))
    if data['Date'] is None:
        return jsonify({'error': 'Invalid date format. Expected format: Wed, 01 Jan 2020 00:00:00 GMT'}), 400
    death = Death(**data)
    db.session.add(death)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred. Please ensure all required fields are provided.'}), 400
    return jsonify(death.to_dict()), 201

@death_bp.route('/<int:death_id>', methods=['PUT'])
def update_death(death_id):
    death = Death.query.get_or_404(death_id)
    data = request.json
    if 'CatID' in data and data['CatID'] is None:
        return jsonify({'error': 'CatID cannot be null.'}), 400
    data['Date'] = convert_to_datetime(data.get('Date'))
    if data['Date'] is None:
        return jsonify({'error': 'Invalid date format. Expected format: Wed, 01 Jan 2020 00:00:00 GMT'}), 400
    for key, value in data.items():
        setattr(death, key, value)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred. Please ensure all required fields are provided.'}), 400
    return jsonify(death.to_dict())

@death_bp.route('/<int:death_id>', methods=['DELETE'])
def delete_death(death_id):
    death = Death.query.get_or_404(death_id)
    db.session.delete(death)
    db.session.commit()
    return '', 204
