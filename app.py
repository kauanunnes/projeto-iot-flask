from flask import Flask, render_template, session, g
from models.db import db, instance 
from utils.create_db import create_db
from controllers.base_controller import base
from controllers.auth_controller import auth
from controllers.people_controller import people
from controllers.iot_controller import iot
from flask_login import LoginManager


app = Flask(__name__, template_folder="./views/", static_folder="./static/")
app.secret_key = 'mysecretkey'
app.register_blueprint(base, url_prefix='/base')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(people, url_prefix='/people')
app.register_blueprint(iot, url_prefix='/iot')


@app.route('/')
def index():
    return render_template("home.html", logged_in=session.get('logged_in'), name=session.get('is_admin'))

if __name__ == "__main__":
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)
    create_db(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.auth_index'
    login_manager.init_app(app)
    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.get_user(user_id)
    app.run(debug=True)