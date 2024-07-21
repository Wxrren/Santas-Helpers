from santashelpers import db
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash




class Activeuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.id} - {self.username}>"


class christmas_folders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    due_date = db.Column(db.Date, nullable=False)
    folder_name = db.Column(db.String(25), unique=True, nullable=False)
    activeuser = db.relationship("Activeuser", backref=db.backref("christmas_folders", cascade="all, delete"), lazy=True)
    activeuser_id = db.Column(db.Integer, db.ForeignKey('activeuser.id'), nullable=False)



class Christmas_lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    user_christmas_list = db.Column(db.Text, nullable=False)
    letter_to_santa = db.Column(db.Boolean, default=False, nullable=False)
    milk_and_cookies = db.Column(db.Boolean, default=False, nullable=False)
    favourite_reindeer = db.Column(db.Text, nullable=False)
    activeuser = db.relationship("Activeuser", backref=db.backref("christmas_folders", cascade="all, delete"), lazy=True)
    activeuser_id = db.Column(db.Integer, db.ForeignKey('activeuser.id'), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
