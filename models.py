from flask_login import UserMixin
from datetime import datetime
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
  isbn = db.Column(db.Integer)
  campus = db.Column(db.String(128))
  date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  person = db.Column(db.Integer)

  def __repr__(self):
    return '<Submission {}>'.format(self.title)