from models.db import db
from models import User

class Sensor(db.Model):
  __tablename__ = "sensor"
  id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
  sensor_name = db.Column(db.String(100))
  water_qtd = db.Column(db.Integer)
  user_id = db.Column(db.Integer(), db.ForeignKey(User.id), nullable=False)

  def get_sensor_by_user_id(user_id):
    return Sensor.query.filter_by(user_id = user_id).all()
  
  def add_sensor(sensor_name, water_qtd, user_id):
    sensor = Sensor(sensor_name = sensor_name, water_qtd = water_qtd, user_id = user_id)
    db.session.add(sensor)
    db.session.commit()