from flask import Blueprint, render_template,redirect,request,session
import csv
users = []

filename = 'C:/Users/kaua.nunes/Desktop/faculdade/experiancia-criativa/projeto-pbl/models/users.csv'


with open(filename, 'r', encoding='utf-8') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        users.append({
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'password': row[3],
            'admin':  row[4]
        })

people = Blueprint("people", __name__, template_folder='./views/', static_folder='./static/', root_path="./")
frame_value = 'privacy'
# if not session.get('is_admin'):
#     frame_value = 'privacy'

@people.route("/")
def people_index():
    global frame_value
    if not session.get('logged_in'):
        return redirect("/")
    if not session.get('is_admin'):
        frame_value = 'privacy'
    return render_template("/people/people_index.html", logged_in=session.get('logged_in'), is_admin=session.get('is_admin'), frame_value=frame_value)

@people.route("/list_all")
def list_all():
    if not session.get('logged_in'):
        return redirect("/")
    return render_template("/people/people_list_all.html", users=users)

@people.route("/privacy")
def privacy():
    if not session.get('logged_in'):
        return redirect("/")
    # if request.method == 'POST':
    #     update(request.form['updateInputName'], request.form['updateInputEmail'], request.form['updateInputPassword'])
    user = {}
    for item in users:
        if item['email'] == session.get('email'):
            user = {
                'name': item['name'],
                'email': item['email']
            }
    return render_template("/people/people_privacy.html", frame_value=frame_value, user=user)

@people.route("/to_list_all")
def change_to_list_all():
    if not session.get('logged_in'):
        return redirect("/")
    global frame_value
    frame_value = 'list_all'
    if not session.get('is_admin'):
        frame_value = 'privacy'
    return redirect("/people")

@people.route("/to_privacy")
def change_to_privacy():
    if not session.get('logged_in'):
        return redirect("/")
    global frame_value
    frame_value = 'privacy'
    return redirect("/people")

# def update(name, email, passowrd):
#     user = {}
#     for item in users:
#         if item['email'] == session.get('email'):
#             user = item
    
#     print('a')
