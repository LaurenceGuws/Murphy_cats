from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.volunteer import Volunteer
from sqlalchemy.exc import IntegrityError

volunteer_bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@volunteer_bp.route('', methods=['GET', 'POST', 'OPTIONS'])
@volunteer_bp.route('/', methods=['GET', 'POST', 'OPTIONS'])
def list_or_create_volunteers():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    
    if request.method == 'GET':
        volunteers = Volunteer.query.all()
        return jsonify([volunteer.to_dict() for volunteer in volunteers])

    if request.method == 'POST':
        data = request.json
        volunteer = Volunteer(**data)
        db.session.add(volunteer)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({'error': 'A volunteer with this username already exists.'}), 400
        return jsonify(volunteer.to_dict()), 201

@volunteer_bp.route('/<int:volunteer_id>', methods=['GET', 'PUT', 'DELETE', 'OPTIONS'])
def handle_volunteer(volunteer_id):
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    
    if request.method == 'GET':
        volunteer = Volunteer.query.get_or_404(volunteer_id)
        return jsonify(volunteer.to_dict())

    if request.method == 'PUT':
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

    if request.method == 'DELETE':
        volunteer = Volunteer.query.get_or_404(volunteer_id)
        db.session.delete(volunteer)
        db.session.commit()
        return '', 204

def _build_cors_preflight_response():
    response = jsonify({'status': 'CORS preflight'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

def _corsify_actual_response(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
