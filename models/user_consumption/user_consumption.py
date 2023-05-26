from models.db import db
from models import User
from datetime import date


class UserConsumption(db.Model):
  __tablename__ = "user_consumption"
  id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
  date = db.Column(db.Date)
  total_consumption = db.Column(db.Float)
  user_id = db.Column(db.Integer(), db.ForeignKey(User.id), nullable=False)


  def find_by_date_and_id(date, id):
    return UserConsumption.query.filter_by(date = date, user_id = id).first()
  
  def increase_consumption(date, id, qtd):
    UserConsumption.query.filter_by(date = date, user_id = id)\
                .update(dict(total_consumption=qtd))
    db.session.commit()

  def create_today_date(id):
    today = date.today()
    user_consumption = UserConsumption(date = today.strftime("%Y-%m-%d"), total_consumption = 0, user_id = id)
    db.session.add(user_consumption)
    db.session.commit()

