from flask import Blueprint, render_template,redirect,request,session
from models.users.users import users, user_by_email
from models.sensor.sensor import add_sensor

people = Blueprint("people", __name__, template_folder='./views/', static_folder='./static/', root_path="./")
frame_value = 'privacy'
# if not session.get('is_admin'):
#     frame_value = 'privacy'

@people.route("/")
def people_index():
    global frame_value
    if not session.get('logged_in'):
        return redirect("/")
    return render_template("/people/people_index.html", logged_in=session.get('logged_in'), is_admin=session.get('is_admin'), frame_value=frame_value)

@people.route("/list_all")
def list_all():
    global frame_value
    if not session.get('logged_in'):
        return redirect("/")
    if not session.get('is_admin'):
        frame_value = 'privacy'
        return redirect("/people")
    return render_template("/people/people_list_all.html", users=users)

@people.route("/privacy")
def privacy():
    if not session.get('logged_in'):
        return redirect("/")
    user = user_by_email(session.get('email'))
    return render_template("/people/people_privacy.html", frame_value=frame_value, user=user)


@people.route("/add_sensor", methods=['GET', 'POST'])
def add_new_sensor():
    if not session.get('logged_in'):
        return redirect("/")
    user = user_by_email(session.get('email'))
    if request.method == 'POST':
        add_sensor(request.form['addInputName'], request.form['addInputWater'], user['id'])
    return render_template("/people/people_sensor.html", frame_value=frame_value, user=user)

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

@people.route("/to_add_sensor")
def change_to_add_sensor():
    if not session.get('logged_in'):
        return redirect("/")
    global frame_value
    frame_value = 'add_sensor'
    print(frame_value)
    return redirect("/people")