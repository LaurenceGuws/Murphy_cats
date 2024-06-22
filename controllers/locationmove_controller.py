# controllers/locationmove_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.locationmove import LocationMove
from datetime import datetime

locationmove_bp = Blueprint('locationmoves', __name__, url_prefix='/locationmoves')

def convert_to_datetime(date_str):
    if date_str is not None:
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')
        except ValueError:
            return None
    return None

@locationmove_bp.route('/', methods=['GET'])
def list_locationmoves():
    locationmoves = LocationMove.query.all()
    return jsonify([move.to_dict() for move in locationmoves])

@locationmove_bp.route('/<int:move_id>', methods=['GET'])
def get_locationmove(move_id):
    locationmove = LocationMove.query.get_or_404(move_id)
    return jsonify(locationmove.to_dict())

@locationmove_bp.route('/', methods=['POST'])
def create_locationmove():
    data = request.json
    data['Date'] = convert_to_datetime(data.get('Date'))
    if data['Date'] is None:
        return jsonify({'error': 'Invalid date format. Expected format: Wed, 01 Jan 2020 00:00:00 GMT'}), 400
    locationmove = LocationMove(**data)
    db.session.add(locationmove)
    db.session.commit()
    return jsonify(locationmove.to_dict()), 201

@locationmove_bp.route('/<int:move_id>', methods=['PUT'])
def update_locationmove(move_id):
    locationmove = LocationMove.query.get_or_404(move_id)
    data = request.json
    data['Date'] = convert_to_datetime(data.get('Date'))
    if data['Date'] is None:
        return jsonify({'error': 'Invalid date format. Expected format: Wed, 01 Jan 2020 00:00:00 GMT'}), 400
    for key, value in data.items():
        setattr(locationmove, key, value)
    db.session.commit()
    return jsonify(locationmove.to_dict())

@locationmove_bp.route('/<int:move_id>', methods=['DELETE'])
def delete_locationmove(move_id):
    locationmove = LocationMove.query.get_or_404(move_id)
    db.session.delete(locationmove)
    db.session.commit()
    return '', 204
