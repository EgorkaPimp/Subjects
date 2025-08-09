from app import app
from flask import render_template
from .extensions import db

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registration')
def create_user():
    return render_template('create-character.html')