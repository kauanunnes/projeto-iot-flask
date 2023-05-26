from models.db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    email = db.Column(db.String(130))
    password = db.Column(db.String(130))
    admin = db.Column(db.Boolean, default=False)
    weight = db.Column(db.Float)

    sensors = db.relationship('Sensor', backref='users')
    user_consumptions = db.relationship('UserConsumption', backref='users')

    def get_user_by_email(email):
        return User.query.filter_by(email = email).first()
    
    def register(name, email, password, weight):
        user = User(name = name, email = email, weight = weight, password = generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

    def get_users():
        return User.query.all()
    
    def get_user(id):
        print(User.query.filter_by(id = id).first())
        return User.query.filter_by(id = id).first()