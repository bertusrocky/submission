from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, Submission
from .import db


main = Blueprint('main', __name__)

@main.route('/request')
@login_required
def submit():
  name = current_user.name

  requests = Submission.query.all()



  return render_template('request.html', name=current_user.name, requests=requests)


@main.route('/request', methods=['POST'])
@login_required
def submit_post():
  title = request.form.get('title')
  author = request.form.get('author')
  publication = request.form.get('year')
  isbn = request.form.get('isbn')
  campus = request.form.get('campus')

  new_submission = Submission(title=title, author=author, publication=publication, isbn=isbn, campus=campus)

  db.session.add(new_submission)
  db.session.commit()

  return redirect(url_for('main.submit'))


