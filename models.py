from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  student_number = db.Column(db.String(8), unique=True)
  password = db.Column(db.String(128))
  name = db.Column(db.String(128))