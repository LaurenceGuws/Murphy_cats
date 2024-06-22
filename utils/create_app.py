# utils/create_app.py
import os
from flask import Flask
from utils.db_instance import db
from controllers.cat_controller import cat_bp
from controllers.volunteer_controller import volunteer_bp
from controllers.adopter_controller import adopter_bp
from controllers.vetvisit_controller import vetvisit_bp
from controllers.locationmove_controller import locationmove_bp
from controllers.document_controller import document_bp
from controllers.death_controller import death_bp

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'instance', 'cats.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import models
    from models import cat, volunteer, death, vetvisit, locationmove, document, adopter

    # Register Blueprints
    app.register_blueprint(cat_bp)
    app.register_blueprint(volunteer_bp)
    app.register_blueprint(adopter_bp)
    app.register_blueprint(vetvisit_bp)
    app.register_blueprint(locationmove_bp)
    app.register_blueprint(document_bp)
    app.register_blueprint(death_bp)

    @app.route('/')
    def index():
        return "Welcome to the Cat Foster Community API"

    return app
