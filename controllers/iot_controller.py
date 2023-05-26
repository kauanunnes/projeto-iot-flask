from flask import Blueprint, render_template,redirect,session, request
from datetime import date, datetime, timedelta
from models import User, Sensor, UserConsumption
from flask_login import login_required, current_user


today = date.today()
yesterday = datetime.now() - timedelta(1)
tomorrow = datetime.now() + timedelta(1)

iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

@iot.route("/", methods=['POST', 'GET'])
@login_required
def iot_index():
    user = current_user
    if request.method == 'POST':
        UserConsumption.increase_consumption(today.strftime("%Y-%m-%d"), user.id, request.form['qtd'])
    consumption = UserConsumption.find_by_date_and_id(today.strftime("%Y-%m-%d"), user.id)
    if (consumption == None):
        UserConsumption.create_today_date(user.id)
        consumption = UserConsumption.find_by_date_and_id(today.strftime("%Y-%m-%d"), user.id)
    yesterday_consumption = UserConsumption.find_by_date_and_id(yesterday.strftime("%Y-%m-%d"), user.id)
    total_consumption = consumption.total_consumption
    total_consumption = int(total_consumption)
    is_aim_finished = total_consumption >= (user.weight * 35)
    user_sensors = Sensor.get_sensor_by_user_id(user.id)
    return render_template("/iot/iot_index.html", logged_in=session.get('logged_in'), user_sensors=user_sensors,today=today, is_aim_finished=is_aim_finished, yesterday=yesterday, tomorrow=tomorrow, user=user, consumption=consumption, total_consumption=total_consumption, yesterday_consumption=yesterday_consumption)