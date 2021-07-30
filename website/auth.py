from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db 
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth",__name__)

@auth.route("/login", methods = ['GET','POST'])
def login():

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged In", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password", category="error")

        else:
            flash("User Doesn\'t exists")

    return render_template("login.html", user = current_user)
    

@auth.route("/signup", methods = ['GET','POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        password1 = request.form.get("password1")

        #checking same email and username and password
        email_exists = User.query.filter_by(email = email).first()
        username_exists = User.query.filter_by(username = username).first()

        if email_exists:
            flash("This email is already registered", category="error")
        elif username_exists:
            flash("Username already taken", category="error")
        elif password != password1:
            flash("Password doesn\'t match")
        elif len(username) < 2:
            flash("Username is too short", category="error")
        elif len(password) < 6:
            flash("Password is too short", category="error")
        elif len(email) < 4:
            flash("Email is invalid", category="error")
        else:
            new_user = User(email = email, username = username, password = generate_password_hash(password, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("User Created")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user = current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))



