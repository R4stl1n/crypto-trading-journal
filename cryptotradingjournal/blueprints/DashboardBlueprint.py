from flask import jsonify
from flask import Blueprint
from flask import render_template
from flask_security import login_required

dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates')

@dashboard_bp.route('/dashboard')
@login_required
def index():
    return render_template('private/dashboard.html')