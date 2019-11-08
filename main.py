from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/request')
@login_required
def request():
  name = current_user.name
  return render_template('request.html', name=current_user.name)
