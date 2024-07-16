from santashelpers import db
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email_address = db.Column(db.String(), nullable=False)
    full_name = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    

    def __init__(self, username, email_address, full_name, password):
        self.username = username
        self.email_address = email_address
        self.full_name = full_name
        self.password = password


    def __repr__(self):
        return f'<User {self.username}>'


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    full_name = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField('Email', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


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