from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# URL base da API FastAPI
API_URL = "http://localhost:8000/api/v1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui implementaremos a lógica de login
        email = request.form.get('email')
        password = request.form.get('password')
        # TODO: Adicionar chamada à API para autenticar usuário
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui implementaremos a lógica de registro
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        # TODO: Adicionar chamada à API para criar usuário
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
