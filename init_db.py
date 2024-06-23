from app import app
from utils.db_instance import db

with app.app_context():
    db.drop_all()  # Optional: Drop all tables before creating them
    db.create_all()
    print("Database tables created successfully")
