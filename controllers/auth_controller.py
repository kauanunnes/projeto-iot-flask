from flask import Blueprint, render_template, redirect, session, request
from models.users.users import user_by_email, register, users
from models.user_consumption.user_consumption import create_today_date

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

def login(email, password):
    flag = False
    for user in users:
        if email == user['email']:
            if password == user['password']:
                session['name'] = user['name']
                session['email'] = user['email']
                session['logged_in'] = True
                session['is_admin'] = True if user['admin'] == "True" else False 
                flag = True
    if flag == False:
        return render_template("auth/auth_index.html", error='Email ou senha inválidos!')
    create_today_date(user_by_email(email)['id'])
    return redirect('/')

@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@auth.route("/", methods=['POST', 'GET'])
def auth_index():
    if session.get('logged_in'):
        return redirect("/")
    if request.method == 'GET':
        return render_template("auth/auth_index.html")
    if request.form['type'] == 'register':
        flag = register(request.form['registerInputName'], request.form['registerInputEmail'], request.form['registerInputPassword'],  request.form['registerInputWeight'])
        if not flag:
            return render_template("auth/auth_index.html", error='Email já consta no sistema!')
        session['logged_in'] = True
        session['name'] = request.form['registerInputName']
        session['email'] = request.form['registerInputEmail']
        session['is_admin'] = False
        return redirect("/")
    else: 
        return login(request.form['loginInputEmail'], request.form['loginInputPassword'])
