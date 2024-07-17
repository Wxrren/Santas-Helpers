from santashelpers import db
from sqlalchemy.orm import relationship




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