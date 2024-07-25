from flask import Flask, flash, redirect, url_for, session, logging, request, render_template
from santashelpers import db, app
from santashelpers.models import Activeuser, generate_password_hash, check_password_hash, Christmas_lists




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
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Search for the user
        existing_site_user = Activeuser.query.filter_by(username=username).first()

        # Check the user exists and the details are correct
        if existing_site_user and check_password_hash(existing_site_user.password, password):
            # success
            session['username'] = username
            flash('You have successfully signed in!', 'success')
            return redirect(url_for('mainpage'))
        else:
            flash("Oh no! The north pole doesn't recognise the username or password. Try Again.", 'error')
    return render_template('sign_in.html')


@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():
    return render_template("index.html")


@app.route("/my_list", methods=["GET", "POST"])
def my_list():
    userlists = list(Christmas_lists.query.order_by(Christmas_lists.id).all())


    return render_template("my_list.html", userlists=userlists)

@app.route("/add_list", methods=["GET", "POST"])
def add_list():
    if request.method == "POST":



        # Retrieve form data
        list_name = request.form.get("list_name")
        due_date = request.form.get("due_date")
        user_christmas_list = request.form.get("user_christmas_list")
        letter_to_santa = True if request.form.get("letter_to_santa") == 'on' else False
        milk_and_cookies = True if request.form.get("milk_and_cookies") == 'on' else False
        favourite_reindeer = request.form.get("favourite_reindeer")

        
        # Create a new Christmas_lists instance
        new_list = Christmas_lists(
            list_name=list_name,
            due_date=due_date,
            user_christmas_list=user_christmas_list,
            letter_to_santa=letter_to_santa,
            milk_and_cookies=milk_and_cookies,
            favourite_reindeer=favourite_reindeer,
        )
        
        # Add the new list to the session and commit
        db.session.add(new_list)
        db.session.commit()

        print(new_list)

        return redirect(url_for('my_list'))


    
    return render_template("add_list.html")

    