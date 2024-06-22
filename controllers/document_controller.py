# controllers/document_controller.py
from flask import Blueprint, request, jsonify
from utils.db_instance import db
from models.document import Document

document_bp = Blueprint('documents', __name__, url_prefix='/documents')

@document_bp.route('/', methods=['GET'])
def list_documents():
    documents = Document.query.all()
    return jsonify([document.to_dict() for document in documents])

@document_bp.route('/<int:doc_id>', methods=['GET'])
def get_document(doc_id):
    document = Document.query.get_or_404(doc_id)
    return jsonify(document.to_dict())

@document_bp.route('/', methods=['POST'])
def create_document():
    data = request.json
    document = Document(**data)
    db.session.add(document)
    db.session.commit()
    return jsonify(document.to_dict()), 201

@document_bp.route('/<int:doc_id>', methods=['PUT'])
def update_document(doc_id):
    document = Document.query.get_or_404(doc_id)
    data = request.json
    for key, value in data.items():
        setattr(document, key, value)
    db.session.commit()
    return jsonify(document.to_dict())

@document_bp.route('/<int:doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    document = Document.query.get_or_404(doc_id)
    db.session.delete(document)
    db.session.commit()
    return '', 204
