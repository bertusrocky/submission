from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, Submission
from datetime import datetime
from .import db


main = Blueprint('main', __name__)

# Render request page
@main.route('/request')
@login_required
def submit():
  name = current_user.name
  student_number = current_user.student_number

  requests = Submission.query.all()

  return render_template('request.html', name=current_user.name, student_number=current_user.student_number, requests=requests)

# Submit request
@main.route('/request', methods=['POST'])
@login_required
def submit_post():
  title = request.form.get('title')
  author = request.form.get('author')
  isbn = request.form.get('isbn')
  campus = request.form.get('campus')
  person = current_user.student_number


  new_submission = Submission(title=title, author=author,isbn=isbn, campus=campus, person=person)

  db.session.add(new_submission)
  db.session.commit()

  flash('Request submitted!')
  return redirect(url_for('main.submit'))

# Allow the user to delete their own request
@main.route('/delete/<int:id>')
@login_required
def delete_submission(id):
  submission_to_delete = Submission.query.get(id)
  db.session.delete(submission_to_delete)
  db.session.commit()
  flash('Request deleted!')
  return redirect(url_for('main.submit'))

# Admin can delete all requests
@main.route('/delete_all')
@login_required
def delete_all():
  db.session.query(Submission).delete()
  db.session.commit()
  return redirect(url_for('main.submit'))

