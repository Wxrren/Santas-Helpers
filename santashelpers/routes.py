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
            session['user_id'] = existing_site_user.id
            
            flash('You have successfully signed in!', 'success')
            return redirect(url_for('mainpage'))
        else:
            flash("Oh no! The north pole doesn't recognise the username or password. Try Again.", 'error')
    return render_template('sign_in.html')


@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():

    all_lists = Christmas_lists.query.all()
    return render_template("index.html", all_lists=all_lists)


@app.route("/my_list", methods=["GET", "POST"])
def my_list():
    # Check the user is signed into the session
    if 'user_id' not in session:
            flash('Please log in to create a list.', 'info')
            return redirect(url_for('sign_in'))
    
    # Search for the current user logged into the session and query's their lists
    current_user_id = session['user_id']

    current_user_lists = Christmas_lists.query.filter_by(owner_id=current_user_id).all()

    return render_template("my_list.html", current_user_lists=current_user_lists)

@app.route("/add_list", methods=["GET", "POST"])
def add_list():
    if request.method == "POST":
        if 'user_id' not in session:
            flash('Please log in to create a list.', 'info')
            return redirect(url_for('sign_in'))


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
            owner_id=session['user_id']
        )
        
        # Add the new list to the session and commit
        db.session.add(new_list)
        db.session.commit()

        print(new_list)

        return redirect(url_for('my_list'))


    
    return render_template("add_list.html")


@app.route("/edit_list/<int:list_id>", methods=["GET", "POST"])
def edit_list(list_id):
    edit_user_list = Christmas_lists.query.get_or_404(list_id)

    if edit_user_list.owner_id != session['user_id']:
        flash('You do not have permission to edit this list.', 'warning')
        return redirect(url_for('my_list'))

    if request.method == "POST":
        if 'user_id' not in session:
            flash('Please log in to create a list.', 'info')
            return redirect(url_for('sign_in'))

        edit_user_list.list_name = request.form.get("list_name")
        edit_user_list.due_date = request.form.get("due_date")
        edit_user_list.user_christmas_list = request.form.get("user_christmas_list")
        edit_user_list.letter_to_santa = True if request.form.get("letter_to_santa") == 'on' else False
        edit_user_list.milk_and_cookies = True if request.form.get("milk_and_cookies") == 'on' else False
        edit_user_list.favourite_reindeer = request.form.get("favourite_reindeer")
        
        db.session.commit()

        print(list_id)

        return redirect(url_for('my_list'))

    
    return render_template("edit_list.html", list=edit_user_list)

@app.route("/delete_list/<int:list_id>")
def delete_list(list_id):
    delete_user_list = Christmas_lists.query.get_or_404(list_id)

    if delete_user_list.owner_id != session['user_id']:
        flash('You do not have permission to delete this list.', 'warning')
        return redirect(url_for('my_list'))

    db.session.delete(delete_user_list)
    db.session.commit()
    return redirect(url_for("my_list"))


@app.route("/search", methods=["GET"])
def search():
    search_user = request.args.get('search', '').lower() 
    
    users = Activeuser.query.filter(Activeuser.username.ilike(f'%{search_user}%')).all()
   
    user_lists = []
    for user in users:
        user_lists.extend(user.christmas_lists)
    
    if not search_user:
        return render_template("search.html", all_lists=[])
        
    return render_template("search.html", all_lists=user_lists)