import os
from flask import Flask
from flask_cors import CORS
from utils.db_instance import db
from controllers.cat_controller import cat_bp
from controllers.volunteer_controller import volunteer_bp
from controllers.adopter_controller import adopter_bp
from controllers.vetvisit_controller import vetvisit_bp
from controllers.locationmove_controller import locationmove_bp
from controllers.document_controller import document_bp
from controllers.death_controller import death_bp
from controllers.pages_controller import pages_bp
from controllers.crud_controller import crud_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'cats.db')
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
app.register_blueprint(pages_bp)
app.register_blueprint(crud_bp)

if __name__ == '__main__':
    app.run(debug=True)
