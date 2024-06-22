# controllers/vetvisit_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.vetvisit import VetVisit
from datetime import datetime

vetvisit_bp = Blueprint('vetvisits', __name__, url_prefix='/vetvisits')

def convert_to_datetime(date_str):
    if date_str is not None:
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')
        except ValueError:
            return None
    return None

@vetvisit_bp.route('/', methods=['GET'])
def list_vetvisits():
    vetvisits = VetVisit.query.all()
    return jsonify([vetvisit.to_dict() for vetvisit in vetvisits])

@vetvisit_bp.route('/<int:visit_id>', methods=['GET'])
def get_vetvisit(visit_id):
    vetvisit = VetVisit.query.get_or_404(visit_id)
    return jsonify(vetvisit.to_dict())

@vetvisit_bp.route('/', methods=['POST'])
def create_vetvisit():
    data = request.json
    data['Date'] = convert_to_datetime(data.get('Date'))
    vetvisit = VetVisit(**data)
    db.session.add(vetvisit)
    db.session.commit()
    return jsonify(vetvisit.to_dict()), 201

@vetvisit_bp.route('/<int:visit_id>', methods=['PUT'])
def update_vetvisit(visit_id):
    vetvisit = VetVisit.query.get_or_404(visit_id)
    data = request.json
    data['Date'] = convert_to_datetime(data.get('Date'))
    for key, value in data.items():
        setattr(vetvisit, key, value)
    db.session.commit()
    return jsonify(vetvisit.to_dict())

@vetvisit_bp.route('/<int:visit_id>', methods=['DELETE'])
def delete_vetvisit(visit_id):
    vetvisit = VetVisit.query.get_or_404(visit_id)
    db.session.delete(vetvisit)
    db.session.commit()
    return '', 204
