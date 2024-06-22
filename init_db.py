# init_db.py
from utils.create_app import create_app
from utils.db_instance import db

app = create_app()

with app.app_context():
    db.drop_all()  # Optional: Drop all tables before creating them
    db.create_all()
    print("Database tables created successfully")
