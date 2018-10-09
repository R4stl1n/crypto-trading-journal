from flask import jsonify
from flask import Blueprint
from flask import render_template
from flask_security import login_required

analytics_bp = Blueprint('analytics_bp', __name__, template_folder='templates')

@analytics_bp.route('/analytics')
@login_required
def analytics_view():
    return render_template('private/analytics.html')