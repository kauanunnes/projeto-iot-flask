from flask import Blueprint, render_template, redirect, session, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, current_user, logout_user
# from models.users.users import user_by_email, register, users
# from models.user_consumption.user_consumption import create_today_date

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

def login(email, password):
    user = User.get_user_by_email(email=email)
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.auth_index'))
    login_user(user, remember=True)
    return redirect('/')

@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@auth.route("/", methods=['POST', 'GET'])
def auth_index():
    if current_user.is_authenticated:
        return redirect("/")
    if request.method == 'GET':
        return render_template("auth/auth_index.html")
    if request.form['type'] == 'register':
        email = request.form['registerInputEmail']
        user = User.get_user_by_email(email)
        print(user)
        print(email)
        if user:
            flash('Email address already exists!')
            return redirect(url_for("auth.auth_index"))
        User.register(request.form['registerInputName'], request.form['registerInputEmail'], request.form['registerInputPassword'],  request.form['registerInputWeight'])
        return redirect(url_for("auth.auth_index"))
    else: 
        return login(request.form['loginInputEmail'], request.form['loginInputPassword'])
