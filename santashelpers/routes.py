from flask import Flask, flash, redirect, url_for, session, logging, request, render_template
from santashelpers import db, app
from santashelpers.models import Activeuser, generate_password_hash, check_password_hash





@app.route("/")
def home():
    return render_template("landing_page.html")


@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        id = request.form.get("id")
        email = request.form.get("email")
        fullname = request.form.get("fullname")
        username = request.form.get("username")
        password = request.form.get("password")

        # Checking for existing users email
        existing_email = Activeuser.query.filter_by(email=email).first()
        if existing_email == True:
            flash('Email already registered. Please log in.', 'error')
            return render_template('register.html', error="Username already registered.")
            

        # Checking for existing users username
        existing_username = Activeuser.query.filter_by(username=username).first()
        if existing_username:
            flash('Username already registered. Please log in.', 'error')
            return render_template('register.html', error="Username already registered.")
        
        # New user sign up
        new_user = Activeuser(
            email=email,
            fullname=fullname,
            username=username,
            password = generate_password_hash(request.form.get("password"))
        )
        

        db.session.add(new_user)
        db.session.commit()
        
        flash('You have successfully registered! Feel free to sign in.', 'success')
        return redirect(url_for('sign_in'))
    
    return render_template('register.html')


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    return render_template('sign_in.html')

