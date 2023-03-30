from flask import Blueprint, render_template, redirect, session, request
import csv

users = []

filename = 'C:/Users/kaua.nunes/Desktop/faculdade/experiancia-criativa/projeto-pbl/models/users.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        users.append({
            'name': row[0],
            'email': row[1],
            'password': row[2],
            'admin':  row[3]
        })


auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

def register(name, email, password):
    flag = True
    for user in users:
        if email == user['email']:
            flag = False
    if flag == False:
        return render_template("auth/auth_index.html", error='Email já consta no sistema!')
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, lineterminator='\n')
        nova_linha = [name, email, password, False]
        writer.writerow(nova_linha)
        file.close()
    session['logged_in'] = True
    return redirect('/')


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
        return register(request.form['registerInputName'], request.form['registerInputEmail'], request.form['registerInputPassword'])
    else: 
        return login(request.form['loginInputEmail'], request.form['loginInputPassword'])
