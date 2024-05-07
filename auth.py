from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, db, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from main import app

auth = Blueprint('auth', __name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('note_list'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email'],
        username = request.form['username'],
        password1 = request.form['password1'],
        password2 = request.form['password2']
        if password1 == password2:
            # Check if the email is already registered
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists.', category='error')
                return redirect(url_for('sign_up'))  # Redirect back to sign-up page
            # Hash the password before storing
            hashed_password = generate_password_hash(password1)
            # Create a new user
            new_user = User(email=email, username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Passwords do not match.', category='error')
            return redirect(url_for('auth.sign_up'))  # Redirect back to sign-up page
    return render_template("sign_up.html", user=current_user)

