from flask import Flask, render_template, session, g
from controllers.base_controller import base
from controllers.auth_controller import auth
from controllers.people_controller import people
from controllers.iot_controller import iot

app = Flask(__name__, template_folder="./views/", static_folder="./static/")
app.secret_key = 'mysecretkey'
app.register_blueprint(base, url_prefix='/base')
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def index():
    return render_template("home.html", logged_in=session.get('logged_in'), name=session.get('is_admin'))

if __name__ == "__main__":
    app.run(debug=True)