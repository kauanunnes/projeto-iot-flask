from flask import Blueprint, render_template, redirect, url_for, session
from flask_login import login_required, current_user

base = Blueprint("base", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@base.route("/")
@login_required
def base_index():
    return render_template("base/home.html", current_user=current_user)
