from flask import render_template
from santashelpers import app, db
from sqlalchemy.orm import relationship



@app.route("/")
def home():
    return render_template("landing_page.html")


@app.route("/register_user")
def register_user():
    return render_template("register.html")


@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")