# controllers/adopter_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.adopter import Adopter
from sqlalchemy.exc import IntegrityError

adopter_bp = Blueprint('adopters', __name__, url_prefix='/adopters')

@adopter_bp.route('/', methods=['GET'])
def list_adopters():
    adopters = Adopter.query.all()
    return jsonify([adopter.to_dict() for adopter in adopters])

@adopter_bp.route('/<int:adopter_id>', methods=['GET'])
def get_adopter(adopter_id):
    adopter = Adopter.query.get_or_404(adopter_id)
    return jsonify(adopter.to_dict())

@adopter_bp.route('/', methods=['POST'])
def create_adopter():
    data = request.json
    if 'AdopterID' in data:
        data.pop('AdopterID')  # Ensure AdopterID is not set explicitly
    adopter = Adopter(**data)
    db.session.add(adopter)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Adopter with this ID already exists or invalid data provided.'}), 400
    return jsonify(adopter.to_dict()), 201

@adopter_bp.route('/<int:adopter_id>', methods=['PUT'])
def update_adopter(adopter_id):
    adopter = Adopter.query.get_or_404(adopter_id)
    data = request.json
    for key, value in data.items():
        setattr(adopter, key, value)
    db.session.commit()
    return jsonify(adopter.to_dict())

@adopter_bp.route('/<int:adopter_id>', methods=['DELETE'])
def delete_adopter(adopter_id):
    adopter = Adopter.query.get_or_404(adopter_id)
    db.session.delete(adopter)
    db.session.commit()
    return '', 204
