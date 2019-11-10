from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_number = db.Column(db.String(8), unique=True)
  password = db.Column(db.String(128))
  name = db.Column(db.String(128))


class Submission(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(1000))
  author = db.Column(db.String(1000))
  publication =db.Column(db.Integer)
  isbn = db.Column(db.Integer)
  campus = db.Column(db.String(128))

  def __repr__(self):
    return '<Submission {}>'.format(self.title)