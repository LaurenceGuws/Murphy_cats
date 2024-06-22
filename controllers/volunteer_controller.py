# controllers/volunteer_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.volunteer import Volunteer
from sqlalchemy.exc import IntegrityError

volunteer_bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@volunteer_bp.route('/', methods=['GET'])
def list_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([volunteer.to_dict() for volunteer in volunteers])

@volunteer_bp.route('/<int:volunteer_id>', methods=['GET'])
def get_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    return jsonify(volunteer.to_dict())

@volunteer_bp.route('/', methods=['POST'])
def create_volunteer():
    data = request.json
    volunteer = Volunteer(**data)
    db.session.add(volunteer)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'A volunteer with this username already exists.'}), 400
    return jsonify(volunteer.to_dict()), 201

@volunteer_bp.route('/<int:volunteer_id>', methods=['PUT'])
def update_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    data = request.json
    for key, value in data.items():
        setattr(volunteer, key, value)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'A volunteer with this username already exists.'}), 400
    return jsonify(volunteer.to_dict())

@volunteer_bp.route('/<int:volunteer_id>', methods=['DELETE'])
def delete_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    db.session.delete(volunteer)
    db.session.commit()
    return '', 204
