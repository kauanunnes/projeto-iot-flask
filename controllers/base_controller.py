from flask import Blueprint, render_template, redirect, url_for, session

base = Blueprint("base", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@base.route("/")
def base_index():
    logged_in=session.get('logged_in')
    return render_template("base/base_index.html", logged_in=logged_in)
