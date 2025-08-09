from app import app
from flask import render_template, request, flash, redirect, url_for
from app.forms import RegistrationForm
from .extensions import db
from .models.user import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role_master=form.role_master.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('home'))
    return render_template('create-character.html', form=form)