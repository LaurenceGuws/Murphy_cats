from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.volunteer import Volunteer
from utils.db_instance import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Volunteer.query.filter_by(Username=username).first()
        if user and check_password_hash(user.Password, password):
            # Login successful, implement session management here
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')
        
        existing_user = Volunteer.query.filter_by(Username=username).first()
        if existing_user:
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        new_user = Volunteer(Username=username, Email=email, Password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')