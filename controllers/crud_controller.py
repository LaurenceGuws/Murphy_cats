from flask import Blueprint, render_template, request, jsonify
from utils.db_instance import db
from sqlalchemy.inspection import inspect

crud_bp = Blueprint('crud', __name__, url_prefix='/crud')

@crud_bp.route('/<model_name>/', methods=['GET'])
def list(model_name):
    model_class = get_model_class(model_name)
    if not model_class:
        return jsonify({'error': 'Model not found'}), 404
    
    instances = model_class.query.all()
    instances_data = [instance.to_dict() for instance in instances]
    
    return render_template('index.html', model_name=model_name, instances=instances_data)

def get_model_class(model_name):
    from models import cat, volunteer, death, vetvisit, locationmove, document, adopter
    model_classes = {
        'cats': cat.Cat,
        'volunteers': volunteer.Volunteer,
        'deaths': death.Death,
        'vetvisits': vetvisit.VetVisit,
        'locationmoves': locationmove.LocationMove,
        'documents': document.Document,
        'adopters': adopter.Adopter,
    }
    return model_classes.get(model_name.lower())
