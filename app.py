# app.py
from utils.create_app import create_app
from flask import jsonify
import logging
from logging.handlers import RotatingFileHandler
from sqlalchemy.exc import IntegrityError

app = create_app()

# Configure the Flask app
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = False

# Set up logging
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

error_handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=3)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

app.logger.addHandler(error_handler)

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all exceptions."""
    # Log the error with minimal information
    app.logger.error(f"An error occurred: {str(e)}")
    # Return a JSON response with the error message
    response = {
        "error": "An internal error occurred. Please try again later."
    }
    return jsonify(response), 500

@app.errorhandler(IntegrityError)
def handle_integrity_error(e):
    """Handle database integrity errors."""
    app.logger.error(f"Database integrity error: {str(e)}")
    response = {
        "error": "A database error occurred. Please check your data and try again."
    }
    return jsonify(response), 400

if __name__ == '__main__':
    app.run(debug=True)
