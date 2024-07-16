from flask import render_template
from santashelpers import app, db
from sqlalchemy.orm import relationship
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


@app.route("/")
def home():
    return render_template("base.html")
