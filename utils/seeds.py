from models import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def generate_seeds(db:SQLAlchemy):
  user1 = User(email = "admin@admin", name = "Admin", admin = True, password = generate_password_hash("admin"), weight = 55)
  db.session.add_all([user1])
  db.session.commit()

  sensor1 = Sensor(sensor_name = "Multilaser", water_qtd = 500, user_id = user1.id)
  db.session.add_all([sensor1])
  db.session.commit()
