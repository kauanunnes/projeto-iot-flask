from flask import Blueprint, render_template,redirect,request,session,flash
from models import User, Sensor
from flask_login import login_required, current_user
# from models.users.users import users, user_by_email

people = Blueprint("people", __name__, template_folder='./views/', static_folder='./static/', root_path="./")
frame_value = 'privacy'

@people.route("/")
@login_required
def people_index():
    global frame_value
    return render_template("/people/people_index.html", user = current_user, frame_value=frame_value)

@people.route("/list_all")
@login_required
def list_all():
    global frame_value
    if not current_user.admin:
        frame_value = 'privacy'
        return redirect("/people")
    users = User.get_users()
    return render_template("/people/people_list_all.html", users=users)

@people.route("/privacy")
@login_required
def privacy():
    user = current_user
    return render_template("/people/people_privacy.html", frame_value=frame_value, user=user)


@people.route("/add_sensor", methods=['GET', 'POST'])
@login_required
def add_new_sensor():
    if request.method == 'POST':
        Sensor.add_sensor(request.form['addInputName'], request.form['addInputWater'], current_user.id)
        flash('Sensor adicionado com sucesso.')
    return render_template("/people/people_sensor.html", frame_value=frame_value, user=current_user)

@people.route("/to_list_all")
def change_to_list_all():
    global frame_value
    frame_value = 'list_all'
    if not current_user.admin:
        frame_value = 'privacy'
    return redirect("/people")

@people.route("/to_privacy")
def change_to_privacy():
    global frame_value
    frame_value = 'privacy'
    return redirect("/people")

@people.route("/to_add_sensor")
def change_to_add_sensor():
    global frame_value
    frame_value = 'add_sensor'
    return redirect("/people")