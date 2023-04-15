from flask import Blueprint, render_template,redirect,session, request
from datetime import date, datetime, timedelta
from models.users.users import user_by_email
from models.user_consumption.user_consumption import find_by_date_and_id, increase_consumption, consumptions, refresh
from models.sensor.sensor import sensors, sensors_by_id

today = date.today()
yesterday = datetime.now() - timedelta(1)
tomorrow = datetime.now() + timedelta(1)



iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

@iot.route("/", methods=['POST', 'GET'])
def iot_index():
    if not session.get('logged_in'):
        return redirect("/")
    refresh()
    user = user_by_email(session.get('email'))
    if request.method == 'POST':
        print( request.form['qtd'])
        increase_consumption(today.strftime("%d-%m-%Y"), user['id'], request.form['qtd'])
    consumption = find_by_date_and_id(today.strftime("%d-%m-%Y"), user['id'])
    yesterday_consumption = find_by_date_and_id(yesterday.strftime("%d-%m-%Y"), user['id'])
    total_consumption = consumption.get('total_consumption') 
    total_consumption = int(total_consumption)
    is_aim_finished = total_consumption >= (user['weight'] * 35)
    user_sensors = sensors_by_id(user['id'])
    return render_template("/iot/iot_index.html", logged_in=session.get('logged_in'), user_sensors=user_sensors,today=today, is_aim_finished=is_aim_finished, yesterday=yesterday, tomorrow=tomorrow, user=user, consumption=consumption, total_consumption=total_consumption, yesterday_consumption=yesterday_consumption)