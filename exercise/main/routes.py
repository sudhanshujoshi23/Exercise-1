from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify, make_response
from flask_login import login_user, current_user, login_required, login_manager, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from exercise import db
from exercise.main.forms import LoginForm, RegistrationForm
from exercise.models import Users
from exercise import Config


main = Blueprint('main', __name__)

@main.route("/")
def Home():
    # Home Page / Welcome Page.
    return render_template('Home.html', title='Welcome')


@main.route('/register', methods=['GET', 'POST'])
def signup_user():
    # Register a new user.
    form = RegistrationForm()
    if form.validate_on_submit():  
        #data = request.get_json()  
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        admin_value = 1 if form.email.data.split('@')[1] == 'sapient.com' else 0
        new_user = Users(public_id=str(uuid.uuid4()), Name=form.Name.data, email= form.email.data, password=hashed_password, admin=admin_value) 
        db.session.add(new_user)  
        db.session.commit()
        return redirect(url_for('main.login'))    

    return render_template('Register.html', title="Register", form=form)


@main.route('/login', methods=['GET', 'POST'])  
def login():
    # Login to the web application.
    if current_user.is_authenticated:
        return redirect(url_for('main.Home')) 
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            token = jwt.encode({'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, Config.SECRET_KEY)
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.Home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('Login.html', title="Login", form=form)

@main.route("/logout")
def logout():
    # Logout from the web application.
    logout_user()
    return redirect(url_for('main.Home'))





 







  

