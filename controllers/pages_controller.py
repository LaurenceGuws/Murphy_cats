from flask import Blueprint, redirect, render_template, request, url_for

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def home():
    return render_template('index.html')

@pages_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your registration logic here
        return redirect(url_for('pages.home'))
    return render_template('register.html')

@pages_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here
        return redirect(url_for('pages.home'))
    return render_template('login.html')

@pages_bp.route('/profile')
def profile():
    return render_template('profile.html')

@pages_bp.route('/upload_document')
def upload_document():
    return render_template('upload_document.html')
