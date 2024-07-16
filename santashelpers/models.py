from santashelpers import db
from sqlalchemy.orm import relationship


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), unique=True, nullable=False)
    email_address = db.Column(db.String(), nullable=False)
    Fullname = db.Column(db.String(25), nullable=False)
    Password = db.Column(db.String(15), nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
         return f"<User(username='{self.Username}', fullname='{self.Fullname}', password='{self.Password}')>"


class List(db.Model):
    # schema for the user relationship model
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users_id'))
    items = Column(db.String(25), nullable=False)
    user = relationship('User', back_populates='lists')


class Christmas_List(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    christmas_list_name = db.Column(db.String(25), unique=True, nullable=False)
    christmas_list_date = db.Column(db.Date, nullable=False)
    christmas_list_description = db.Column(db.Text, nullable=False)
    christmas_list_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
       # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )